# .github

This is the special `.github` repository for the **ivi374forivi** organization. It provides default community health files and configurations that apply to all repositories in the organization.

## What's Inside

### Organization Profile

The `profile/README.md` file displays on the organization's public profile page, introducing visitors to the organization.

### Community Health Files

These files provide default templates for all repositories in the organization:

- **CODE_OF_CONDUCT.md** - Defines standards for community interaction
- **CONTRIBUTING.md** - Guidelines for contributing to projects
- **FUNDING.yml** - Funding and sponsorship configuration
- **GOVERNANCE.md** - Project governance and decision-making processes
- **LICENSE** - License terms for the organization's projects (MIT License)
- **MANIFESTO.md** - Core principles and values of the organization
- **SECURITY.md** - Security policy and vulnerability reporting process
- **SUPPORT.md** - How to get help and support

### Issue and Pull Request Templates

Comprehensive templates to encourage useful issues and pull requests:

#### Issue Templates

- **ISSUE_TEMPLATE/config.yml** - Configuration for issue templates and contact links
- **ISSUE_TEMPLATE/bug_report.md** - Classic markdown bug report template
- **ISSUE_TEMPLATE/bug_report_form.yml** - Modern form-based bug report with structured fields
- **ISSUE_TEMPLATE/feature_request.md** - Classic markdown feature request template
- **ISSUE_TEMPLATE/feature_request_form.yml** - Modern form-based feature request
- **ISSUE_TEMPLATE/documentation.md** - Template for documentation issues
- **ISSUE_TEMPLATE/question.md** - Template for asking questions

#### Pull Request Templates

- **PULL_REQUEST_TEMPLATE.md** - Default comprehensive PR template
- **PULL_REQUEST_TEMPLATE/bug_fix.md** - Specialized template for bug fixes
- **PULL_REQUEST_TEMPLATE/feature.md** - Specialized template for new features
- **PULL_REQUEST_TEMPLATE/documentation.md** - Specialized template for documentation changes
- **PULL_REQUEST_TEMPLATE/refactoring.md** - Specialized template for code refactoring
- **PULL_REQUEST_TEMPLATE/performance.md** - Specialized template for performance improvements

**Note**: Contributors can choose a specific PR template by adding `?template=<name>.md` to the PR URL, e.g., `?template=bug_fix.md`

### Workflow Templates

The `workflow-templates/` directory contains reusable GitHub Actions workflow templates that can be used across repositories.

## How It Works

When a repository in the organization doesn't have its own community health files, GitHub automatically uses the files from this `.github` repository as defaults.

## Customization

Individual repositories can override these defaults by creating their own versions of these files.

## Learn More

- [About default community health files](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file)
- [About organization profiles](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/customizing-your-organizations-profile)
- [Creating workflow templates](https://docs.github.com/en/actions/using-workflows/creating-starter-workflows-for-your-organization)

## Structure

```
.github/
├── profile/
│   └── README.md                           # Organization profile
├── ISSUE_TEMPLATE/
│   ├── config.yml                          # Issue template configuration
│   ├── bug_report.md                       # Bug report (markdown)
│   ├── bug_report_form.yml                 # Bug report (form)
│   ├── feature_request.md                  # Feature request (markdown)
│   ├── feature_request_form.yml            # Feature request (form)
│   ├── documentation.md                    # Documentation issue
│   └── question.md                         # Question template
├── PULL_REQUEST_TEMPLATE/
│   ├── bug_fix.md                          # Bug fix PR template
│   ├── feature.md                          # Feature PR template
│   ├── documentation.md                    # Documentation PR template
│   ├── refactoring.md                      # Refactoring PR template
│   └── performance.md                      # Performance PR template
├── workflow-templates/
│   ├── ci.yml                              # CI workflow template
│   └── ci.properties.json                  # Workflow template metadata
├── CODE_OF_CONDUCT.md                      # Code of conduct
├── CONTRIBUTING.md                         # Contributing guidelines
├── FUNDING.yml                             # Funding configuration
├── GOVERNANCE.md                           # Governance model
├── LICENSE                                 # License (MIT)
├── MANIFESTO.md                            # Organization manifesto
├── PULL_REQUEST_TEMPLATE.md                # Default PR template
├── SECURITY.md                             # Security policy
└── SUPPORT.md                              # Support information
```