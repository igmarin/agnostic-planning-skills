#!/usr/bin/env python3
"""
Unit tests for task-complexity-classifier

Tests cover class mapping, threshold handling, malformed responses,
provider failure, key handling, and command output without live API.
"""

import copy
import json
import os
import sys
import unittest
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Import after path is set
import classifier
from classifier import classify_task, load_config, get_api_key, DEFAULT_CONFIG


class TestLoadConfig(unittest.TestCase):
    """Test configuration loading."""

    def test_default_config(self):
        """Test that default config is returned when no file exists."""
        config = load_config("/nonexistent/path.json")
        self.assertEqual(config, DEFAULT_CONFIG)

    def test_custom_config(self):
        """Test loading custom config file."""
        # Create a temporary config file
        import tempfile
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            custom_config = {
                "classes": {
                    "trivial": "Very simple",
                    "hard": "Very hard"
                },
                "thresholds": {
                    "min_probability": 0.9,
                    "fallback_class": "hard"
                }
            }
            json.dump(custom_config, f)
            temp_path = f.name

        try:
            config = load_config(temp_path)
            self.assertEqual(config["classes"]["trivial"], "Very simple")
            self.assertEqual(config["thresholds"]["min_probability"], 0.9)
        finally:
            os.unlink(temp_path)


class TestGetApiKey(unittest.TestCase):
    """Test API key retrieval."""

    def test_environment_variable(self):
        """Test getting API key from environment variable."""
        with patch.dict(os.environ, {'TYPESAFE_API_KEY': 'test-key'}):
            key = get_api_key()
            self.assertEqual(key, 'test-key')

    def test_no_api_key(self):
        """Test when no API key is configured."""
        with patch.dict(os.environ, {}, clear=True):
            key = get_api_key()
            self.assertIsNone(key)


