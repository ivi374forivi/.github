# GitHub Actions Workflows

> **A high-level overview of the GitHub Actions workflows used in this repository.**

**Last Updated**: 2025-11-16
**Version**: 1.0.0

---

This repository contains 30+ GitHub Actions workflows for comprehensive automation.

## Security Workflows

| Workflow | Trigger | Purpose | File |
|----------|---------|---------|------|
| **CodeQL Analysis** | Push, PR, Weekly | Security vulnerability scanning | `codeql-analysis.yml` |
| **Dependency Review** | PR | Review dependencies for vulnerabilities | `dependency-review.yml` |
| **Semgrep** | Push, PR | Static analysis security testing | `semgrep.yml` |

## Quality Workflows

| Workflow | Trigger | Purpose | File |
|----------|---------|---------|------|
| **Link Checker** | PR, Weekly | Validate markdown links | `link-checker.yml` |
| **Accessibility Testing** | PR | Check accessibility standards | `accessibility-testing.yml` |
| **Mutation Testing** | PR | Test quality of tests | `mutation-testing.yml` |
| **Code Coverage** | PR | Track test coverage | `code-coverage.yml` |

## Automation Workflows

| Workflow | Trigger | Purpose | File |
|----------|---------|---------|------|
| **Auto-Assign** | PR, Issue | Assign to appropriate reviewers | `auto-assign.yml` |
| **Auto-Labeler** | PR, Issue | Automatic labeling | `auto-labeler.yml` |
| **Welcome** | First PR/Issue | Welcome new contributors | `welcome.yml` |
| **Community Health** | Schedule | Manage stale issues/PRs | `community-health.yml` |

## AI Workflows

| Workflow | Trigger | Purpose | File |
|----------|---------|---------|------|
| **Claude Code Review** | PR Comment | AI-powered code review | `claude-code-review.yml` |
| **Gemini Workflow** | Manual | Gemini AI integration | `gemini_workflow.yml` |
| **Grok Workflow** | Manual | Grok AI integration | `grok_workflow.yml` |
| **OpenAI Workflow** | Manual | OpenAI integration | `openai_workflow.yml` |

## Metrics & Reporting

| Workflow | Trigger | Purpose | File |
|----------|---------|---------|------|
| **Repo Metrics** | Monthly | Repository analytics | `repo-metrics.yml` |
| **Commit Tracking** | Push | Track commit patterns | `commit-tracking.yml` |
| **Performance Benchmark** | PR | Performance testing | `performance-benchmark.yml` |

## Release & Deployment

| Workflow | Trigger | Purpose | File |
|----------|---------|---------|------|
| **Release** | Tag | Automated releases | `release.yml` |
| **CI Advanced** | PR | Comprehensive CI pipeline | `ci-advanced.yml` |
