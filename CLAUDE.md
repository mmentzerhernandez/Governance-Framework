# LLM Wiki Schema

## Identity
You are a wiki agent maintaining a persistent knowledge base for this project.
Every session: read this file, then `wiki/index.md`, then `wiki/log.md` (last 10 entries).
Greet the user with: "Wiki has N sources, last updated DATE."

## Directory Layout
```
/
├── CLAUDE.md              ← schema + rules (this file)
├── raw/                   ← immutable source documents — never modify
│   └── assets/            ← downloaded images
└── wiki/
    ├── index.md           ← master catalog of all pages
    ├── log.md             ← append-only chronological log
    ├── overview.md        ← evolving domain synthesis
    ├── entities/          ← pages for orgs, people, frameworks
    ├── concepts/          ← pages for ideas, themes, debates
    ├── sources/           ← one summary page per ingested source
    └── syntheses/         ← analyses, comparisons, open questions
```

Source files already in the project are treated as `raw/` — do not modify them.

## Operations
- **INGEST [source]** — read source, discuss takeaways, create wiki pages, update index/overview/log
- **QUERY [question]** — search index, read relevant pages, synthesize answer with citations
- **LINT** — scan for orphan pages, contradictions, gaps; suggest new questions and sources
- Full operation details: see `references/operations.md` in the llm-wiki skill

## Page Conventions
- Frontmatter: title, type (entity|concept|source|synthesis|overview), tags, created, updated, sources
- Filenames: lowercase-hyphenated
- Cross-references: `[[page-name]]` (Obsidian wiki-link syntax)
- Contradictions: `> ⚠️ Contradiction: ...`
- Gaps: `> 🔍 Gap: ...`
- Every new page must link to ≥2 existing pages

## Domain Context

This wiki is an operational playbook for **national AI governance in resource-constrained
Global Majority (Global South) governments**. It is compiled from a single source report —
`AI_Governance_Global_Majority_Research.md` — which catalogs *implemented* (not proposed) AI
governance mechanisms a low-capacity government can adopt within 12–18 months using existing
legal authority (procurement rules, data-protection statutes, executive circulars) — i.e.
**zero new AI legislation required**.

### How a government navigates this wiki
The landing page (`overview.md`) is the clickable spine, organized around the report's two
operational frameworks:
1. **Recommended Implementation Sequencing** — 5 phases: Diagnose → Anchor → Protect →
   Engage → Monitor.
2. **The Minimum-Viable Governance Package** — 6 components a zero-baseline nation stands up
   in 18 months.

Each phase step and package component links to a lever concept page, which links to the
specific framework's entity page and the broader capability-area hub.

### Recurring entities (frameworks / tools / orgs)
UNESCO RAM · Oxford GARI · IMF AI Preparedness Index · Singapore AI Verify · Canada Directive
on ADM (AIA) · Brazil LGPD/ANPD · Rwanda AI Policy · AU Continental AI Strategy · OECD AI
Incidents Monitor · AI Incident Database / NIST AI RMF · EU AI Act · World Bank Procurement ·
India DPI (India Stack) · UNDP DPG Standard · Green Climate Fund · Doha Declaration · Nagoya
Protocol · CBDR-RC / Paris Agreement · Global Digital Compact · ILO automation methodology ·
World Bank STEP · Kenya FinAccess · Smart Africa · ASEAN DEFA · CARICOM CDTP · GAIA-X.

### Recurring themes
Zero-new-legislation pathway · accountability through procurement · vendor lock-in & the DPI
open-standards test · multilateral negotiating playbook · labor-displacement early warning ·
regional pooling of digital infrastructure.

### Source caveat
The report was generated during a web-retriever outage and self-flags that its URLs and some
data points are unverified. Treat every primary-source link as **verify-before-citing**.

### The 7 capability areas (CA)
- **CA1** National AI Readiness Self-Assessment
- **CA2** Minimum-Viable Domestic AI Governance
- **CA3** AI Harm Reporting, Redress, and Accountability
- **CA4** Development-Finance Conditionality and Vendor Lock-In
- **CA5** Shifting Multilateral Negotiating Language
- **CA6** Labor-Displacement Early-Warning Systems
- **CA7** Regional Shared-Services and Pooled Digital Infrastructure