class TestClassifyTask(unittest.TestCase):
    """Test task classification."""

    def test_empty_task(self):
        """Test classification of empty task."""
        config = copy.deepcopy(DEFAULT_CONFIG)
        result = classify_task("", config, None)
        self.assertEqual(result["classification"], config["thresholds"]["fallback_class"])
        self.assertTrue(result["fallback_used"])
        self.assertIn("Empty task description", result["reasoning"])

    def test_whitespace_only_task(self):
        """Test classification of whitespace-only task."""
        config = copy.deepcopy(DEFAULT_CONFIG)
        result = classify_task("   \n\t  ", config, None)
        self.assertEqual(result["classification"], config["thresholds"]["fallback_class"])
        self.assertTrue(result["fallback_used"])

    def test_no_api_key(self):
        """Test classification when no API key is configured."""
        config = copy.deepcopy(DEFAULT_CONFIG)
        result = classify_task("Fix a bug", config, None)
        self.assertEqual(result["classification"], config["thresholds"]["fallback_class"])
        self.assertTrue(result["fallback_used"])
        self.assertIn("No TYPESAFE_API_KEY", result["reasoning"])

    def test_dry_run(self):
        """Test dry run mode."""
        config = copy.deepcopy(DEFAULT_CONFIG)
        result = classify_task("Test task", config, None, dry_run=True)
        self.assertEqual(result["classification"], "standard")
        self.assertFalse(result["fallback_used"])
        self.assertIn("Dry run", result["reasoning"])

    @patch('classifier.Client')
    def test_successful_classification(self, mock_client_class):
        """Test successful classification with mocked API."""
        # This test is skipped when typesafe SDK is not available
        # The important behavior (fallback) is tested in other tests
        if not classifier.TYPESAFE_AVAILABLE:
            self.skipTest("typesafe-sdk not installed - fallback behavior is tested elsewhere")

        # Mock the Jev client and response
        mock_client = MagicMock()
        mock_client_class.return_value = mock_client

        mock_response = MagicMock()
        mock_answer = MagicMock()
        mock_answer.choice = "standard"
        mock_answer.probabilities = {"routine": 0.1, "standard": 0.8, "complex": 0.1}
        mock_answer.confidence = 0.85
        mock_response.choices = {"complexity": mock_answer}
        mock_client.system_one.return_value = mock_response

        config = copy.deepcopy(DEFAULT_CONFIG)
        result = classify_task("Add a feature", config, "test-key")

        self.assertEqual(result["classification"], "standard")
        self.assertEqual(result["probability"], 0.8)
        self.assertEqual(result["confidence"], 0.85)
        self.assertFalse(result["fallback_used"])

    @patch('classifier.Client')
    def test_low_probability_fallback(self, mock_client_class):
        """Test fallback when probability is below threshold."""
        if not classifier.TYPESAFE_AVAILABLE:
            self.skipTest("typesafe-sdk not installed - fallback behavior is tested elsewhere")

        mock_client = MagicMock()
        mock_client_class.return_value = mock_client

        mock_response = MagicMock()
        mock_answer = MagicMock()
        mock_answer.choice = "standard"
        mock_answer.probabilities = {"routine": 0.4, "standard": 0.5, "complex": 0.1}
        mock_answer.confidence = 0.5
        mock_response.choices = {"complexity": mock_answer}
        mock_client.system_one.return_value = mock_response

        config = copy.deepcopy(DEFAULT_CONFIG)
        result = classify_task("Add a feature", config, "test-key")

        self.assertEqual(result["classification"], config["thresholds"]["fallback_class"])  # fallback
        self.assertTrue(result["fallback_used"])
        self.assertIn("below threshold", result["reasoning"])

    @patch('classifier.Client')
    def test_api_error_fallback(self, mock_client_class):
        """Test fallback when Jev API raises an error."""
        if not classifier.TYPESAFE_AVAILABLE:
            self.skipTest("typesafe-sdk not installed - fallback behavior is tested elsewhere")

        mock_client_class.side_effect = Exception("API error")

        config = copy.deepcopy(DEFAULT_CONFIG)
        result = classify_task("Add a feature", config, "test-key")

        self.assertEqual(result["classification"], config["thresholds"]["fallback_class"])
        self.assertTrue(result["fallback_used"])
        self.assertIn("error", result["reasoning"])

    @patch('classifier.Client')
    def test_unexpected_error_fallback(self, mock_client_class):
        """Test fallback on unexpected errors."""
        if not classifier.TYPESAFE_AVAILABLE:
            self.skipTest("typesafe-sdk not installed - fallback behavior is tested elsewhere")

        mock_client_class.side_effect = Exception("Unexpected error")

        config = copy.deepcopy(DEFAULT_CONFIG)
        result = classify_task("Add a feature", config, "test-key")

        self.assertEqual(result["classification"], config["thresholds"]["fallback_class"])
        self.assertTrue(result["fallback_used"])
        self.assertIn("Unexpected error", result["reasoning"])

    @patch('classifier.Client')
    def test_missing_answer_fallback(self, mock_client_class):
        """Test fallback when response is missing the expected answer."""
        if not classifier.TYPESAFE_AVAILABLE:
            self.skipTest("typesafe-sdk not installed - fallback behavior is tested elsewhere")

        mock_client = MagicMock()
        mock_client_class.return_value = mock_client

        mock_response = MagicMock()
        mock_response.choices = {}  # No complexity answer
        mock_client.system_one.return_value = mock_response

        config = copy.deepcopy(DEFAULT_CONFIG)
        result = classify_task("Add a feature", config, "test-key")

        self.assertEqual(result["classification"], config["thresholds"]["fallback_class"])
        self.assertTrue(result["fallback_used"])

    def test_custom_fallback_class(self):
        """Test using a custom fallback class."""
        config = copy.deepcopy(DEFAULT_CONFIG)
        config["thresholds"]["fallback_class"] = "standard"

        result = classify_task("", config, None)
        self.assertEqual(result["classification"], "standard")
        self.assertTrue(result["fallback_used"])

    @patch('classifier.Client')
    def test_custom_threshold(self, mock_client_class):
        """Test using a custom probability threshold."""
        if not classifier.TYPESAFE_AVAILABLE:
            self.skipTest("typesafe-sdk not installed - fallback behavior is tested elsewhere")

        mock_client = MagicMock()
        mock_client_class.return_value = mock_client

        mock_response = MagicMock()
        mock_answer = MagicMock()
        mock_answer.choice = "standard"
        mock_answer.probabilities = {"routine": 0.1, "standard": 0.85, "complex": 0.05}
        mock_answer.confidence = 0.9
        mock_response.choices = {"complexity": mock_answer}
        mock_client.system_one.return_value = mock_response

        config = copy.deepcopy(DEFAULT_CONFIG)
        config["thresholds"]["min_probability"] = 0.9  # Higher threshold

        result = classify_task("Add a feature", config, "test-key")

        # Should fall back because 0.85 < 0.9
        self.assertEqual(result["classification"], config["thresholds"]["fallback_class"])
        self.assertTrue(result["fallback_used"])


class TestOutputFormat(unittest.TestCase):
    """Test output format consistency."""

    def test_fallback_output_structure(self):
        """Test that fallback output has correct structure."""
        config = copy.deepcopy(DEFAULT_CONFIG)
        result = classify_task("", config, None)

        required_fields = [
            "classification", "probability", "confidence",
            "reasoning", "distribution", "fallback_used"
        ]

        for field in required_fields:
            self.assertIn(field, result)

        self.assertIsInstance(result["distribution"], dict)
        self.assertIsInstance(result["fallback_used"], bool)

    @patch('classifier.Client')
    def test_distribution_sum(self, mock_client_class):
        """Test that distribution probabilities sum to approximately 1.0."""
        if not classifier.TYPESAFE_AVAILABLE:
            self.skipTest("typesafe-sdk not installed - fallback behavior is tested elsewhere")

        mock_client = MagicMock()
        mock_client_class.return_value = mock_client

        mock_response = MagicMock()
        mock_answer = MagicMock()
        mock_answer.choice = "standard"
        mock_answer.probabilities = {"routine": 0.1, "standard": 0.8, "complex": 0.1}
        mock_answer.confidence = 0.85
        mock_response.choices = {"complexity": mock_answer}
        mock_client.system_one.return_value = mock_response

        config = copy.deepcopy(DEFAULT_CONFIG)
        result = classify_task("Add a feature", config, "test-key")

        distribution = result["distribution"]
        total = sum(distribution.values())
        self.assertAlmostEqual(total, 1.0, places=2)


if __name__ == '__main__':
    unittest.main()
