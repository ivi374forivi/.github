# CLAUDE.md - AI Assistant Guide for ivi374forivi/.github Repository

> **Comprehensive guide for AI assistants working with the ivi374forivi organization's default GitHub configuration repository**

**Last Updated**: 2025-11-16
**Version**: 1.0.0
**Repository**: `ivi374forivi/.github`

---

## Table of Contents

- [Repository Overview](#repository-overview)
- [Repository Purpose & Architecture](#repository-purpose--architecture)
- [Codebase Structure](#codebase-structure)
- [Development Workflows](#development-workflows)
- [AI Assistant Guidelines](#ai-assistant-guidelines)
- [GitHub Copilot Integration](#github-copilot-integration)
- [Automation & Workflows](#automation--workflows)
- [Security & Compliance](#security--compliance)
- [Documentation Standards](#documentation-standards)
- [Best Practices for AI Assistants](#best-practices-for-ai-assistants)
- [Key Files Reference](#key-files-reference)
- [AI Management Protocol](#ai-management-protocol)

---

## Repository Overview

### What is This Repository?

This is the **special `.github` repository** for the `ivi374forivi` organization. It serves as the central hub for organization-wide:

- **Default community health files** (CODE_OF_CONDUCT, CONTRIBUTING, SECURITY, etc.)
- **Standardized templates** for issues and pull requests
- **Reusable workflow templates** for CI/CD and automation
- **GitHub Copilot customizations** (agents, instructions, prompts, chat modes)
- **Living Document System** - AI-driven governance and management protocols
- **Organization-wide configuration** and documentation standards

When a repository in the organization doesn't have its own community health file, GitHub automatically uses the defaults from this repository.

### Key Characteristics

- **Type**: Organization default configuration repository
- **Visibility**: Public
- **Primary Language**: Markdown (documentation-heavy)
- **Key Technologies**: GitHub Actions, YAML, Markdown, JSON
- **AI Integration**: Extensive (Claude, GitHub Copilot, multiple AI workflows)
- **Management Model**: AI-driven with 8 core operational modules

---

## Repository Purpose & Architecture

### Core Functions

1. **Organization Defaults Provider**
   - Provides default community health files for all repositories
   - Supplies issue and PR templates
   - Offers reusable workflow templates

2. **GitHub Copilot Enhancement Hub**
   - Custom agents for specialized AI assistance
   - Language/framework-specific instructions
   - Task-specific prompts
   - Role-based chat modes
   - Curated collections

3. **AI Management Center**
   - Implements 8-module AI GitHub management protocol
   - Automated governance and compliance
   - Security and quality automation
   - Strategic analysis and risk mitigation

4. **Documentation Central**
   - Comprehensive guides and best practices
   - Organization standards and conventions
   - Developer onboarding resources

### The 8 AI Management Modules

As defined in `for-ai-implementation.txt`, this repository implements:

1. **[AI-GH-01] Organization & Repository Administration**
   - Organization profile management
   - Access control and RBAC
   - Repository provisioning
   - Branch protection enforcement
   - Billing and audit monitoring

2. **[AI-GH-02] Project Management & Workflow Automation**
   - Project board management
   - Workflow automation rules
   - Issue/PR template maintenance
   - Label and milestone management
   - Community engagement

3. **[AI-GH-03] CI/CD & Development Lifecycle**
   - Workflow configuration
   - Pipeline integration
   - Test orchestration
   - Deployment strategy
   - Secrets management

4. **[AI-GH-04] Security & Compliance Operations**
   - Vulnerability management (Dependabot, CodeQL)
   - Code scanning
   - Access and authentication audits
   - Data protection
   - Compliance reporting

5. **[AI-GH-05] Documentation & Knowledge Base Management**
   - Contribution guidelines maintenance
   - Project documentation management
   - GitHub Pages management
   - Wiki organization
   - Code review assistance

6. **[AI-GH-06] Ecosystem Integration & Architecture Monitoring**
   - Dynamic ecosystem mapping
   - Dependency hierarchy tracking
   - API contract auditing
   - Interoperability testing
   - External integrations management

7. **[AI-GH-07] Observability & System Health**
   - Repository analytics
   - Stale asset management
   - Centralized observability
   - Alerting configuration

8. **[AI-GH-08] Strategic Analysis & Risk Mitigation**
   - Blind spot identification
   - Shatter point analysis
   - Scalability and performance audits
   - Automated threat modeling

---

## Codebase Structure

### Root Directory Layout

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
├── CLAUDE.md                         # This file
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

### Key Directory Purposes

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

---

## Development Workflows

### Git Workflow

This repository follows a **modified Git Flow** strategy as documented in `GIT_WORKFLOW.md`:

#### Branch Types

1. **Main Branch** (`main`)
   - Production-ready code
   - Highest protection level
   - No direct commits
   - Requires PR approval
   - All checks must pass
   - Signed commits required

2. **Develop Branch** (`develop`)
   - Integration branch
   - High protection level
   - Auto-deploys to staging
   - Merges from feature branches

3. **Feature Branches** (`feature/*`)
   - Format: `feature/short-description` or `feature/TICKET-123-description`
   - Base: `develop`
   - Merge to: `develop`
   - Delete after merging

4. **Release Branches** (`release/*`)
   - Format: `release/v1.2.0`
   - Base: `develop`
   - Merge to: Both `main` and `develop`
   - For version bumping, final testing, bug fixes

5. **Hotfix Branches** (`hotfix/*`)
   - Format: `hotfix/critical-fix-description`
   - Base: `main`
   - Merge to: Both `main` and `develop`
   - Highest priority

6. **Bugfix Branches** (`bugfix/*`)
   - Format: `bugfix/fix-login-error`
   - Base: `develop`
   - Merge to: `develop`

#### AI-Specific Branch Naming

For Claude Code sessions, branches follow the pattern:
```
claude/claude-md-<session-id>-<unique-id>
```

**CRITICAL**: When pushing, always use:
```bash
git push -u origin <branch-name>
```

Branches MUST start with `claude/` and end with matching session ID, or push will fail with 403.

### Commit Convention

**Format**: [Conventional Commits](https://www.conventionalcommits.org/)

```
<type>(<scope>): <subject>

[optional body]

[optional footer]
```

#### Commit Types

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style (formatting, semicolons, etc.)
- `refactor`: Code refactoring
- `perf`: Performance improvements
- `test`: Adding/updating tests
- `build`: Build system changes
- `ci`: CI/CD changes
- `chore`: Maintenance tasks

#### Examples

```bash
# Simple feature
feat: add user authentication

# Feature with scope
feat(copilot): add new TypeScript expert agent

# Bug fix with issue reference
fix(workflows): resolve codeql timeout issue

Closes #123

# Documentation update
docs: update AI assistant guidelines in CLAUDE.md

# Breaking change
feat(templates)!: restructure PR template format

BREAKING CHANGE: PR templates now use YAML schema.
Update all repository references.
```

#### Commit Message Guidelines

1. **Subject line**:
   - Max 50 characters
   - Imperative mood ("add" not "added")
   - No period at end
   - Capitalize first letter

2. **Body** (optional):
   - Wrap at 72 characters
   - Explain what and why, not how
   - Separate from subject with blank line

3. **Footer** (optional):
   - Reference issues: `Closes #123`, `Fixes #456`
   - Breaking changes: `BREAKING CHANGE: description`

### Pull Request Workflow

#### Creating a PR

1. **Title**: Follow conventional commit format
   ```
   feat: add new security workflow
   fix(docs): correct broken links in README
   ```

2. **Description**: Use appropriate template
   - Select template: `?template=<name>.md`
   - Available: `bug_fix`, `feature`, `documentation`, `refactoring`, `performance`

3. **Required Sections**:
   - Description of changes
   - Type of change checklist
   - Testing checklist
   - Related issues

#### Code Review Process

1. **Automated Checks** (must pass):
   - Linting
   - Tests
   - Security scans (CodeQL, Semgrep)
   - Link checking
   - Spell checking

2. **Peer Review**:
   - At least 1 approval required (see CODEOWNERS)
   - Review code quality
   - Verify documentation updates
   - Check for security issues

3. **Merge**:
   - All checks passed
   - Approvals received
   - No merge conflicts
   - Branch up to date

### Versioning

Follows [Semantic Versioning](https://semver.org/):

```
MAJOR.MINOR.PATCH

Example: 1.2.3
```

- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes (backward compatible)

Pre-release versions:
```
1.2.3-alpha.1
1.2.3-beta.2
1.2.3-rc.1
```

---

## AI Assistant Guidelines

### Core Principles for AI Assistants

When working with this repository, AI assistants should:

1. **Understand the Special Nature**
   - This is an organization-level `.github` repository
   - Changes affect ALL repositories in the organization
   - Exercise extra caution with modifications

2. **Respect the AI Management Protocol**
   - Follow the 8-module framework in `for-ai-implementation.txt`
   - Understand module responsibilities
   - Coordinate actions across modules

3. **Maintain Documentation Excellence**
   - This is a documentation-heavy repository
   - Keep all documentation accurate and up-to-date
   - Follow markdown best practices
   - Ensure links are valid (link-checker runs on PRs)

4. **Follow Git Workflow Strictly**
   - Use conventional commits
   - Create appropriate branch types
   - Write comprehensive PR descriptions
   - Reference related issues

5. **Preserve Automation**
   - Don't break existing workflows
   - Test workflow changes carefully
   - Understand workflow dependencies
   - Document workflow modifications

### What AI Assistants Should Do

✅ **Always**:
- Read `for-ai-implementation.txt` to understand your module responsibilities
- Check CODEOWNERS before modifying files
- Follow conventional commit format
- Update CHANGELOG.md for significant changes
- Run link checker after updating documentation
- Verify YAML syntax in workflow files
- Test workflow changes in a safe environment
- Update relevant documentation when changing functionality
- Reference GitHub issues in commits and PRs
- Use appropriate PR templates

✅ **When Creating/Modifying**:
- **Workflows**: Test thoroughly, document triggers and permissions
- **Templates**: Ensure they work across different scenarios
- **Documentation**: Check for broken links, spelling, formatting
- **Copilot customizations**: Follow naming conventions, add documentation
- **Security configs**: Understand implications, test carefully

### What AI Assistants Should Not Do

❌ **Never**:
- Commit directly to `main` or `develop`
- Modify workflows without understanding their purpose
- Break existing automation
- Remove security checks without justification
- Ignore CODEOWNERS requirements
- Use generic commit messages
- Create PRs without descriptions
- Modify multiple unrelated things in one PR
- Delete documentation without replacement
- Change configuration files without testing

❌ **Avoid**:
- Large, monolithic PRs (break into smaller, focused PRs)
- Mixing feature changes with refactoring
- Adding dependencies without documentation
- Creating new workflows that duplicate existing ones
- Using deprecated GitHub Actions
- Hardcoding secrets or credentials

### AI Decision-Making Framework

When uncertain about a change, ask:

1. **Impact**: Does this affect the entire organization?
2. **Reversibility**: Can this be easily reverted if it causes issues?
3. **Testing**: Can this be tested before merging?
4. **Documentation**: Is the change documented?
5. **Dependencies**: What else depends on this?
6. **Security**: Does this introduce security risks?

If any answer raises concerns, consult with human maintainers.

---

## GitHub Copilot Integration

This repository contains extensive GitHub Copilot customizations from [github/awesome-copilot](https://github.com/github/awesome-copilot).

### Components

#### 1. Custom Agents (`agents/`)

**Location**: `agents/` directory (12+ agents)

**Purpose**: Specialized GitHub Copilot agents that integrate with MCP servers

**Examples**:
- `CSharpExpert.agent.md` - C# development expertise
- `WinFormsExpert.agent.md` - Windows Forms development
- `adr-generator.agent.md` - Architecture Decision Records
- `dynatrace-expert.agent.md` - Dynatrace monitoring
- `launchdarkly-flag-cleanup.agent.md` - Feature flag management
- `neon-migration-specialist.agent.md` - Neon database migrations

**Documentation**: See `docs/README.agents.md`

#### 2. Instructions (`instructions/`)

**Location**: `instructions/` directory (100+ files)

**Purpose**: Comprehensive coding standards that auto-apply based on file patterns

**Coverage**:
- **Frameworks**: Angular, React, Vue, Astro, Blazor, ASP.NET
- **Languages**: Python, JavaScript/TypeScript, C#, Go, Rust, Clojure
- **Cloud**: Azure, AWS (DevOps, Functions, Logic Apps, Terraform)
- **Tools**: Ansible, Docker, Kubernetes, CMake
- **Practices**: Accessibility, AI safety, security best practices

**How They Work**:
- Match file patterns (e.g., `*.tf` triggers Terraform instructions)
- Automatically applied by Copilot when editing matching files
- Provide language/framework-specific best practices

**Documentation**: See `docs/README.instructions.md` (comprehensive 104KB guide)

**Example Instruction Files**:
```
angular.instructions.md                    # Angular best practices
azure-devops-pipelines.instructions.md     # Azure DevOps CI/CD
bicep-code-best-practices.instructions.md  # Azure Bicep IaC
python-best-practices.instructions.md      # Python standards
react-best-practices.instructions.md       # React patterns
terraform-best-practices.instructions.md   # Terraform IaC
```

#### 3. Prompts (`prompts/`)

**Location**: `prompts/` directory (80+ files)

**Purpose**: Task-specific prompts for code generation and problem-solving

**Access**: Via `/` commands in GitHub Copilot Chat

**Categories**:
- Architecture & Design
- Code Generation
- Testing & Quality
- Documentation
- Cloud/Infrastructure
- Refactoring & Optimization

**Documentation**: See `docs/README.prompts.md` (comprehensive 110KB guide)

**Example Prompts**:
```
/architecture-blueprint-generator          # Generate architecture docs
/az-cost-optimize                         # Azure cost optimization
/breakdown-epic-arch                      # Break down epics
/code-exemplars-blueprint-generator       # Generate code examples
/containerize-aspnetcore                  # Containerize .NET apps
```

**Usage Example**:
```
# In Copilot Chat
/architecture-blueprint-generator

# Copilot will:
1. Analyze current architecture
2. Generate comprehensive blueprint
3. Create diagrams and documentation
4. Suggest improvements
```

#### 4. Chat Modes (`chatmodes/`)

**Location**: `chatmodes/` directory

**Purpose**: Specialized AI personas for different roles

**Examples**:
- Architect Mode - System design and architecture
- DBA Mode - Database optimization and design
- Security Expert Mode - Security analysis and hardening
- DevOps Mode - CI/CD and infrastructure

**Documentation**: See `docs/README.chatmodes.md`

#### 5. Collections (`collections/`)

**Location**: `collections/` directory

**Purpose**: Curated collections organized by theme

**Themes**:
- Azure Cloud Development
- Frontend Web Development
- Security Best Practices
- Backend API Development

**Documentation**: See `docs/README.collections.md`

### Using Copilot Customizations

#### For AI Assistants

When working with code in repositories:

1. **Instructions Auto-Apply**: Copilot automatically applies relevant instructions based on file extensions
2. **Use Prompts**: Reference prompts in `prompts/` for common tasks
3. **Activate Agents**: Use specialized agents for complex domain-specific work
4. **Switch Modes**: Activate chat modes for role-specific assistance

#### Adding New Customizations

When adding new Copilot customizations:

1. **Follow Naming Conventions**:
   - Agents: `name.agent.md`
   - Instructions: `framework.instructions.md`
   - Prompts: `task-name.prompt.md`
   - Chat modes: `role-mode.chatmode.md`

2. **Document Thoroughly**:
   - Add description in front matter
   - Include usage examples
   - Document any MCP server requirements
   - Update relevant README in `docs/`

3. **Test Before Committing**:
   - Verify syntax
   - Test with Copilot
   - Ensure no conflicts with existing customizations

---

## Automation & Workflows

### GitHub Actions Workflows

This repository contains 30+ GitHub Actions workflows for comprehensive automation.

#### Security Workflows

| Workflow | Trigger | Purpose | File |
|----------|---------|---------|------|
| **CodeQL Analysis** | Push, PR, Weekly | Security vulnerability scanning | `codeql-analysis.yml` |
| **Dependency Review** | PR | Review dependencies for vulnerabilities | `dependency-review.yml` |
| **Semgrep** | Push, PR | Static analysis security testing | `semgrep.yml` |

#### Quality Workflows

| Workflow | Trigger | Purpose | File |
|----------|---------|---------|------|
| **Link Checker** | PR, Weekly | Validate markdown links | `link-checker.yml` |
| **Accessibility Testing** | PR | Check accessibility standards | `accessibility-testing.yml` |
| **Mutation Testing** | PR | Test quality of tests | `mutation-testing.yml` |
| **Code Coverage** | PR | Track test coverage | `code-coverage.yml` |

#### Automation Workflows

| Workflow | Trigger | Purpose | File |
|----------|---------|---------|------|
| **Auto-Assign** | PR, Issue | Assign to appropriate reviewers | `auto-assign.yml` |
| **Auto-Labeler** | PR, Issue | Automatic labeling | `auto-labeler.yml` |
| **Welcome** | First PR/Issue | Welcome new contributors | `welcome.yml` |
| **Community Health** | Schedule | Manage stale issues/PRs | `community-health.yml` |

#### AI Workflows

| Workflow | Trigger | Purpose | File |
|----------|---------|---------|------|
| **Claude Code Review** | PR Comment | AI-powered code review | `claude-code-review.yml` |
| **Gemini Workflow** | Manual | Gemini AI integration | `gemini_workflow.yml` |
| **Grok Workflow** | Manual | Grok AI integration | `grok_workflow.yml` |
| **OpenAI Workflow** | Manual | OpenAI integration | `openai_workflow.yml` |

#### Metrics & Reporting

| Workflow | Trigger | Purpose | File |
|----------|---------|---------|------|
| **Repo Metrics** | Monthly | Repository analytics | `repo-metrics.yml` |
| **Commit Tracking** | Push | Track commit patterns | `commit-tracking.yml` |
| **Performance Benchmark** | PR | Performance testing | `performance-benchmark.yml` |

#### Release & Deployment

| Workflow | Trigger | Purpose | File |
|----------|---------|---------|------|
| **Release** | Tag | Automated releases | `release.yml` |
| **CI Advanced** | PR | Comprehensive CI pipeline | `ci-advanced.yml` |

### Key Workflow Concepts

#### Workflow Structure

```yaml
name: Workflow Name
on:
  push:
    branches: [main, develop]
  pull_request:
  schedule:
    - cron: '0 0 * * 0'  # Weekly

jobs:
  job-name:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pull-requests: write
    steps:
      - uses: actions/checkout@v4
      - name: Step name
        run: echo "Commands"
```

#### Important Permissions

Workflows use **least privilege** principle:

```yaml
permissions:
  contents: read          # Read repository contents
  pull-requests: write    # Comment on PRs
  issues: write          # Manage issues
  security-events: write # Upload security results
```

#### Secrets and Variables

- **Secrets**: Stored in GitHub Secrets (encrypted)
- **Variables**: Organization/repository variables
- **Access**: `${{ secrets.SECRET_NAME }}`

### Modifying Workflows

#### Before Modifying

1. **Understand Current Behavior**:
   - Read the workflow file
   - Check recent runs
   - Review any linked documentation

2. **Plan Changes**:
   - What's the goal?
   - What's the impact?
   - Can it be tested?

3. **Test Safely**:
   - Use `workflow_dispatch` for manual testing
   - Test on feature branch first
   - Monitor workflow runs

#### After Modifying

1. **Document Changes**:
   - Update comments in workflow file
   - Update relevant documentation
   - Add CHANGELOG entry if significant

2. **Monitor**:
   - Watch first few runs
   - Check for errors
   - Verify expected behavior

---

## Security & Compliance

### Security Layers

This repository implements **defense in depth** with multiple security layers:

#### Layer 1: Code Scanning

- **CodeQL**: Semantic code analysis for vulnerabilities
- **Semgrep**: Pattern-based security scanning
- **Bandit**: Python security linting (`.bandit` config)

#### Layer 2: Dependency Security

- **Dependabot**: Automated dependency updates (`dependabot.yml`)
- **Renovate**: Advanced dependency management (`renovate.json`)
- **Dependency Review**: PR-based dependency analysis

#### Layer 3: Access Control

- **CODEOWNERS**: Required reviewers for sensitive files
- **Branch Protection**: Enforced on `main` and `develop`
- **Required Reviews**: Minimum 1 approval
- **Status Checks**: All checks must pass

#### Layer 4: Secrets Management

- **No Secrets in Code**: Enforced by scanning
- **GitHub Secrets**: For workflow credentials
- **Secret Scanning**: Detect exposed secrets (if enabled)

### Security Best Practices for AI

✅ **Do**:
- Review all dependencies before adding
- Use specific versions, not `latest`
- Check licenses for compliance
- Scan for vulnerabilities before merging
- Follow principle of least privilege
- Document security decisions

❌ **Don't**:
- Commit secrets or credentials
- Disable security checks without justification
- Use deprecated or vulnerable dependencies
- Bypass code review requirements
- Grant excessive permissions to workflows
- Ignore security alerts

### Compliance Requirements

#### License Compliance

- **Allowed Licenses**: MIT, Apache-2.0, BSD-2-Clause, BSD-3-Clause, ISC
- **Denied Licenses**: GPL-3.0, AGPL-3.0 (copyleft)
- **Verification**: Automated in dependency-review workflow

#### Audit Trail

- All changes tracked in Git history
- Workflow runs logged
- Security alerts tracked
- Dependency changes audited

---

## Documentation Standards

### Markdown Style Guide

#### File Structure

```markdown
# Title (H1 - only one per file)

> Brief description or tagline

**Metadata** (if applicable):
- Last Updated: YYYY-MM-DD
- Version: X.Y.Z
- Related: [Links]

---

## Table of Contents (for long docs)

- [Section 1](#section-1)
- [Section 2](#section-2)

---

## Section 1 (H2)

Content...

### Subsection (H3)

Content...

---

## Resources

---

**Last Updated**: YYYY-MM-DD
```

#### Formatting Conventions

**Headers**:
- H1: Document title only
- H2: Major sections
- H3: Subsections
- H4+: Nested subsections (use sparingly)

**Lists**:
```markdown
- Unordered list
- With dash `-`

1. Ordered list
2. With numbers

* Alternative unordered
* With asterisk `*`
```

**Code Blocks**:
````markdown
```language
code here
```
````

**Links**:
```markdown
[Link text](url)
[Reference link][ref]

[ref]: url
```

**Tables**:
```markdown
| Header 1 | Header 2 |
|----------|----------|
| Cell 1   | Cell 2   |
```

**Emphasis**:
```markdown
**Bold**
*Italic*
***Bold Italic***
`Code`
```

**Admonitions**:
```markdown
> Note: Information
> Warning: Caution
> Important: Critical info
```

**Checkboxes**:
```markdown
- [x] Completed
- [ ] Pending
```

### Documentation Types

#### 1. Guide Documents

Format: Comprehensive guides with TOC
Examples: `BEST_PRACTICES.md`, `GIT_WORKFLOW.md`, `AI_CODE_INTELLIGENCE.md`

Structure:
```markdown
# Title

> Description

## Table of Contents

## Overview

## Main Content Sections

## Resources

## Support

---

**Last Updated**: Date
```

#### 2. Reference Documents

Format: Quick reference with tables
Examples: `CODEOWNERS`, `dependabot.yml`

Structure:
- Concise
- Well-commented
- Examples provided

#### 3. Templates

Format: Structured with placeholders
Examples: Issue templates, PR templates

Structure:
- Clear sections
- Required/optional fields marked
- Examples or hints

#### 4. README Files

Format: Overview and navigation
Examples: `README.md`, `docs/README.agents.md`

Structure:
```markdown
# Repository/Section Name

## About

## Contents

## Getting Started

## Documentation

## Resources
```

### Link Management

#### Internal Links

```markdown
# Absolute path from repo root
[Link](docs/CONTRIBUTING.md)

# Relative path
[Link](../SECURITY.md)

# Anchor link
[Link](#section-name)
```

#### External Links

```markdown
# Always use HTTPS
[GitHub](https://github.com)

# Include protocol
[Example](https://example.com)
```

#### Link Validation

- Link checker runs on PRs
- Weekly scheduled check
- Configuration: `.github/markdown-link-check-config.json`

### Documentation Maintenance

#### When to Update

- When functionality changes
- When workflows are added/modified
- When dependencies change
- When new features are added
- When issues are identified

#### What to Update

- Relevant markdown files
- CHANGELOG.md
- Version numbers
- Last Updated dates
- Links and references

#### How to Update

1. Make changes in feature branch
2. Run link checker locally if possible
3. Check spelling
4. Verify formatting
5. Update Last Updated date
6. Create PR with `docs:` commit type

---

## Best Practices for AI Assistants

### Code Generation

#### When Generating Workflows

```yaml
# ✅ Good: Specific, documented, secure
name: Descriptive Name
on:
  push:
    branches: [main]
  pull_request:

permissions:  # Explicit permissions
  contents: read
  pull-requests: write

jobs:
  job-name:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4  # Pinned version
      - name: Clear step name
        run: |
          # Commented command
          echo "What this does"
```

```yaml
# ❌ Bad: Vague, undocumented, excessive permissions
name: Workflow
on: [push]

permissions: write-all  # Too broad!

jobs:
  job:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2  # Outdated
      - run: do-things  # What things?
```

#### When Generating Documentation

```markdown
✅ Good:
# Clear Title

> Helpful description

## Table of Contents (for >3 sections)

## Well-Organized Sections

Examples with code blocks

### Subsections with Context

**Last Updated**: 2025-11-16
```

```markdown
❌ Bad:
# title

stuff

more stuff
```

#### When Generating Templates

```markdown
✅ Good:
## Description
<!-- Provide a clear description of the changes -->

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change

## Checklist
- [ ] Tests added/updated
- [ ] Documentation updated
```

```markdown
❌ Bad:
Describe your PR

- [ ] Done testing
```

### Code Review

#### What to Look For

When reviewing code or being asked to review:

1. **Security**:
   - No hardcoded secrets
   - No SQL injection vectors
   - No XSS vulnerabilities
   - Proper input validation
   - Secure dependencies

2. **Quality**:
   - Follows conventions
   - Properly documented
   - Tests included
   - Error handling
   - Edge cases considered

3. **Maintainability**:
   - Clear, readable code
   - Appropriate comments
   - Consistent style
   - Logical organization
   - No unnecessary complexity

4. **Functionality**:
   - Solves stated problem
   - No unintended side effects
   - Handles errors gracefully
   - Performance acceptable
   - Accessibility considered

#### Review Comments Format

```markdown
✅ Good:
**Security**: This workflow needs explicit permissions. Consider:
```yaml
permissions:
  contents: read
  pull-requests: write
```
This follows principle of least privilege.

Reference: [GitHub Actions security](https://docs.github.com/en/actions/security-guides)
```

```markdown
❌ Bad:
needs permissions
```

### Problem Solving

#### Approach

1. **Understand the Problem**:
   - What's the actual issue?
   - What's the desired outcome?
   - What's the context?

2. **Research**:
   - Check existing documentation
   - Review similar implementations
   - Consider constraints and requirements

3. **Plan**:
   - Outline approach
   - Identify dependencies
   - Consider edge cases

4. **Implement**:
   - Follow conventions
   - Document as you go
   - Test thoroughly

5. **Verify**:
   - Does it solve the problem?
   - Are there side effects?
   - Is it maintainable?

#### Common Scenarios

**Scenario**: Add new workflow

1. Check if similar workflow exists
2. Review workflow best practices
3. Use appropriate template
4. Add required permissions
5. Document purpose and triggers
6. Test with `workflow_dispatch`
7. Create PR with clear description

**Scenario**: Update documentation

1. Identify affected files
2. Check for related documentation
3. Update all relevant files
4. Verify links still work
5. Check spelling
6. Update "Last Updated" date
7. Create PR with `docs:` type

**Scenario**: Fix security issue

1. Understand the vulnerability
2. Research secure alternatives
3. Implement fix
4. Add tests if applicable
5. Document the change
6. Reference security advisory
7. Create PR with `fix(security):` type

---

## Key Files Reference

### Critical Files (Never Delete)

| File | Purpose | AI Module | Notes |
|------|---------|-----------|-------|
| `for-ai-implementation.txt` | AI management protocol | ALL | Defines 8-module system |
| `README.md` | Repository overview | AI-GH-05 | Main documentation |
| `CODEOWNERS` | Code ownership | AI-GH-01 | Review assignments |
| `LICENSE` | MIT License | AI-GH-04 | Legal requirement |
| `SECURITY.md` | Security policy | AI-GH-04 | Vulnerability reporting |

### Configuration Files

| File | Purpose | AI Module | Modify With Caution |
|------|---------|-----------|---------------------|
| `dependabot.yml` | Dependency automation | AI-GH-04 | ⚠️ Yes |
| `renovate.json` | Dependency management | AI-GH-04 | ⚠️ Yes |
| `.gitattributes` | Git attributes | AI-GH-01 | ⚠️ Yes |
| `.gitignore` | Ignore patterns | AI-GH-01 | ✅ Carefully |
| `.releaserc.json` | Semantic release | AI-GH-03 | ⚠️ Yes |
| `.pre-commit-config.yaml` | Pre-commit hooks | AI-GH-03 | ⚠️ Yes |

### Documentation Files

| File | Purpose | AI Module | Update Frequency |
|------|---------|-----------|------------------|
| `CHANGELOG.md` | Version history | AI-GH-05 | Every release |
| `CONTRIBUTING.md` | Contribution guide | AI-GH-05 | Quarterly |
| `CODE_OF_CONDUCT.md` | Community standards | AI-GH-05 | Rarely |
| `BEST_PRACTICES.md` | Best practices guide | AI-GH-05 | Monthly |
| `GIT_WORKFLOW.md` | Git workflow guide | AI-GH-05 | Quarterly |
| `AI_CODE_INTELLIGENCE.md` | AI tools guide | AI-GH-05 | Monthly |

### Workflow Files

Located in `.github/workflows/`, see [Automation & Workflows](#automation--workflows) section.

### Template Files

Located in `ISSUE_TEMPLATE/` and `PULL_REQUEST_TEMPLATE/`.

### Copilot Customization Files

Located in `agents/`, `instructions/`, `prompts/`, `chatmodes/`, `collections/`.
See [GitHub Copilot Integration](#github-copilot-integration) section.

---

## AI Management Protocol

### The 8-Module System

Detailed in `for-ai-implementation.txt`, this protocol defines AI responsibilities:

#### Module 1: Organization & Repository Administration [AI-GH-01]
- Organization profile maintenance
- Access control (RBAC)
- Repository provisioning with templates
- Branch protection enforcement
- Billing and audit monitoring

#### Module 2: Project Management & Workflow Automation [AI-GH-02]
- Project board management
- Workflow automation rules
- Issue/PR template maintenance
- Label and milestone management
- Community engagement facilitation

#### Module 3: CI/CD & Development Lifecycle [AI-GH-03]
- Workflow configuration (.github/workflows/)
- Pipeline integration (linters, security)
- Test orchestration
- Deployment strategies
- Secrets management

#### Module 4: Security & Compliance Operations [AI-GH-04]
- Vulnerability management (Dependabot alerts)
- Code scanning (CodeQL, Semgrep)
- Access and authentication audits
- Data protection (secrets scanning)
- Compliance reporting

#### Module 5: Documentation & Knowledge Base Management [AI-GH-05]
- Contribution guidelines (CONTRIBUTING.md, CODE_OF_CONDUCT.md)
- Project documentation (docs/)
- GitHub Pages management
- Wiki organization
- Code review assistance

#### Module 6: Ecosystem Integration & Architecture Monitoring [AI-GH-06]
- Dynamic ecosystem mapping
- Dependency hierarchy monitoring
- API contract auditing
- Interoperability testing
- External integrations (webhooks, Slack, etc.)

#### Module 7: Observability & System Health [AI-GH-07]
- Repository analytics (insights, metrics)
- Stale asset management
- Centralized observability (metrics, logs, traces)
- Alerting configuration

#### Module 8: Strategic Analysis & Risk Mitigation [AI-GH-08]
- Blind spot identification (unmonitored dependencies)
- Shatter point analysis (single points of failure)
- Scalability and performance audits
- Automated threat modeling

### AI Assistant Responsibilities

As an AI assistant working with this repository:

1. **Identify Your Module**: Determine which module(s) your task falls under
2. **Follow Protocol**: Reference `for-ai-implementation.txt` for module-specific guidelines
3. **Coordinate**: Understand how modules interact
4. **Document**: Record decisions and changes
5. **Monitor**: Track outcomes and adjust as needed

### Module Interaction Example

**Task**: Add a new security workflow

- **Module 3 (CI/CD)**: Create workflow file
- **Module 4 (Security)**: Configure security scanning
- **Module 5 (Documentation)**: Document the workflow
- **Module 7 (Observability)**: Set up monitoring/alerting

Each module has specific responsibilities, but they work together.

---

## Quick Reference

### Common Tasks

#### 1. Add New Workflow

```bash
# Create workflow file
touch .github/workflows/my-workflow.yml

# Edit with required structure
# Commit with conventional format
git add .github/workflows/my-workflow.yml
git commit -m "ci: add workflow for X"

# Create PR
git push -u origin feature/add-x-workflow
```

#### 2. Update Documentation

```bash
# Edit documentation
vim RELEVANT_FILE.md

# Update "Last Updated" date
# Verify links
# Check spelling

# Commit
git add RELEVANT_FILE.md
git commit -m "docs: update RELEVANT_FILE with new information"
```

#### 3. Add Copilot Customization

```bash
# Create file in appropriate directory
touch prompts/my-task.prompt.md

# Follow naming convention
# Add documentation
# Update docs/README.prompts.md

# Commit
git add prompts/my-task.prompt.md docs/README.prompts.md
git commit -m "feat(copilot): add my-task prompt"
```

#### 4. Fix Security Issue

```bash
# Create hotfix branch
git checkout -b hotfix/security-fix

# Make fix
# Test thoroughly
# Document in commit

git add .
git commit -m "fix(security): resolve XYZ vulnerability

Addresses security advisory ABC-123.
See: https://..."

# Push and create PR
git push -u origin hotfix/security-fix
```

### Emergency Contacts

**For Security Issues**:
- See `SECURITY.md`
- Email: ivi374forivi (GitHub user)

**For Repository Issues**:
- Open issue using appropriate template
- Tag `@ivi374forivi`

### Useful Links

- [Repository](https://github.com/ivi374forivi/.github)
- [Organization](https://github.com/ivi374forivi)
- [GitHub Docs](https://docs.github.com/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Semantic Versioning](https://semver.org/)

---

## Appendix

### Glossary

- **CODEOWNERS**: File defining code ownership for automatic review requests
- **MCP**: Model Context Protocol (for Copilot agents)
- **RBAC**: Role-Based Access Control
- **SBOM**: Software Bill of Materials
- **SAST**: Static Application Security Testing
- **SARIF**: Static Analysis Results Interchange Format
- **PR**: Pull Request
- **CI/CD**: Continuous Integration/Continuous Deployment

### Acronyms

- **AI-GH-01 through AI-GH-08**: AI GitHub Management Module IDs
- **YAML**: YAML Ain't Markup Language
- **JSON**: JavaScript Object Notation
- **MD**: Markdown
- **IaC**: Infrastructure as Code

### Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2025-11-16 | Initial comprehensive CLAUDE.md created |

---

## Contributing to This Document

This document should evolve with the repository. To update:

1. Create feature branch: `feature/update-claude-md`
2. Make changes
3. Ensure accuracy
4. Update "Last Updated" date
5. Update version if major changes
6. Create PR with `docs(claude-md):` commit type

---

**Maintained by**: [@ivi374forivi](https://github.com/ivi374forivi)

**Repository**: [ivi374forivi/.github](https://github.com/ivi374forivi/.github)

**License**: [MIT](LICENSE)

---

*This guide is specifically designed for AI assistants like Claude to understand and work effectively with the ivi374forivi organization's default .github repository. It should be read in conjunction with `for-ai-implementation.txt` and other repository documentation.*
