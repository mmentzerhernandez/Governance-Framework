#!/usr/bin/env python3
"""Generate a self-contained wiki.html from the llm-wiki markdown, using the S03 / StructureSense
CSS template (verbatim) from 'WIKI-TO-HTML copy/SKILL.md'."""
import re, glob, os, html

ROOT = "/Users/rabies/Desktop/Wiki"
SKILL = os.path.join(ROOT, "WIKI-TO-HTML copy", "SKILL.md")

# ---- pull the exact CSS block verbatim from the reference SKILL.md ----
skill_txt = open(SKILL).read()
css = re.search(r"## CSS Template.*?```css\n(.*?)\n```", skill_txt, re.S).group(1)

# ---- load pages ----
def parse(path):
    raw = open(path).read()
    fm = {}
    body = raw
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", raw, re.S)
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                fm[k.strip()] = v.strip()
        body = m.group(2)
    slug = os.path.splitext(os.path.basename(path))[0]
    return {"slug": slug, "fm": fm, "body": body.strip(),
            "title": fm.get("title", slug), "type": fm.get("type", "")}

pages = {}
for f in glob.glob(os.path.join(ROOT, "wiki", "**", "*.md"), recursive=True):
    p = parse(f)
    pages[p["slug"]] = p

# ---- inline markdown -> html ----
def inline(text):
    text = html.escape(text, quote=False)
    # wiki links [[slug|label]] or [[slug]]
    def wl(m):
        tgt = m.group(1).strip(); lab = (m.group(2) or tgt).strip()
        return f'<a href="#{tgt}">{lab}</a>'
    text = re.sub(r"\[\[([^\]|]+)(?:\|([^\]]*))?\]\]", wl, text)
    # markdown links [text](url)
    text = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)",
                  r'<a href="\2">\1</a>', text)
    # bare urls (not already in an href)
    text = re.sub(r'(?<!["\(>])(https?://[^\s<]+)', r'<a href="\1">\1</a>', text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    return text

def render_body(body):
    lines = body.splitlines()
    out = []; i = 0; n = len(lines)
    while i < n:
        line = lines[i]
        s = line.strip()
        if not s:
            i += 1; continue
        # callouts / blockquotes
        if s.startswith(">"):
            content = s.lstrip(">").strip()
            if content.startswith("⚠️"):
                out.append(f'<div class="contradiction-callout">{inline(content)}</div>')
            elif content.startswith("🔍"):
                out.append(f'<div class="gap-callout">{inline(content)}</div>')
            else:
                out.append(f'<div class="gap-callout">{inline(content)}</div>')
            i += 1; continue
        # headings
        if s.startswith("#"):
            h = len(s) - len(s.lstrip("#"))
            txt = inline(s[h:].strip())
            tag = "h3" if h <= 2 else "h4"
            out.append(f"<{tag}>{txt}</{tag}>")
            i += 1; continue
        # table
        if "|" in line and i + 1 < n and re.match(r"^\s*\|?[\s:\-|]+\|?\s*$", lines[i+1]):
            header = [c.strip() for c in line.strip().strip("|").split("|")]
            i += 2
            rows = []
            while i < n and "|" in lines[i] and lines[i].strip():
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            t = ["<table><thead><tr>"] + [f"<th>{inline(c)}</th>" for c in header] + ["</tr></thead><tbody>"]
            for r in rows:
                t.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
            t.append("</tbody></table>")
            out.append("".join(t))
            continue
        # unordered list
        if re.match(r"^\s*[-*]\s+", line):
            items = []
            while i < n and re.match(r"^\s*[-*]\s+", lines[i]):
                items.append(inline(re.sub(r"^\s*[-*]\s+", "", lines[i])))
                i += 1
            out.append("<ul>" + "".join(f"<li>{x}</li>" for x in items) + "</ul>")
            continue
        # ordered list
        if re.match(r"^\s*\d+\.\s+", line):
            items = []
            while i < n and re.match(r"^\s*\d+\.\s+", lines[i]):
                items.append(inline(re.sub(r"^\s*\d+\.\s+", "", lines[i])))
                i += 1
            out.append("<ol>" + "".join(f"<li>{x}</li>" for x in items) + "</ol>")
            continue
        if set(s) <= set("-"):  # hr
            i += 1; continue
        # paragraph (gather until blank)
        para = [line]
        i += 1
        while i < n and lines[i].strip() and not re.match(r"^\s*([-*]\s|\d+\.\s|#|>|\|)", lines[i]):
            para.append(lines[i]); i += 1
        out.append(f"<p>{inline(' '.join(x.strip() for x in para))}</p>")
    return "\n".join(out)

# ---- ordering / grouping ----
levers = ["diagnostic-anchor","procurement-lever","regulatory-lever","redress-focal-point",
          "infrastructure-safeguard","protection-survey"]
crosscut = ["zero-new-legislation-pathway","vendor-lock-in-dpi-test"]
cas = [f"ca{i}-" for i in range(1,8)]
ca_slugs = [s for n in cas for s in pages if s.startswith(n)]
entity_slugs = [p["slug"] for p in pages.values() if p["type"]=="entity"]
# order entities by the index order
entity_order = ["unesco-ram","oxford-insights-gari","imf-ai-preparedness-index","singapore-ai-verify",
  "canada-directive-adm","brazil-lgpd-anpd","rwanda-ai-policy","au-continental-ai-strategy",
  "oecd-ai-incidents-monitor","ai-incident-database-nist","eu-ai-act","world-bank-procurement",
  "india-dpi-stack","undp-dpg-standard","green-climate-fund","doha-declaration","nagoya-protocol",
  "cbdr-rc-paris","global-digital-compact","ilo-automation-methodology","world-bank-step",
  "kenya-finaccess","smart-africa","asean-defa","caricom-cdtp","gaia-x"]
entity_slugs = [s for s in entity_order if s in pages]
source_slugs = [p["slug"] for p in pages.values() if p["type"]=="source"]

n_src=len(source_slugs); n_con=len(levers)+len(crosscut)+len(ca_slugs); n_ent=len(entity_slugs)

def section(slug, label, active=False):
    p = pages[slug]
    cls = "section page active" if active else "section page"
    return (f'<section class="{cls}" id="{slug}">'
            f'<div class="section-label">{html.escape(label)}</div>'
            f'<h2>{html.escape(p["title"])}</h2>'
            f'{render_body(p["body"])}</section>')

# ---- log section ----
log = pages.get("log")
log_html = ""
if log:
    entries = re.findall(r"^## \[([^\]]+)\]([^\n]*)\n(.*?)(?=^## \[|\Z)", log["body"], re.S|re.M)
    rows = []
    for date, head, body in entries:
        rows.append(f'<div class="log-entry"><div class="log-date">{html.escape(date)}</div>'
                    f'<div class="log-content"><strong>{inline(head.strip(" |"))}</strong><br>'
                    f'{inline(" ".join(l.strip() for l in body.strip().splitlines()))}</div></div>')
    log_html = ('<section class="section page" id="log"><div class="section-label">History</div>'
                '<h2>Log</h2>' + "".join(rows) + "</section>")

# ---- sidebar ----
def nav_links(slugs):
    return "".join(f'<a href="#{s}">{html.escape(pages[s]["title"])}</a>' for s in slugs)

nav = f"""<nav>
  <div class="nav-header"><h1>National AI Governance Playbook</h1>
  <div class="nav-sub">Global Majority Governments · {n_ent} frameworks</div></div>
  <div class="nav-section">Overview</div>
  <a href="#overview">Start Here — Playbook</a>
  <div class="nav-section">The 6-Component Package</div>
  {nav_links(levers)}
  <div class="nav-section">Cross-Cutting</div>
  {nav_links(crosscut)}
  <div class="nav-section">Capability Areas</div>
  {nav_links(ca_slugs)}
  <div class="nav-section">Frameworks &amp; Tools</div>
  {nav_links(entity_slugs)}
  <div class="nav-section">Source &amp; History</div>
  {nav_links(source_slugs)}
  <a href="#log">Log</a>
</nav>"""

# ---- body sections (overview is the landing page; one page shown at a time) ----
body_sections = [section("overview","Domain", active=True)]
for s in levers: body_sections.append(section(s,"Package Component"))
for s in crosscut: body_sections.append(section(s,"Cross-Cutting Theme"))
for s in ca_slugs: body_sections.append(section(s,"Capability Area"))
for s in entity_slugs: body_sections.append(section(s,"Framework / Tool / Org"))
for s in source_slugs: body_sections.append(section(s,"Source"))
body_sections.append(log_html)

# Routing layer: only the active page is visible; links navigate between pages via the hash.
# Added as a separate style block so the verbatim S03 CSS template above is left unaltered.
route_css = """
/* Replace the light-blue accent (#01BAEF) everywhere — nav, headers, links, borders, pills */
:root { --accent-blue: #002fa7; }
.page { display: none; }
.page.active { display: block; }
nav a.nav-current { background: var(--border-strong); color: #ffffff; }
.page-back { display: inline-block; margin-bottom: 20px; font-family: var(--font-display);
  font-size: 11px; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase;
  text-decoration: none; color: var(--text-primary); border: var(--border-medium) solid var(--border-strong); padding: 6px 12px; }
.page-back:hover { background: var(--border-strong); color: #ffffff; }
/* Recolor in-content links from the light-blue accent to #002fa7 */
main a { color: #002fa7; }
.section td a, .field-value a, .url-list li a { color: #002fa7; }
.field-value a { border-bottom: 1px solid #002fa7; }
.field-value a:hover, .section td a:hover { background: #002fa7; color: #ffffff; }
"""

route_js = """
function showPage() {
  var id = (location.hash || '#overview').slice(1) || 'overview';
  var pages = document.querySelectorAll('.page');
  var found = false;
  pages.forEach(function (p) { var on = (p.id === id); p.classList.toggle('active', on); if (on) found = true; });
  if (!found) { var ov = document.getElementById('overview'); if (ov) ov.classList.add('active'); }
  document.querySelectorAll('nav a').forEach(function (a) {
    a.classList.toggle('nav-current', a.getAttribute('href') === '#' + id);
  });
  window.scrollTo(0, 0);
}
window.addEventListener('hashchange', showPage);
window.addEventListener('DOMContentLoaded', showPage);
"""

# A "back to overview" link on every non-landing page
def with_back(html_section, slug):
    if slug == "overview":
        return html_section
    back = '<a class="page-back" href="#overview">← Back to Playbook</a>'
    return html_section.replace('">', '">' + back, 1) if False else \
        re.sub(r'(<h2>.*?</h2>)', r'\1' + back, html_section, count=1)

body_sections = [with_back(s, re.search(r'id="([^"]+)"', s).group(1)) for s in body_sections]

doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>National AI Governance Playbook for Global Majority Governments</title>
<style>{css}</style>
<style>{route_css}</style>
</head>
<body>
{nav}
<main>
{''.join(body_sections)}
</main>
<script>{route_js}</script>
</body>
</html>"""

open(os.path.join(ROOT, "wiki.html"), "w").write(doc)
print(f"wiki.html written — {n_src} source, {n_con} concepts, {n_ent} frameworks, {len(pages)} pages total")
