"""Roadmap template."""

TEMPLATE = """# Roadmap: [Project Name]

## Vision & Scope

- [High-level vision statement]
- [Core architectural principles]
- [In scope: key features and components]
- [Out of scope (for now): features deferred to future]

## Development Priority Principle (MANDATORY)

**CRITICAL**: Development priorities MUST follow this order:

1. **Fixes/Improvements First** - All known bugs, code quality issues, and improvements must be addressed before new feature development
2. **[Domain-Specific Priority]** - [Domain-specific work that should proceed after fixes/improvements]
3. **Advanced Features Last** - Advanced feature development should only begin after priorities 1 and 2 are complete

**Rationale**: [Explain why this priority order is important]

## Current Focus ([Date])

### Completed Foundation ✅

- [Major completed milestone 1]
- [Major completed milestone 2]
- [Major completed milestone 3]

### Current Work 🚧

- [Current work item 1]
  - [Sub-item or detail]
  - [Sub-item or detail]
- [Current work item 2]

## Near-Term Milestones

- ✅ ([Date]) [Milestone 1] - COMPLETED
- ✅ ([Date]) [Milestone 2] - COMPLETED
- 🚧 ([Date]) [Milestone 3] - IN PROGRESS
- 📋 ([Date]) [Milestone 4] - READY

## Component Roadmap

### [Component 1]

- [Component 1 roadmap item]
- [Component 1 roadmap item]

### [Component 2]

- [Component 2 roadmap item]
- [Component 2 roadmap item]

## Performance Goals

- [Performance goal 1]
- [Performance goal 2]

## History of Major Milestones (last 3 months, newest first)

- ([Date]) [Milestone description]
- ([Date]) [Milestone description]
- ([Date]) [Milestone description]

## Immediate Next Steps ([Date])

### Priority 0: Critical Issues & Performance Violations 📋

**Status**: [Status description]

#### Priority 0.1: [Issue Name] ⚠️

**Critical Issue**: [Issue description]

**Impact**: [Impact description]

**Plan**: [Plan reference or description]

**Timeline**: [Estimated timeline]

### Priority 1: [Priority 1 Work]

[Description of priority 1 work]

### Priority 2: [Priority 2 Work]

[Description of priority 2 work]

## Plan References

All detailed implementation plans are located in `.cursor/plans/`:

### Current Plans (Active)

- **[Plan Name]**: `[plan-file-name].plan.md` ([Description])

### Archived Plans

- [Completed plans are archived in `.cursor/plans/archive/`]

## Quality Gates

- [Quality gate 1]
- [Quality gate 2]
- [Quality gate 3]
"""

