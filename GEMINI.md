# Gemini Workspace Context: .github

## Directory Overview

This directory, `/Users/4jp/Development/organization/.github`, is the central organizational `.github` repository for the `ivi374forivi` organization. It is not a standard software project but a configuration and documentation hub that enforces development standards, provides community health files, and automates workflows across all repositories within the organization.

A primary feature of this repository is its "Living Document System," an AI-driven approach to governance and management. It also contains extensive customizations for GitHub Copilot, including custom agents, chat modes, and prompts, to create a highly tailored AI-assisted development environment.

## Key Files and Directories

This repository uses a "convention over configuration" approach, where default files stored here are automatically applied to other repositories in the organization.

*   **`README.md`**: Provides a comprehensive overview of the repository's purpose, structure, and the organization's mission. It is the primary source of information for understanding this repository.
*   **`docs/`**: A centralized location for all documentation, including the `MANIFESTO.md`, `GOVERNANCE.md`, and various best-practice guides.
*   **`for-ai-implementation.txt`**: A key document outlining the complete protocol for the AI-driven GitHub management system.
*   **`dependabot.yml` & `renovate.json`**: These files define the organization-wide configuration for automated dependency updates using Dependabot and Renovate.
*   **`.pre-commit-config.yaml`**: Configures pre-commit hooks to enforce code quality and standards before code is committed.
*   **`ISSUE_TEMPLATE/` & `PULL_REQUEST_TEMPLATE/`**: Contains standardized templates for creating issues and pull requests, ensuring consistency and quality in contributions.
*   **`workflow-templates/`**: A collection of reusable GitHub Actions workflows for CI/CD, security scanning, and other automation tasks that can be used by any repository in the organization.
*   **GitHub Copilot Customizations (`agents/`, `chatmodes/`, `collections/`, `instructions/`, `prompts/`)**: These directories contain a rich set of customizations for GitHub Copilot to provide specialized, context-aware assistance for various development tasks.

## Usage

The contents of this repository are intended to be used as the foundation for all development activities within the `ivi374forivi` organization.

*   **Automatic Inheritance**: Community health files (`CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, etc.) and issue/PR templates are automatically inherited by repositories that do not have their own.
*   **Workflow Adoption**: To use a workflow from `workflow-templates/`, navigate to the "Actions" tab in a repository and select a template from the "By your organization" section.
*   **Contribution**: Changes to organizational standards and practices should be proposed via pull requests to this repository.

## Development Conventions

*   **Commit Messages**: The organization follows the **Conventional Commits** specification. All commit messages should be in the format `<type>: <description>`.
    *   **Types**: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `chore`.
*   **Branching**: The `README.md` mentions branch protection rules are documented in `docs/BRANCH_PROTECTION.md`. Key branches are likely `main` and `develop`.
*   **AI-Driven Management**: All development and administrative activities are expected to align with the principles outlined in the `for-ai-implementation.txt` protocol.
