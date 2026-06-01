# Wiki Log

> How this wiki was generated, step by step — the process used to turn one source report into
> an interlinked, clickable knowledge base, and how its ideas and concepts were connected.

---

## [Step 1] Start from a single source
Everything here was compiled from **one document** — `AI_Governance_Global_Majority_Research.md`,
a best-practice survey of *implemented* AI-governance mechanisms for Global South governments.
The llm-wiki method compiles that knowledge **once** into durable, linked pages rather than
re-reading the whole report on every question (the difference from RAG). So the report became the
single root that every other page traces back to.

## [Step 2] Find the two operational spines
Reading the report surfaced its two backbones, and these became the wiki's organizing skeleton:
the **5-phase Implementation Sequence** (Diagnose → Anchor → Protect → Engage → Monitor) and the
**6-component Minimum-Viable Governance Package**. Together they answer "in what order?" and "what
exactly do we stand up?" — and they became the two tables on the landing page.

## [Step 3] Decompose the report into four page types
Each distinct idea was given its own page, sorted into four types: **source** (the report itself),
**entities** (26 frameworks/tools/orgs — UNESCO RAM, Canada AIA, Brazil ANPD, India DPI, …),
**concepts** (15 pages: 6 package-component "levers", 7 capability-area hubs, 2 overarching
principles), and the **overview** (the spine). One page = one idea keeps each concept reusable and
linkable.

## [Step 4] Map each action to its evidence
This is the core connection rule. Every package component (a "lever" — what a country *does*) was
traced to the report's capability-area best-practice entry that justifies it, and then to the
specific framework that implements it. Example chain: **Procurement Lever → Capability Area 2 →
Canada's Algorithmic Impact Assessment**. Doing this for all six levers connected *action* to
*evidence* to *real-world precedent*.

## [Step 5] Wire the graph with wiki-links
Pages were then cross-linked using Obsidian-style wiki-links (each reference wraps a page name in
double square brackets) so the wiki reads as a graph, not a list. Every page links to at least two
others: levers link **down** to their framework entity and **up** to their capability-area hub;
each implementation phase links to the frameworks active in it; the two overarching principles
(zero-new-legislation, the DPI lock-in test) cut **across** many pages; and every page cites the
source — making one rooted citation graph you can traverse from any starting point.

## [Step 6] Build the clickable landing page
`overview.md` was assembled as the entry point: the 5-phase sequence and 6-component package
rendered as tables where **every phase action and every component is a drill-in link**. A reader can
move from "what do I do in months 1–9?" straight to the framework that delivers it, then back.

## [Step 7] Verify the graph holds together
The whole link graph was checked: zero dangling links, every page reachable, and the index
counts consistent with the pages created. This guarantees a reader never hits a dead end.

## [Step 8] Export to a self-contained, clickable site
Finally a small generator (`build_html.py`) converted the markdown into one self-contained
`wiki.html`: each wiki-link became an in-page anchor, tables/lists/callouts became HTML, and a tiny
hash-router makes each page open on its own (land on the Overview, click through to any page, click
back). No external files — the whole knowledge base travels as a single shareable document.
