# Fact Check Report — AI Governance Wiki + wiki.html (Run 2: Post URL-Update Re-Check)
**Date:** 2026-06-02
**Content checked:** wiki/ (43 .md pages) · wiki.html
**Sources audited:** AI_Governance_Global_Majority_Research.md
**Claims extracted:** 52 (URL/citation claims + ASEAN DEFA modal re-check)   **Sections checked:** 28

---

## Summary Scorecard

| Status | Count |
|---|---|
| FAIL | 3 |
| WARNING | 8 |
| PASS | 41 |

**Verification status:** CORRECTIONS REQUIRED

---

## Prior Warning Resolved

**ASEAN DEFA tense — FIXED ✓**
The 3 warnings from Run 1 are resolved. `asean-defa.md` now reads "Set to be the world's first comprehensive regional digital-economy treaty … negotiating 2023–2024 (conclusion targeted 2025)." Future tense correctly preserved throughout.

---

## Findings by Section

### FAIL items (must correct)

---

**[FAIL] CITATION MISMATCH**
```
Claim ID:       CLM-URL-01
Section:        unesco-ram.md — Primary source URL
Claim type:     Reference
Content text:   "https://www.unesco.org/en/artificial-intelligence/recommendation-ethics"
Source passage: "https://www.unesco.org/en/artificial-intelligence/recommendation/ram"
                [CA1-BP1(e)]
Finding:        /recommendation-ethics leads to the UNESCO Recommendation on AI Ethics
                — a different resource entirely. The source specifies /recommendation/ram,
                the RAM-specific page. A reader following the wiki link reaches the
                wrong document.
Required action: Restore the source URL:
                https://www.unesco.org/en/artificial-intelligence/recommendation/ram
```

---

**[FAIL] CITATION MISMATCH**
```
Claim ID:       CLM-URL-02
Section:        ilo-automation-methodology.md — Primary source URL
Claim type:     Reference
Content text:   "ILO Working Paper No. 87 (2023):
                https://www.ilo.org/publications/flagship-reports/
                world-employment-and-social-outlook-trends-2024"
Source passage: "ILO Working Paper No. 87 (2023), *Automation and the Future of Work
                in Developing Countries*:
                https://www.ilo.org/wcmsp5/groups/public/---dgreports/---inst/
                documents/publication/wcms_869256.pdf"
                [CA6-BP1(e)]
Finding:        The primary source label says "Working Paper No. 87" but the URL
                leads to the ILO WESO 2024 flagship report — a completely different
                publication. WESO 2024 was a secondary source for this entry; it
                must not replace the Working Paper citation.
Required action: Restore Working Paper No. 87 URL:
                https://www.ilo.org/wcmsp5/groups/public/---dgreports/---inst/
                documents/publication/wcms_869256.pdf
                WESO 2024 may be retained as a supplementary note.
```

---

**[FAIL] CITATION MISMATCH + INTERNAL INCONSISTENCY**
```
Claim ID:       CLM-URL-03
Section:        gaia-x.md — Primary source URL + entity header
Claim type:     Reference
Content text:   Header: "Trust Framework v23.06 (2023)"
                URL: https://docs.gaia-x.eu/policy-rules-committee/
                     trust-framework/22.10/
Source passage: "GAIA-X Trust Framework v23.06:
                https://docs.gaia-x.eu/policy-rules-committee/trust-framework/23.06/"
                [CA7-BP4(e)]
Finding:        Page header correctly says v23.06 (matching the source) but the URL
                was changed to v22.10 — one version earlier. Creates an internal
                contradiction within the page and contradicts the source.
Required action: Restore:
                https://docs.gaia-x.eu/policy-rules-committee/trust-framework/23.06/
```

---

### WARNING items (human review required)

---

**[WARNING] NOT FOUND**
```
Claim ID:       CLM-URL-04
Section:        kenya-finaccess.md — Primary source URL (CBK)
Content text:   "https://www.centralbank.go.ke/wp-content/uploads/2022/08/
                2021-Finaccesss-Survey-Report.pdf"
Source passage: "https://www.centralbank.go.ke/wp-content/uploads/2021/12/
                2021-FinAccess-Household-Survey-Report.pdf" [CA6-BP3(e)]
Finding:        Path date changed (2021/12 → 2022/08) and filename has triple-s
                "Finaccesss" — likely a transcription error. Cannot confirm URL
                is live without browser access.
Required action: Verify at CBK portal. If broken or "Finaccesss" is a typo,
                restore source URL.
```

**[WARNING] GENERALIZATION**
```
Claim ID:       CLM-URL-05
Section:        kenya-finaccess.md — Primary source URL (FSD Africa)
Content text:   "https://fsdafrica.org/publications/"
Source passage: "https://fsdafrica.org/research/ai-and-financial-services/"
                [CA6-BP3(e)]
Finding:        Changed from the specific report page to the general publications
                index. The named 2023 report is no longer directly linked.
Required action: Verify if /research/ai-and-financial-services/ is still live;
                if so, restore.
```

**[WARNING] NOT FOUND**
```
Claim ID:       CLM-URL-06
Section:        singapore-ai-verify.md — Primary source URL
Content text:   "https://aiverifyfoundation.sg/"
Source passage: "https://aiverify.sg" [CA2-BP1(e)]
Finding:        Different domain than source specifies. May be a valid updated
                canonical URL or may be incorrect.
Required action: Confirm which domain is the current official AI Verify
                Foundation website.
```

