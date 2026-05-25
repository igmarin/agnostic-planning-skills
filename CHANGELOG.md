# Changelog

All notable changes to `agnostic-planning-skills` will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- GitHub Actions workflow (`.github/workflows/tile-check.yml`) to perform local `tile.json` integrity validation.

### Fixed
- Fixed agent dependencies syntax (from string to YAML list of hashes) in `product-owner`, `project-manager`, `tech-lead`, and `delivery-lead` agents to pass ecosystem consistency audit.
