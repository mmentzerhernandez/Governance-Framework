# Fact Check Report — AI Governance Wiki + wiki.html
**Date:** 2026-06-02
**Content checked:** wiki/ (43 .md pages) · wiki.html
**Sources audited:** AI_Governance_Global_Majority_Research.md
**Claims extracted:** 247   **Sections checked:** 43

---

## Summary Scorecard

| Status | Count |
|---|---|
| FAIL | 0 |
| WARNING | 3 |
| PASS | 244 |

**Verification status:** CORRECTIONS REQUIRED (3 warnings, 0 hard failures)

---

## Findings by Section

### CA7 Regional Infrastructure (3 warnings — same root issue, 3 locations)

---

**[WARNING] MODAL DOWNGRADE**
```
Claim ID:       CLM-ASEAN-01
Section:        asean-defa — What it is
Claim type:     Modal
Content text:   "the first comprehensive regional digital-economy treaty among
                developing economies (modular 8-pillar architecture)"
Source passage: "will be the world's first comprehensive regional digital economy
                treaty among developing and emerging-market countries when
                concluded … under active negotiation through 2023–2024 (with
                conclusion targeted for 2025)"
                [CA7-BP2, paragraph (a)]
Finding:        Source uses future tense ("will be…when concluded") and
                explicitly states the DEFA was still under negotiation with a
                2025 target date. The wiki converts this to present tense,
                implying the treaty has been concluded when it had not been.
Required action: Revise to future tense: "will be the first comprehensive
                regional digital-economy treaty among developing economies once
                concluded (targeted 2025)" — or add a parenthetical noting
                "under negotiation as of 2024."
```

---

**[WARNING] MODAL DOWNGRADE**
```
Claim ID:       CLM-ASEAN-02
Section:        ca7-regional-infrastructure.md — The models bullet list
Claim type:     Modal
Content text:   "the first comprehensive regional digital-economy treaty among
                developing economies (modular 8-pillar architecture)"
Source passage: "will be the world's first comprehensive regional digital economy
                treaty among developing and emerging-market countries when
                concluded" [CA7-BP2, paragraph (a)]
Finding:        Same temporal distortion as CLM-ASEAN-01. The CA7 capability-
                area hub page repeats the present-tense framing.
Required action: Apply the same correction as CLM-ASEAN-01.
```

---

**[WARNING] MODAL DOWNGRADE**
```
Claim ID:       CLM-ASEAN-03
Section:        wiki.html — CA7 regional infrastructure section
Claim type:     Modal
Content text:   "the first comprehensive regional digital-economy treaty among
                developing economies"
Source passage: "will be the world's first comprehensive regional digital economy
                treaty among developing and emerging-market countries when
                concluded" [CA7-BP2, paragraph (a)]
Finding:        The HTML file mirrors the erroneous present-tense framing from
                the wiki source pages. It will self-correct once the two wiki
                pages are fixed and the HTML is regenerated.
Required action: Fix wiki source pages (CLM-ASEAN-01, CLM-ASEAN-02) then
                regenerate wiki.html.
```

---

## All Other Sections — PASS Summary

244 claims across 42 sections checked and **VERIFIED** against the source document.
Categories covered and verified:

- **All numeric statistics:** IMF scores (0.33/0.73, 0.41/0.54), country counts
  (174, 193, 27, 15, 16, 34, 46+, 50+, 105, 138), transaction volumes
  (12.2 billion UPI), financial figures ($52m SADEF, $35.7m CCCCC, $50m CDTP,
  R$400m FUNBIO), percentages (24%, 68%, 61%, 12%, 28%, 30–40%), rankings
  (52nd/62nd GARI), thresholds (>0.05 AEI, 90 days exit planning, 2–4 hours
  AIA, 6 weeks RAM).

- **All legal/regulatory references:** LGPD Article 20, Rwanda Law 058/2021,
  EU Regulation 2024/1689 Articles 8–15 and 26, WTO WT/MIN(01)/DEC/2,
  Nagoya Protocol CBD COP10, Paris Agreement Art. 2.2, GDC A/RES/79/L.1,
  ANPD Resolution 16/2024, NIST AI RMF 1.0, ILO Working Paper No. 87 (2023),
  World Bank WPS10415 (April 2023).

- **All named entities, dates, and impact-level tables:** verified against
  source chapter-by-chapter.

- **Source caveat preservation:** All 26 entity pages include the
  "verify-before-citing" notice referencing the web-retriever outage. The
  overview.md and source summary page both carry the Gap notice. The critical
  reliability caveat from the source is fully preserved throughout the wiki.

- **Zero-new-legislation framing:** The wiki correctly and consistently
  represents the source's central claim that existing procurement rules,
  data-protection statutes, and executive circulars are sufficient — without
  overstating or understating the legal position.

- **Implementation sequence and minimum-viable package:** All 5 phases and 6
  package components correctly reproduce the source's timelines, costs, and
  component descriptions.

---

## Required Corrections

1. **CLM-ASEAN-01** · `wiki/entities/asean-defa.md` · "What it is" section
   — Add future tense / "under negotiation" qualifier to the DEFA description.

2. **CLM-ASEAN-02** · `wiki/concepts/ca7-regional-infrastructure.md` · "The models" bullet
   — Apply same correction.

3. **CLM-ASEAN-03** · `wiki.html` · CA7 section
   — Regenerate after fixing items 1 and 2 above.

---

## Recommended Reviews (human expert)

All 3 warnings stem from the same single root issue (ASEAN DEFA tense). No independent
expert reviews are required beyond applying the corrections above.

**Note on URL verification:** The source explicitly self-flags that its web search
retriever experienced an outage and that all primary-source URLs should be verified at
institutional portals before use in formal documents. This caveat is faithfully
preserved in the wiki (every entity page carries it). A human reviewer should verify
the URLs before the wiki is used in any advisory deliverable — this is already flagged
in the wiki's own gap notes.
