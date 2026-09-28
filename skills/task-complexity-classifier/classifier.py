#!/usr/bin/env python3
"""
Task Complexity Classifier using Jev (TypeSafe AI)

Classifies task complexity without prescribing specific models or tools.
Completely agnostic - outputs classification data only.
"""

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Dict, Any, Optional

try:
    from typesafe import Client, Error as TypesafeError
    from dotenv import load_dotenv
    TYPESAFE_AVAILABLE = True
except ImportError:
    # Dependencies not installed - will fail gracefully at runtime
    TYPESAFE_AVAILABLE = False
    Client = None
    TypesafeError = Exception


# Default configuration
DEFAULT_CONFIG = {
    "classes": {
        "routine": "Simple, mechanical work with clear steps and minimal domain knowledge",
        "standard": "Moderate complexity requiring some domain knowledge or multiple components",
        "complex": "High complexity requiring deep reasoning, multiple domains, or significant refactoring"
    },
    "thresholds": {
        "min_probability": 0.8,
        "fallback_class": "complex"
    },
    "api": {
        "model": "jev-latest",
        "timeout": 30
    }
}


def load_config(config_path: Optional[str] = None) -> Dict[str, Any]:
    """Load configuration from file or use defaults."""
    if config_path and Path(config_path).exists():
        with open(config_path, 'r') as f:
            user_config = json.load(f)
        # Merge with defaults
        config = DEFAULT_CONFIG.copy()
        config.update(user_config)
        return config

    # Try to load from default location
    default_config_path = Path.home() / ".config" / "task-complexity-classifier" / "config.json"
    if default_config_path.exists():
        with open(default_config_path, 'r') as f:
            user_config = json.load(f)
        config = DEFAULT_CONFIG.copy()
        config.update(user_config)
        return config

    return DEFAULT_CONFIG


def get_api_key() -> Optional[str]:
    """Get API key from environment or config file."""
    # Try environment variable first
    api_key = os.environ.get("TYPESAFE_API_KEY")
    if api_key:
        return api_key

    # Try config file
    env_file = Path.home() / ".config" / "task-complexity-classifier" / ".env"
    if env_file.exists():
        load_dotenv(env_file)
        return os.environ.get("TYPESAFE_API_KEY")

    return None


def classify_task(
    task_description: str,
    config: Dict[str, Any],
    api_key: Optional[str] = None,
    dry_run: bool = False
) -> Dict[str, Any]:
    """
    Classify task complexity using Jev API.

    Returns classification with probability, confidence, and reasoning.
    Falls back to safe default on any error.
    """
    fallback_class = config["thresholds"]["fallback_class"]
    classes = config["classes"]

    # Validate input
    if not task_description or not task_description.strip():
        distribution = {k: 0.0 for k in classes.keys()}
        distribution[fallback_class] = 1.0
        return {
            "classification": fallback_class,
            "probability": 0.0,
            "confidence": 0.0,
            "reasoning": "Empty task description - using safe fallback",
            "distribution": distribution,
            "fallback_used": True
        }

    if dry_run:
        print(f"[DRY RUN] Would classify: {task_description[:100]}...", file=sys.stderr)
        return {
            "classification": "standard",
            "probability": 0.85,
            "confidence": 0.90,
            "reasoning": "Dry run - simulated classification",
            "distribution": {"routine": 0.10, "standard": 0.85, "complex": 0.05},
            "fallback_used": False
        }

    # Check for API key
    if not api_key:
        distribution = {k: 0.0 for k in classes.keys()}
        distribution[fallback_class] = 1.0
        return {
            "classification": fallback_class,
            "probability": 0.0,
            "confidence": 0.0,
            "reasoning": "No TYPESAFE_API_KEY configured - using safe fallback",
            "distribution": distribution,
            "fallback_used": True
        }

    # Check if dependencies are available
    if not TYPESAFE_AVAILABLE:
        distribution = {k: 0.0 for k in classes.keys()}
        distribution[fallback_class] = 1.0
        return {
            "classification": fallback_class,
            "probability": 0.0,
            "confidence": 0.0,
            "reasoning": "typesafe-sdk not installed - using safe fallback. Install with: uv add typesafe-sdk python-dotenv",
            "distribution": distribution,
            "fallback_used": True
        }

    try:
        # Initialize Jev client
        client = Client(api_key=api_key)

        # Build the classification question
        questions = {
            "complexity": {
                "type": "choice",
                "instructions": "Classify the complexity of this task based on effort, domain knowledge required, and number of components involved.",
                "criteria": classes
            }
        }

        # Call Jev API
        response = client.ask(
            model=config["api"]["model"],
            state=task_description,
            questions=questions
        )

        # Parse response
        answer = response.answers.get("complexity")
        if not answer:
            raise ValueError("No complexity answer in response")

        selected_class = answer.choice
        probability = answer.probabilities.get(selected_class, 0.0)
        confidence = answer.confidence if hasattr(answer, 'confidence') else probability

        # Check threshold
        min_probability = config["thresholds"]["min_probability"]
        if probability < min_probability:
            distribution = answer.probabilities.copy()
            return {
                "classification": fallback_class,
                "probability": probability,
                "confidence": confidence,
                "reasoning": f"Probability {probability:.2f} below threshold {min_probability} - using safe fallback",
                "distribution": distribution,
                "fallback_used": True
            }

        return {
            "classification": selected_class,
            "probability": probability,
            "confidence": confidence,
            "reasoning": f"Classified as {selected_class} based on task characteristics",
            "distribution": answer.probabilities,
            "fallback_used": False
        }

    except TypesafeError as e:
        distribution = {k: 0.0 for k in classes.keys()}
        distribution[fallback_class] = 1.0
        return {
            "classification": fallback_class,
            "probability": 0.0,
            "confidence": 0.0,
            "reasoning": f"Jev API error: {str(e)} - using safe fallback",
            "distribution": distribution,
            "fallback_used": True
        }
    except Exception as e:
        distribution = {k: 0.0 for k in classes.keys()}
        distribution[fallback_class] = 1.0
        return {
            "classification": fallback_class,
            "probability": 0.0,
            "confidence": 0.0,
            "reasoning": f"Unexpected error: {str(e)} - using safe fallback",
            "distribution": distribution,
            "fallback_used": True
        }


def main():
    parser = argparse.ArgumentParser(
        description="Classify task complexity using Jev (TypeSafe AI)"
    )
    parser.add_argument(
        "task",
        nargs="?",
        help="Task description to classify (omit to read from stdin)"
    )
    parser.add_argument(
        "--config",
        help="Path to custom config file"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Simulate classification without calling API"
    )
    parser.add_argument(
        "--pretty",
        action="store_true",
        help="Pretty-print JSON output"
    )

    args = parser.parse_args()

    # Load configuration
    config = load_config(args.config)

    # Get task description
    if args.task:
        task_description = args.task
    else:
        # Read from stdin
        task_description = sys.stdin.read()

    # Get API key
    api_key = get_api_key()

    # Classify
    result = classify_task(task_description, config, api_key, args.dry_run)

    # Output
    if args.pretty:
        print(json.dumps(result, indent=2))
    else:
        print(json.dumps(result))


if __name__ == "__main__":
    main()
