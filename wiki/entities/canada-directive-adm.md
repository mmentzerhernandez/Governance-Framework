---
title: Canada Directive on Automated Decision-Making (AIA)
type: entity
tags: [canada, aia, procurement, accountability, ca2]
created: 2026-06-01
updated: 2026-06-05
sources: [ai-governance-global-majority-report]
---

# Canada Directive on Automated Decision-Making (Algorithmic Impact Assessment)

**Type:** accountability directive + open-source assessment tool
**Origin:** Treasury Board of Canada Secretariat (TBS)
**Year:** April 2019 (original); variously dated 2021 and 2023 for subsequent revisions — exact version dates unconfirmed across sources.
**Capability area:** [[ca2-minimum-viable-governance]] (CA2-BP2), one of the most widely replicated public-sector algorithmic-accountability instruments.

## What it is
Requires every federal department deploying decision-affecting AI to complete an **Algorithmic
Impact Assessment (AIA)** before deployment, a free, web-based questionnaire (no AI expertise
needed, 2–4 hours) that auto-scores the system into one of four impact levels:

| Level | Example | Obligations |
|---|---|---|
| I | Low-stakes routing | Notice to affected individuals |
| II | Benefits screening | + Explanation on request + human-review option |
| III | Welfare/license decisions | + Peer review + plain-language explanation + annual audit |
| IV | Criminal justice, immigration, health | + Interdepartmental review + full explainability + independent bias audit |

The tool is **MIT-licensed**, free to translate and adapt.

## Documented outcomes
- 70+ federal AI systems assessed by 2023, results in a public registry.
- Adopted/adapted by Argentina (2022), Brazil's SERPRO (2023); referenced by UK, OECD, World Bank,
  and the EU AI Act's conformity-assessment design.
- Zero new legislation: operates under existing Treasury Board authority.

## Transferable mechanism
1. Translate the AIA questionnaire (MIT licence): https://canada-ca.github.io/aia-eia-js/
2. Issue a Treasury/Finance circular requiring an AIA before any ministry deploys/procures AI.
3. Create a simple public AIA registry webpage.
4. Use Levels III–IV obligations as minimum contract clauses in high-stakes procurement.

> ⚠️ Audit note (2026-06-05): The source report described Canada's AIA as "the most operationally detailed public-sector AI accountability instrument in the world." This superlative is unsupported; the EU AI Act, UK ATRS, and NSW AI Assessment Framework are comparable instruments. Softened above to "one of the most widely replicated."

## Primary source
TBS, *Directive on Automated Decision-Making* (2019/2023):
https://www.tbs-sct.canada.ca/pol/doc-eng.aspx?id=32592 · Tool: https://canada-ca.github.io/aia-eia-js/
*(verify-before-citing, see [[ai-governance-global-majority-report]])*

## Cross-references
- [[procurement-lever]]: the package component built on the AIA
- [[ca2-minimum-viable-governance]]
- [[rwanda-ai-policy]]: embeds an AIA-style template
