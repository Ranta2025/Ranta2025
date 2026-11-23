#!/usr/bin/env python3
"""Generate the SVG assets used by README.md and README.es.md.

Run from the repository root:  python3 scripts/build_assets.py
GitHub renders SVGs inside <img> with CSS/SMIL animation but no JavaScript and
no web fonts, so every asset is self-contained and uses system font stacks.
"""
import os
import textwrap
from html import escape

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets")
os.makedirs(OUT, exist_ok=True)

SANS = "-apple-system, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
MONO = "'SF Mono', 'JetBrains Mono', Consolas, 'Liberation Mono', monospace"
REDUCE = "@media (prefers-reduced-motion: reduce){*{animation:none!important}}"


def write(name, svg):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(svg)


def e(s):
    return escape(s, quote=True)


# --------------------------------------------------------------------- hero
def hero(lang, phrases, role, status, label):
    W, H = 1000, 380
    ph = ""
    for i, p in enumerate(phrases):
        ph += (f'<text class="p p{i+1}" x="64" y="262" font-family="{MONO}" font-size="21" fill="#e0e7ff">'
               f'<tspan fill="#22d3ee">&gt; </tspan>{e(p)}</text>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{e(label)}">
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#070b18"/><stop offset=".55" stop-color="#14103a"/><stop offset="1" stop-color="#070b18"/>
  </linearGradient>
  <linearGradient id="name" gradientUnits="userSpaceOnUse" x1="60" y1="0" x2="560" y2="0" spreadMethod="reflect">
    <stop offset="0" stop-color="#22d3ee"/><stop offset=".5" stop-color="#8b5cf6"/><stop offset="1" stop-color="#f472b6"/>
    <animateTransform attributeName="gradientTransform" type="translate" values="-220 0;220 0;-220 0" dur="9s" repeatCount="indefinite"/>
  </linearGradient>
  <linearGradient id="ring" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#22d3ee"/><stop offset="1" stop-color="#f472b6"/>
  </linearGradient>
  <radialGradient id="rg1"><stop offset="0" stop-color="#8b5cf6" stop-opacity=".85"/><stop offset="1" stop-color="#8b5cf6" stop-opacity="0"/></radialGradient>
  <radialGradient id="rg2"><stop offset="0" stop-color="#22d3ee" stop-opacity=".7"/><stop offset="1" stop-color="#22d3ee" stop-opacity="0"/></radialGradient>
  <radialGradient id="rg3"><stop offset="0" stop-color="#f472b6" stop-opacity=".6"/><stop offset="1" stop-color="#f472b6" stop-opacity="0"/></radialGradient>
  <pattern id="grid" width="36" height="36" patternUnits="userSpaceOnUse">
    <path d="M36 0H0V36" fill="none" stroke="#ffffff" stroke-opacity=".045"/>
  </pattern>
  <clipPath id="clip"><rect width="{W}" height="{H}" rx="22"/></clipPath>
</defs>
<style>
  .b1{{animation:f1 14s ease-in-out infinite alternate}}
  .b2{{animation:f2 17s ease-in-out infinite alternate}}
  .b3{{animation:f3 12s ease-in-out infinite alternate}}
  @keyframes f1{{to{{transform:translate(120px,60px)}}}}
  @keyframes f2{{to{{transform:translate(-110px,-40px)}}}}
  @keyframes f3{{to{{transform:translate(-60px,70px)}}}}
  .p{{opacity:0;animation:cyc 9s infinite}}
  .p2{{animation-delay:3s}} .p3{{animation-delay:6s}}
  @keyframes cyc{{0%{{opacity:0;transform:translateY(10px)}}5%,28%{{opacity:1;transform:none}}33%,100%{{opacity:0;transform:translateY(-10px)}}}}
  .pulse{{animation:pl 2s ease-out infinite;transform-origin:center;transform-box:fill-box}}
  @keyframes pl{{0%{{opacity:.7;transform:scale(1)}}100%{{opacity:0;transform:scale(2.6)}}}}
  {REDUCE}
  @media (prefers-reduced-motion: reduce){{.p1{{opacity:1}}}}
</style>
<g clip-path="url(#clip)">
  <rect width="{W}" height="{H}" fill="url(#bg)"/>
  <g>
    <circle class="b1" cx="130" cy="70" r="230" fill="url(#rg1)"/>
    <circle class="b2" cx="880" cy="300" r="250" fill="url(#rg2)"/>
    <circle class="b3" cx="620" cy="40" r="190" fill="url(#rg3)"/>
  </g>
  <rect width="{W}" height="{H}" fill="url(#grid)"/>
  <!-- window chrome -->
  <circle cx="44" cy="40" r="6" fill="#ff5f57"/><circle cx="64" cy="40" r="6" fill="#febc2e"/><circle cx="84" cy="40" r="6" fill="#28c840"/>
  <text x="108" y="45" font-family="{MONO}" font-size="13" fill="#94a3b8">~/rafael-tanda</text>
  <!-- right-hand orbit art -->
  <g transform="translate(815 190)">
    <circle r="150" fill="none" stroke="#ffffff" stroke-opacity=".06"/>
    <circle r="108" fill="none" stroke="url(#ring)" stroke-width="2" stroke-dasharray="6 14" stroke-linecap="round">
      <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="40s" repeatCount="indefinite"/>
    </circle>
    <circle r="70" fill="none" stroke="url(#ring)" stroke-width="2.5" stroke-dasharray="90 350" stroke-linecap="round">
      <animateTransform attributeName="transform" type="rotate" from="360" to="0" dur="14s" repeatCount="indefinite"/>
    </circle>
    <circle r="34" fill="url(#ring)" opacity=".9"/>
    <text y="9" text-anchor="middle" font-family="{MONO}" font-size="24" font-weight="700" fill="#0b1020">&lt;/&gt;</text>
    <g font-family="{MONO}" font-size="13" font-weight="600" fill="#e0e7ff">
      <g transform="translate(-170 -110)"><rect width="46" height="26" rx="13" fill="#22d3ee" fill-opacity=".16" stroke="#22d3ee" stroke-opacity=".6"/><text x="23" y="17.5" text-anchor="middle">Go</text></g>
      <g transform="translate(95 -135)"><rect width="46" height="26" rx="13" fill="#8b5cf6" fill-opacity=".2" stroke="#8b5cf6" stroke-opacity=".7"/><text x="23" y="17.5" text-anchor="middle">TS</text></g>
      <g transform="translate(88 105)"><rect width="74" height="26" rx="13" fill="#f472b6" fill-opacity=".16" stroke="#f472b6" stroke-opacity=".6"/><text x="37" y="17.5" text-anchor="middle">Flutter</text></g>
    </g>
  </g>
  <!-- headline -->
  <text x="60" y="152" font-family="{SANS}" font-size="84" font-weight="800" letter-spacing="-2" fill="url(#name)">Rafael Tanda</text>
  <text x="64" y="196" font-family="{SANS}" font-size="17" font-weight="600" letter-spacing="5" fill="#c7d2fe">{e(role.upper())}</text>
  {ph}
  <!-- status pill -->
  <g transform="translate(64 306)">
    <rect width="{len(status)*8.2+52:.0f}" height="34" rx="17" fill="#22c55e" fill-opacity=".1" stroke="#22c55e" stroke-opacity=".45"/>
    <circle class="pulse" cx="20" cy="17" r="5" fill="#22c55e"/>
    <circle cx="20" cy="17" r="5" fill="#22c55e"/>
    <text x="36" y="22" font-family="{SANS}" font-size="14" font-weight="600" fill="#bbf7d0">{e(status)}</text>
  </g>
  <rect x=".75" y=".75" width="{W-1.5}" height="{H-1.5}" rx="21.5" fill="none" stroke="#ffffff" stroke-opacity=".1" stroke-width="1.5"/>
</g>
</svg>
'''


# ------------------------------------------------------------------ buttons
def button(name, label, c1, c2):
    W, H = 190, 52
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{e(label)}">
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient></defs>
<style>.s{{animation:sh 4s ease-in-out infinite}}@keyframes sh{{0%,60%{{transform:translateX(-80px)}}100%{{transform:translateX(280px)}}}}{REDUCE}</style>
<clipPath id="c"><rect width="{W}" height="{H}" rx="26"/></clipPath>
<g clip-path="url(#c)">
  <rect width="{W}" height="{H}" fill="url(#g)"/>
  <rect class="s" x="0" y="-10" width="36" height="80" fill="#fff" fill-opacity=".22" transform="skewX(-20)"/>
</g>
<text x="{W/2-8}" y="32" text-anchor="middle" font-family="{SANS}" font-size="17" font-weight="700" fill="#fff">{e(label)}</text>
<text x="{W/2+len(label)*5.2+4:.0f}" y="32" font-family="{SANS}" font-size="17" font-weight="700" fill="#fff" fill-opacity=".85">↗</text>
</svg>
'''


# ------------------------------------------------------------------ heading
def heading(num, title, c1, c2):
    W, H = 880, 64
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{e(title)}">
<defs>
  <linearGradient id="t" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient>
  <linearGradient id="l" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{c2}" stop-opacity=".9"/><stop offset="1" stop-color="{c2}" stop-opacity="0"/></linearGradient>
</defs>
<text x="2" y="42" font-family="{MONO}" font-size="16" font-weight="700" fill="{c1}">{num}</text>
<text x="40" y="44" font-family="{SANS}" font-size="32" font-weight="800" letter-spacing="-.5" fill="url(#t)">{e(title)}</text>
<rect x="0" y="58" width="{W}" height="2" rx="1" fill="url(#l)"/>
</svg>
'''


# --------------------------------------------------------------- about card
def about(lang, rows):
    W = 880
    H = 100 + 27 * (len(rows) + 1) + 26
    body = ""
    y = 100
    delay = 0.1

    def line(parts, y, d):
        t = f'<text class="ln" style="animation-delay:{d:.1f}s" x="34" y="{y}" font-family="{MONO}" font-size="16" xml:space="preserve">'
        for txt, col in parts:
            t += f'<tspan fill="{col}">{e(txt)}</tspan>'
        return t + "</text>\n"

    K, N, S, B, P = "#c084fc", "#7dd3fc", "#86efac", "#fda4af", "#94a3b8"
    body += line([("const ", K), ("rafael", "#fde68a"), (" = {", P)], y, delay); y += 27; delay += .15
    for key, val, kind in rows:
        parts = [("  ", P), (key, N), (": ", P)]
        if kind == "str":
            parts += [(f'"{val}"', S)]
        elif kind == "bool":
            parts += [(val, B)]
        elif kind == "arr":
            parts += [("[", P)]
            for i, v in enumerate(val):
                parts += [(f'"{v}"', S)] + ([(", ", P)] if i < len(val) - 1 else [])
            parts += [("]", P)]
        parts += [(",", P)]
        body += line(parts, y, delay); y += 27; delay += .15
    body += line([("};", P)], y, delay)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Profile summary as a code snippet">
<defs>
  <linearGradient id="bd" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#22d3ee" stop-opacity=".7"/><stop offset=".5" stop-color="#8b5cf6" stop-opacity=".6"/><stop offset="1" stop-color="#f472b6" stop-opacity=".7"/></linearGradient>
  <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0f1530"/><stop offset="1" stop-color="#0a0e22"/></linearGradient>
</defs>
<style>.ln{{opacity:0;animation:fi .5s ease-out forwards}}@keyframes fi{{from{{opacity:0;transform:translateX(-8px)}}to{{opacity:1;transform:none}}}}{REDUCE}@media (prefers-reduced-motion: reduce){{.ln{{opacity:1}}}}</style>
<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="18" fill="url(#bg)" stroke="url(#bd)" stroke-width="1.5"/>
<rect x="1" y="1" width="{W-2}" height="46" rx="18" fill="#ffffff" fill-opacity=".04"/>
<circle cx="30" cy="25" r="6" fill="#ff5f57"/><circle cx="50" cy="25" r="6" fill="#febc2e"/><circle cx="70" cy="25" r="6" fill="#28c840"/>
<text x="{W/2}" y="30" text-anchor="middle" font-family="{MONO}" font-size="13" fill="#94a3b8">rafael.ts</text>
{body}</svg>
'''


# ------------------------------------------------------------------ metrics
def metrics(tiles):
    W, H = 880, 120
    gap = 14
    tw = (W - gap * (len(tiles) - 1)) / len(tiles)
    cols = [("#22d3ee", "#3b82f6"), ("#8b5cf6", "#f472b6"), ("#34d399", "#22d3ee"), ("#fb923c", "#f472b6")]
    defs, body = "", ""
    for i, (num, lab) in enumerate(tiles):
        c1, c2 = cols[i % len(cols)]
        x = i * (tw + gap)
        defs += f'<linearGradient id="n{i}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient>'
        body += f'''<g transform="translate({x:.1f} 0)">
  <rect x=".75" y=".75" width="{tw-1.5:.1f}" height="{H-1.5}" rx="16" fill="#0d1226" stroke="{c1}" stroke-opacity=".35" stroke-width="1.5"/>
  <rect x=".75" y=".75" width="{tw-1.5:.1f}" height="{H-1.5}" rx="16" fill="url(#n{i})" fill-opacity=".07"/>
  <text x="{tw/2:.1f}" y="62" text-anchor="middle" font-family="{SANS}" font-size="44" font-weight="800" fill="url(#n{i})">{e(num)}</text>
  <text x="{tw/2:.1f}" y="92" text-anchor="middle" font-family="{SANS}" font-size="13" fill="#a5b4fc">{e(lab)}</text>
</g>
'''
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Key numbers">
<defs>{defs}</defs>
{body}</svg>
'''


# -------------------------------------------------------------------- cards
def pills(items, max_w):
    rows, cur, x = [], [], 0
    for it in items:
        w = len(it) * 7.6 + 22
        if x + w > max_w and cur:
            rows.append(cur); cur, x = [], 0
        cur.append((it, x, w)); x += w + 8
    if cur:
        rows.append(cur)
    return rows


def card_height(desc, stack):
    return 128 + 22 * len(textwrap.wrap(desc, width=50)[:5]) + 34 * len(pills(stack, 440 - 56)) + 22


def card(slug, lang, tag, metric, title, desc, stack, c1, c2, H):
    W = 440
    lines = textwrap.wrap(desc, width=50)[:5]
    prow = pills(stack, W - 56)
    d = ""
    for i, l in enumerate(lines):
        d += f'<text x="28" y="{118 + 22*i}" font-family="{SANS}" font-size="14" fill="#cbd5e1">{e(l)}</text>\n'
    py = 118 + 22 * len(lines) + 10
    p = ""
    for r, row in enumerate(prow):
        for it, x, w in row:
            p += (f'<g transform="translate({28+x:.1f} {py + 34*r})"><rect width="{w:.1f}" height="26" rx="13" fill="{c1}" fill-opacity=".12" stroke="{c1}" stroke-opacity=".45"/>'
                  f'<text x="{w/2:.1f}" y="17.5" text-anchor="middle" font-family="{MONO}" font-size="12" font-weight="600" fill="#e0e7ff">{e(it)}</text></g>\n')
    tagw = len(tag) * 8.4 + 22
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{e(title)}: {e(desc)}">
<defs>
  <linearGradient id="ac" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0f1530"/><stop offset="1" stop-color="#090d1f"/></linearGradient>
  <radialGradient id="gl" cx="1" cy="0" r="1"><stop offset="0" stop-color="{c2}" stop-opacity=".45"/><stop offset="1" stop-color="{c2}" stop-opacity="0"/></radialGradient>
  <clipPath id="cl"><rect width="{W}" height="{H}" rx="20"/></clipPath>
</defs>
<style>.gl{{animation:gl 6s ease-in-out infinite alternate}}@keyframes gl{{to{{transform:translate(-30px,20px)}}}}{REDUCE}</style>
<g clip-path="url(#cl)">
  <rect width="{W}" height="{H}" fill="url(#bg)"/>
  <circle class="gl" cx="{W}" cy="0" r="230" fill="url(#gl)"/>
  <rect width="{W}" height="4" fill="url(#ac)"/>
</g>
<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="19" fill="none" stroke="url(#ac)" stroke-opacity=".55" stroke-width="1.5"/>
<rect x="28" y="26" width="{tagw:.0f}" height="26" rx="13" fill="url(#ac)" fill-opacity=".16" stroke="{c1}" stroke-opacity=".5"/>
<text x="{28+tagw/2:.0f}" y="43.5" text-anchor="middle" font-family="{MONO}" font-size="12" font-weight="700" letter-spacing="1" fill="{c1}">{e(tag)}</text>
<text x="{W-28}" y="43.5" text-anchor="end" font-family="{MONO}" font-size="12" fill="#94a3b8">{e(metric)}</text>
<text x="28" y="92" font-family="{SANS}" font-size="27" font-weight="800" letter-spacing="-.5" fill="url(#ac)">{e(title)}</text>
{d}{p}</svg>
'''


# ------------------------------------------------------------------- stack
def stack(rows):
    W = 880
    palette = ["#22d3ee", "#8b5cf6", "#f472b6", "#34d399", "#fb923c"]
    y = 34
    body = ""
    for gi, (label, items) in enumerate(rows):
        col = palette[gi % len(palette)]
        prow = pills(items, W - 220)
        body += f'<text x="28" y="{y+17}" font-family="{MONO}" font-size="13" font-weight="700" fill="{col}">{e(label)}</text>\n'
        for r, row in enumerate(prow):
            for it, x, w in row:
                body += (f'<g transform="translate({190+x:.1f} {y + 32*r})"><rect width="{w:.1f}" height="26" rx="13" fill="{col}" fill-opacity=".13" stroke="{col}" stroke-opacity=".5"/>'
                         f'<text x="{w/2:.1f}" y="17.5" text-anchor="middle" font-family="{MONO}" font-size="12" font-weight="600" fill="#e0e7ff">{e(it)}</text></g>\n')
        y += 32 * len(prow) + 16
    H = y + 14
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Tech stack">
<defs><linearGradient id="bd" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#22d3ee" stop-opacity=".5"/><stop offset="1" stop-color="#f472b6" stop-opacity=".5"/></linearGradient></defs>
<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="18" fill="#0b1024" stroke="url(#bd)" stroke-width="1.5"/>
{body}</svg>
'''


# ------------------------------------------------------------------ footer
def footer(text):
    W, H = 1000, 150

    def wave(period, amp, reps):
        d = "M0 70 "
        for i in range(reps):
            x = i * period
            d += f"C {x+period*.25:.0f} {70-amp}, {x+period*.75:.0f} {70+amp}, {x+period} 70 "
        return d + f"V150 H0 Z"

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{e(text)}">
<defs>
  <linearGradient id="w1" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#22d3ee"/><stop offset=".5" stop-color="#8b5cf6"/><stop offset="1" stop-color="#f472b6"/></linearGradient>
</defs>
<style>.w{{animation:mv 16s linear infinite}}.w2{{animation:mv2 26s linear infinite}}@keyframes mv{{to{{transform:translateX(-500px)}}}}@keyframes mv2{{from{{transform:translateX(-1000px)}}to{{transform:translateX(0)}}}}{REDUCE}</style>
<g class="w2" opacity=".35"><path d="{wave(1000, 36, 3)}" fill="url(#w1)"/></g>
<g class="w" opacity=".9"><path d="{wave(500, 30, 4)}" fill="url(#w1)"/></g>
<text x="{W/2}" y="118" text-anchor="middle" font-family="{SANS}" font-size="20" font-weight="700" fill="#0b1020">{e(text)}</text>
</svg>
'''


# -------------------------------------------------------------------- build
L = {
    "en": dict(
        phrases=["Real products, end to end", "Go · TypeScript · Flutter", "AI agents + tests on every change"],
        role="Full-Stack Software Engineer", status="Open to remote & on-site roles",
        label="Rafael Tanda — Full-Stack Software Engineer",
        h_about="About me", h_nums="By the numbers", h_work="Featured work", h_stack="Tech stack",
        about=[("role", "Full-Stack Software Engineer", "str"), ("based", "Havana, Cuba", "str"),
               ("studying", "Computer Science @ UCI", "str"), ("stack", ["Go", "TypeScript", "Flutter"], "arr"),
               ("workflow", "AI agents in the loop + tests + review", "str"), ("openToWork", "true", "bool")],
        nums=[("276", "test files in chatapp"), ("7", "Docker services in chatapp"),
              ("100%", "offline-first salon app"), ("147", "commits in salon-saas")],
        cards=[
            ("chatapp", "WEB · REAL-TIME", "275 commits", "chatapp",
             "Real-time messaging platform: offline-capable PWA, 1:1 and group chat, Web Push, voice and video calls, with unit, integration and e2e tests in CI.",
             ["Go", "Gin", "React 19", "PostgreSQL", "Redis", "MinIO", "WebSockets", "Docker"], "#22d3ee", "#3b82f6"),
            ("salon-saas", "WEB · SAAS", "147 commits", "salon-saas",
             "Multi-tenant SaaS for salons: DB-enforced no-overlap bookings, clients with photos, POS and cash close, real-time notifications, offline-first PWA.",
             ["Go", "Gin", "React 18", "TypeScript", "PostgreSQL", "WebSockets", "Docker"], "#8b5cf6", "#f472b6"),
            ("gestion-salon", "MOBILE · ANDROID + IOS", "offline-first", "gestion-salon",
             "Mobile app for a real beauty salon: income, expenses, clients, appointments with reminders, PDF/CSV reports and backup. No backend.",
             ["Flutter", "Dart", "SQLite", "Provider"], "#34d399", "#22d3ee"),
            ("portfolio", "WEB · STATIC SITE", "on Vercel", "portfolio",
             "My personal site and bilingual CV: case studies, tech stack and downloadable PDFs, built as a fast static site.",
             ["Astro", "TypeScript", "Vercel"], "#fb923c", "#f472b6"),
        ],
        stack=[("Languages", ["Go", "TypeScript", "Python", "Dart", "GDScript", "Java"]),
               ("Backend & data", ["Gin", "REST", "WebSockets", "PostgreSQL", "Redis", "SQLite", "MinIO (S3)"]),
               ("Clients", ["React 19", "PWA", "Flutter", "Godot 4"]),
               ("Quality & delivery", ["go test", "Playwright", "pytest", "GitHub Actions", "Docker Compose", "Nginx", "Caddy"]),
               ("AI tooling", ["Claude Code", "opencode", "MCP", "agent skills & hooks", "spec-driven dev"])],
        footer="Thanks for stopping by",
    ),
    "es": dict(
        phrases=["Productos reales, de punta a punta", "Go · TypeScript · Flutter", "Agentes de IA + pruebas en cada cambio"],
        role="Ingeniero de Software Full-Stack", status="Abierto a roles remotos y presenciales",
        label="Rafael Tanda — Ingeniero de Software Full-Stack",
        h_about="Sobre mí", h_nums="En números", h_work="Proyectos destacados", h_stack="Stack tecnológico",
        about=[("rol", "Ingeniero de Software Full-Stack", "str"), ("ubicacion", "La Habana, Cuba", "str"),
               ("estudia", "Ciencias Informáticas @ UCI", "str"), ("stack", ["Go", "TypeScript", "Flutter"], "arr"),
               ("metodo", "Agentes de IA + pruebas + revisión", "str"), ("abiertoATrabajo", "true", "bool")],
        nums=[("276", "archivos de prueba en chatapp"), ("7", "servicios Docker en chatapp"),
              ("100%", "app de salón offline-first"), ("147", "commits en salon-saas")],
        cards=[
            ("chatapp", "WEB · TIEMPO REAL", "275 commits", "chatapp",
             "Plataforma de mensajería en tiempo real: PWA offline, chat 1:1 y grupal, Web Push, llamadas de voz y video, con pruebas unitarias, de integración y e2e en CI.",
             ["Go", "Gin", "React 19", "PostgreSQL", "Redis", "MinIO", "WebSockets", "Docker"], "#22d3ee", "#3b82f6"),
            ("salon-saas", "WEB · SAAS", "147 commits", "salon-saas",
             "SaaS multi-tenant para salones: reservas sin solape garantizadas por la base de datos, clientes con fotos, POS y cierre de caja, notificaciones en tiempo real, PWA offline-first.",
             ["Go", "Gin", "React 18", "TypeScript", "PostgreSQL", "WebSockets", "Docker"], "#8b5cf6", "#f472b6"),
            ("gestion-salon", "MÓVIL · ANDROID + IOS", "offline-first", "gestion-salon",
             "App móvil para una peluquería real: ingresos, gastos, clientes, citas con recordatorios, reportes PDF/CSV y respaldo. Sin backend.",
             ["Flutter", "Dart", "SQLite", "Provider"], "#34d399", "#22d3ee"),
            ("portfolio", "WEB · SITIO ESTÁTICO", "en Vercel", "portfolio",
             "Mi sitio personal y CV bilingüe: casos de estudio, stack y PDFs descargables, hecho como sitio estático rápido.",
             ["Astro", "TypeScript", "Vercel"], "#fb923c", "#f472b6"),
        ],
        stack=[("Lenguajes", ["Go", "TypeScript", "Python", "Dart", "GDScript", "Java"]),
               ("Backend y datos", ["Gin", "REST", "WebSockets", "PostgreSQL", "Redis", "SQLite", "MinIO (S3)"]),
               ("Clientes", ["React 19", "PWA", "Flutter", "Godot 4"]),
               ("Calidad y entrega", ["go test", "Playwright", "pytest", "GitHub Actions", "Docker Compose", "Nginx", "Caddy"]),
               ("Herramientas de IA", ["Claude Code", "opencode", "MCP", "skills y hooks", "desarrollo por specs"])],
        footer="Gracias por pasar",
    ),
}

for name, label, c1, c2 in [
    ("btn-portfolio", "Portfolio", "#2f81f7", "#8b5cf6"),
    ("btn-linkedin", "LinkedIn", "#0a66c2", "#3b9dff"),
    ("btn-instagram", "Instagram", "#f58529", "#dd2a7b"),
    ("btn-email", "Email", "#ea4335", "#fb923c"),
]:
    write(f"{name}.svg", button(name, label, c1, c2))

for lang, d in L.items():
    write(f"hero-{lang}.svg", hero(lang, d["phrases"], d["role"], d["status"], d["label"]))
    write(f"h-about-{lang}.svg", heading("01", d["h_about"], "#22d3ee", "#3b82f6"))
    write(f"h-work-{lang}.svg", heading("02", d["h_work"], "#8b5cf6", "#f472b6"))
    write(f"h-stack-{lang}.svg", heading("03", d["h_stack"], "#34d399", "#22d3ee"))
    write(f"about-{lang}.svg", about(lang, d["about"]))
    write(f"metrics-{lang}.svg", metrics(d["nums"]))
    write(f"stack-{lang}.svg", stack(d["stack"]))
    write(f"footer-{lang}.svg", footer(d["footer"]))
    ch = max(card_height(c[4], c[5]) for c in d["cards"])
    for slug, tag, metric, title, desc, st, c1, c2 in d["cards"]:
        write(f"card-{slug}-{lang}.svg", card(slug, lang, tag, metric, title, desc, st, c1, c2, ch))

print("assets:", len(os.listdir(OUT)))
