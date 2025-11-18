# Codebase Structure

> **An overview of the file and directory structure of the `ivi374forivi/.github` repository.**
>
> *Note: This file is auto-generated and should not be edited manually. It will be updated periodically to reflect the current state of the repository.*

**Last Updated**: 2025-11-16
**Version**: 1.0.0

---

## Root Directory Layout

```
.github/
├── .github/                          # Repository's own GitHub configuration
│   ├── workflows/                    # GitHub Actions workflows (30+ files)
│   │   ├── accessibility-testing.yml
│   │   ├── auto-assign.yml
│   │   ├── auto-labeler.yml
│   │   ├── ci-advanced.yml
│   │   ├── claude-code-review.yml    # AI code review integration
│   │   ├── codeql-analysis.yml       # Security scanning
│   │   ├── commit-tracking.yml
│   │   ├── community-health.yml
│   │   ├── dependency-review.yml
│   │   ├── link-checker.yml
│   │   ├── mutation-testing.yml
│   │   ├── performance-benchmark.yml
│   │   ├── release.yml
│   │   ├── repo-metrics.yml
│   │   ├── semgrep.yml
│   │   ├── welcome.yml
│   │   └── [other workflows...]
│   ├── copilot-instructions.md       # Copilot code review instructions
│   ├── labeler.yml                   # Auto-labeling configuration
│   ├── markdown-link-check-config.json
│   ├── spellcheck-config.yml
│   └── subscriptions.json
│
├── .devcontainer/                    # Dev container configuration
├── .semgrep/                         # Semgrep security rules
├── .vscode/                          # VS Code workspace settings
│
├── agents/                           # GitHub Copilot custom agents (12+ files)
│   ├── CSharpExpert.agent.md
│   ├── WinFormsExpert.agent.md
│   ├── adr-generator.agent.md
│   ├── dynatrace-expert.agent.md
│   ├── launchdarkly-flag-cleanup.agent.md
│   ├── neon-migration-specialist.agent.md
│   └── [other agents...]
│
├── chatmodes/                        # GitHub Copilot chat modes (specialized personas)
│
├── collections/                      # Curated Copilot collections by theme
│
├── instructions/                     # Copilot coding instructions (100+ files)
│   ├── angular.instructions.md
│   ├── ansible.instructions.md
│   ├── aspnet-rest-apis.instructions.md
│   ├── azure-devops-pipelines.instructions.md
│   ├── bicep-code-best-practices.instructions.md
│   ├── python.instructions.md
│   ├── react.instructions.md
│   ├── terraform.instructions.md
│   └── [framework/language specific...]
│
├── prompts/                          # GitHub Copilot prompts (80+ files)
│   ├── architecture-blueprint-generator.prompt.md
│   ├── az-cost-optimize.prompt.md
│   ├── breakdown-epic-arch.prompt.md
│   ├── code-exemplars-blueprint-generator.prompt.md
│   └── [task-specific prompts...]
│
├── docs/                             # Organization documentation
│   ├── AI_IMPLEMENTATION_GUIDE.md
│   ├── BRANCH_PROTECTION.md
│   ├── CODE_OF_CONDUCT.md
│   ├── CONTRIBUTING.md
│   ├── GOVERNANCE.md
│   ├── LABELS.md
│   ├── MANIFESTO.md
│   ├── PULL_REQUEST_TEMPLATE.md
│   ├── README.agents.md              # Agents documentation
│   ├── README.chatmodes.md           # Chat modes documentation
│   ├── README.collections.md         # Collections documentation
│   ├── README.instructions.md        # Instructions documentation (detailed)
│   ├── README.prompts.md             # Prompts documentation (comprehensive)
│   ├── REPOSITORY_SETUP_CHECKLIST.md
│   ├── SECURITY.md
│   ├── SUPPORT.md
│   └── TESTING.md
│
├── ISSUE_TEMPLATE/                   # Issue templates
│   ├── bug_report.md                 # Classic markdown template
│   ├── bug_report_form.yml           # Modern form-based template
│   ├── config.yml                    # Template configuration
│   ├── documentation.md
│   ├── feature_request.md
│   ├── feature_request_form.yml
│   └── question.md
│
├── PULL_REQUEST_TEMPLATE/            # PR templates
│   ├── bug_fix.md
│   ├── documentation.md
│   ├── feature.md
│   ├── performance.md
│   └── refactoring.md
│
├── workflow-templates/               # Reusable workflow templates for org repos
│   ├── ci.yml
│   ├── ci.properties.json
│   ├── deployment.yml
│   ├── dependency-updates.yml
│   ├── security-scan.yml
│   ├── stale-management.yml
│   └── [templates + metadata...]
│
├── observability/                    # Observability configurations
│   └── prometheus-example.yml
│
├── profile/                          # Organization profile
│   └── README.md                     # Public org profile page
│
├── reports/                          # Generated reports
├── scripts/                          # Automation scripts
│
├── AI_CODE_INTELLIGENCE.md           # AI code intelligence guide
├── AUTOMATION_MASTER_GUIDE.md        # Automation comprehensive guide
├── BEST_PRACTICES.md                 # Gold standard best practices
├── CHANGELOG.md                      # Version history
├── CODEOWNERS                        # Code ownership rules
├── CONTRIBUTORS.md                   # Contributor recognition
├── DOCKER_BEST_PRACTICES.md          # Docker guide
├── FUNDING.yml                       # Funding configuration
├── GITHUB_APPS_INTEGRATIONS.md       # GitHub Apps guide
├── GIT_WORKFLOW.md                   # Git workflow and branching
├── LICENSE                           # MIT License
├── LOGICAL_EXPANSIONS.md             # Logical expansions guide
├── ORG_HEALTH_REPORT.md              # Organization health metrics
├── QUICK_START.md                    # Quick start guide
├── README.md                         # Main repository documentation
├── REPOSITORY_PURPOSE_ANALYSIS.md    # Analysis of repository purpose
├── SECURITY_ADVANCED.md              # Advanced security guide
├── SEMANTIC_VERSIONING.md            # Versioning guide
├── The Living Document System.pdf    # Living document system spec
│
├── .bandit                           # Bandit security config
├── .gitattributes                    # Git attributes
├── .gitignore                        # Git ignore patterns
├── .pre-commit-config.yaml           # Pre-commit hooks
├── .releaserc.json                   # Semantic release config
├── dependabot.yml                    # Dependabot configuration
├── for-ai-implementation.txt         # AI handoff protocol (CRITICAL)
├── renovate.json                     # Renovate config
└── setup.sh                          # Setup script
```

## Key Directory Purposes

| Directory | Purpose | File Count | Usage |
|-----------|---------|------------|-------|
| `.github/workflows/` | GitHub Actions automation | 30+ | CI/CD, security, quality, metrics |
| `agents/` | Copilot custom agents | 12+ | Specialized AI assistance with MCP servers |
| `instructions/` | Copilot coding standards | 100+ | Auto-apply based on file patterns |
| `prompts/` | Copilot task prompts | 80+ | Accessible via `/` commands |
| `chatmodes/` | Copilot specialized personas | 10+ | Role-based AI modes |
| `collections/` | Curated Copilot content | Multiple | Themed collections |
| `docs/` | Organization documentation | 20+ | Community health, guides, standards |
| `ISSUE_TEMPLATE/` | Issue templates | 7 | Bug reports, features, questions |
| `PULL_REQUEST_TEMPLATE/` | PR templates | 6 | Different PR types |
| `workflow-templates/` | Reusable workflows | 10+ | Org-wide CI/CD templates |
