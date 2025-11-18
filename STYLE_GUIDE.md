# Documentation Style Guide

> **Standards for creating and maintaining documentation in the ivi374forivi organization.**

**Last Updated**: 2025-11-16
**Version**: 1.0.0

---

## Markdown Style Guide

### File Structure

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

### Formatting Conventions

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

## Documentation Types

### 1. Guide Documents

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

### 2. Reference Documents

Format: Quick reference with tables
Examples: `CODEOWNERS`, `dependabot.yml`

Structure:
- Concise
- Well-commented
- Examples provided

### 3. Templates

Format: Structured with placeholders
Examples: Issue templates, PR templates

Structure:
- Clear sections
- Required/optional fields marked
- Examples or hints

### 4. README Files

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

## Link Management

### Internal Links

```markdown
# Absolute path from repo root
[Link](/docs/CONTRIBUTING.md)

# Relative path
[Link](../SECURITY.md)

# Anchor link
[Link](#section-name)
```

### External Links

```markdown
# Always use HTTPS
[GitHub](https://github.com)

# Include protocol
[Example](https://example.com)
```

### Link Validation

- Link checker runs on PRs
- Weekly scheduled check
- Configuration: `.github/markdown-link-check-config.json`

## Documentation Maintenance

### When to Update

- When functionality changes
- When workflows are added/modified
- When dependencies change
- When new features are added
- When issues are identified

### What to Update

- Relevant markdown files
- CHANGELOG.md
- Version numbers
- Last Updated dates
- Links and references

### How to Update

1. Make changes in feature branch
2. Run link checker locally if possible
3. Check spelling
4. Verify formatting
5. Update Last Updated date
6. Create PR with `docs:` commit type