**[WARNING] GENERALIZATION**
```
Claim ID:       CLM-URL-07
Section:        world-bank-step.md — Primary source URL (WPS10415)
Content text:   "https://openknowledge.worldbank.org/"
Source passage: "https://openknowledge.worldbank.org/handle/10986/39788"
                [CA6-BP2(e)]
Finding:        Specific document handle removed; now links only to the
                repository homepage.
Required action: Restore:
                https://openknowledge.worldbank.org/handle/10986/39788
```

**[WARNING] GENERALIZATION**
```
Claim ID:       CLM-URL-08
Section:        india-dpi-stack.md — Primary source URL (G20)
Content text:   "https://www.g20.org/en/"
Source passage: "https://www.g20.org/content/dam/gtwenty/gtwenty_new/document/
                G20_Digital_Economy_Outcome_Document_and_Chair_Summary.pdf"
                [CA4-BP1(e)]
Finding:        Specific document PDF replaced with G20 homepage.
Required action: Verify if source PDF is still live; if so, restore it.
```

**[WARNING] GENERALIZATION**
```
Claim ID:       CLM-URL-09
Section:        rwanda-ai-policy.md — Primary source URL
Content text:   "https://www.minict.gov.rw"
Source passage: "https://www.minict.gov.rw/index.php/en/artificial-intelligence-policy"
                [CA2-BP4(e)]
Finding:        Specific AI Policy page path dropped; links only to homepage.
Required action: Verify if specific path is still live; if so, restore.
```

**[WARNING] NOT FOUND**
```
Claim ID:       CLM-URL-10
Section:        asean-defa.md — Primary source URL (DEFA)
Content text:   "https://asean.org/our-communities/economic-community/
                asean-digital-sector/digital-economy-framework-agreement/"
Source passage: "https://asean.org/asean-digital-economy-framework-agreement/"
                [CA7-BP2(e)]
Finding:        Path structure changed significantly. May be a valid URL
                restructure by ASEAN Secretariat.
Required action: Verify both URLs resolve to the DEFA page.
```

**[WARNING] NOT FOUND**
```
Claim ID:       CLM-URL-11
Section:        asean-defa.md — Primary source URL (ASEAN AI Guide)
Content text:   "https://asean.org/book/asean-guide-on-ai-governance-and-ethics/"
Source passage: "https://asean.org/wp-content/uploads/2023/09/
                ASEAN-Guide-on-AI-Governance-and-Ethics_2023.pdf"
                [CA7-BP2(e)]
Finding:        Changed from direct PDF link to a web landing page. Cannot
                confirm 2023 2nd edition content is accessible at new URL.
Required action: Verify 2nd edition 2023 PDF is accessible from the new URL.
```

---

## Required Corrections (3 FAIL items)

1. **CLM-URL-01** · `wiki/entities/unesco-ram.md` + `wiki.html`
   Restore UNESCO RAM URL: `https://www.unesco.org/en/artificial-intelligence/recommendation/ram`
   *(Current URL goes to the AI Ethics Recommendation page, not the RAM page)*

2. **CLM-URL-02** · `wiki/entities/ilo-automation-methodology.md` + `wiki.html`
   Restore ILO Working Paper No. 87 URL:
   `https://www.ilo.org/wcmsp5/groups/public/---dgreports/---inst/documents/publication/wcms_869256.pdf`
   *(Current URL goes to WESO 2024, a different ILO publication entirely)*

3. **CLM-URL-03** · `wiki/entities/gaia-x.md` + `wiki.html`
   Restore GAIA-X Trust Framework v23.06 URL:
   `https://docs.gaia-x.eu/policy-rules-committee/trust-framework/23.06/`
   *(Current URL goes to v22.10; page header already correctly says v23.06)*

---

## Recommended Reviews (8 WARNING items)

1. **CLM-URL-04** — Kenya FinAccess CBK URL: verify `2022/08/2021-Finaccesss-Survey-Report.pdf` is live and "Finaccesss" is not a typo.
2. **CLM-URL-05** — FSD Africa URL: verify if specific `/research/ai-and-financial-services/` page is still live.
3. **CLM-URL-06** — AI Verify Foundation: confirm `aiverifyfoundation.sg` vs `aiverify.sg` — which is current official domain.
4. **CLM-URL-07** — World Bank WPS10415: restore `/handle/10986/39788` if document is still at that handle.
5. **CLM-URL-08** — G20 DPI Framework: verify if specific PDF URL is still live.
6. **CLM-URL-09** — Rwanda MINICT: verify if `/index.php/en/artificial-intelligence-policy` path is still live.
7. **CLM-URL-10** — ASEAN DEFA URL: verify both old and new path resolve to the DEFA page.
8. **CLM-URL-11** — ASEAN AI Guide: verify 2nd edition 2023 content is accessible at the new web page URL.

---

## What Was Not Changed (No New Errors Introduced)

All factual content (statistics, legal article numbers, country counts, financial figures, named entities,
obligation tables, sequencing, and the minimum-viable package components) remained unchanged from Run 1.
244 non-URL claims remain VERIFIED. The URL-update edits touched only primary-source link fields and
did not introduce any new factual or structural errors.
