# AI Assistant Guide

> **Guidelines and best practices for AI assistants working with the ivi374forivi organization's default GitHub configuration repository.**

**Last Updated**: 2025-11-16
**Version**: 1.0.0
**Repository**: `ivi374forivi/.github`

---

## Core Principles for AI Assistants

When working with this repository, AI assistants should:

1.  **Understand the Special Nature**
    *   This is an organization-level `.github` repository.
    *   Changes affect ALL repositories in the organization.
    *   Exercise extra caution with modifications.

2.  **Respect the AI Management Protocol**
    *   Follow the 8-module framework in `for-ai-implementation.txt`.
    *   Understand module responsibilities.
    *   Coordinate actions across modules.

3.  **Maintain Documentation Excellence**
    *   This is a documentation-heavy repository.
    *   Keep all documentation accurate and up-to-date.
    *   Follow the [Documentation Style Guide](STYLE_GUIDE.md).
    *   Ensure links are valid (link-checker runs on PRs).

4.  **Follow Git Workflow Strictly**
    *   Use conventional commits (see [Semantic Versioning Guide](SEMANTIC_VERSIONING.md)).
    *   Create appropriate branch types (see [Git Workflow Guide](GIT_WORKFLOW.md)).
    *   Write comprehensive PR descriptions.
    *   Reference related issues.

5.  **Preserve Automation**
    *   Don't break existing workflows.
    *   Test workflow changes carefully.
    *   Understand workflow dependencies.
    *   Document workflow modifications.

## What AI Assistants Should Do

✅ **Always**:
- Read `for-ai-implementation.txt` to understand your module responsibilities.
- Check `CODEOWNERS` before modifying files.
- Follow conventional commit format.
- Update `CHANGELOG.md` for significant changes.
- Run link checker after updating documentation.
- Verify YAML syntax in workflow files.
- Test workflow changes in a safe environment.
- Update relevant documentation when changing functionality.
- Reference GitHub issues in commits and PRs.
- Use appropriate PR templates.

✅ **When Creating/Modifying**:
- **Workflows**: Test thoroughly, document triggers and permissions.
- **Templates**: Ensure they work across different scenarios.
- **Documentation**: Check for broken links, spelling, formatting.
- **Copilot customizations**: Follow naming conventions, add documentation.
- **Security configs**: Understand implications, test carefully.

## What AI Assistants Should Not Do

❌ **Never**:
- Commit directly to `main` or `develop`.
- Modify workflows without understanding their purpose.
- Break existing automation.
- Remove security checks without justification.
- Ignore `CODEOWNERS` requirements.
- Use generic commit messages.
- Create PRs without descriptions.
- Modify multiple unrelated things in one PR.
- Delete documentation without replacement.
- Change configuration files without testing.

❌ **Avoid**:
- Large, monolithic PRs (break into smaller, focused PRs).
- Mixing feature changes with refactoring.
- Adding dependencies without documentation.
- Creating new workflows that duplicate existing ones.
- Using deprecated GitHub Actions.
- Hardcoding secrets or credentials.

## AI Decision-Making Framework

When uncertain about a change, ask:

1.  **Impact**: Does this affect the entire organization?
2.  **Reversibility**: Can this be easily reverted if it causes issues?
3.  **Testing**: Can this be tested before merging?
4.  **Documentation**: Is the change documented?
5.  **Dependencies**: What else depends on this?
6.  **Security**: Does this introduce security risks?

If any answer raises concerns, consult with human maintainers.
