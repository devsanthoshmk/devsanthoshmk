#!/usr/bin/env python3
"""
Pure Native SVG Generator for GitHub Profile Terminal Card.
100% compatible with GitHub Camo Proxy (no foreignObject).
"""

import os

ASCII_ART = [
    "               .:::.               ",
    "            .:'     ':.            ",
    "          .'           '.          ",
    "         /   .--------.  \\         ",
    "        :   /  ______  \\  :        ",
    "       :   :  | 01  10 |  :  :       ",
    "       |   |  | DEVELOP|  |  |       ",
    "       |   |  |________|  |  |       ",
    "       :   :  [SYSTEM] :  :       ",
    "        :   \\  ======  /  :        ",
    "         \\   '--------'  /         ",
    "        .::'.   ||||   .'::.       ",
    "     .-'    '---''''---'    '-.    ",
    "   .'   .----------------.   '.   ",
    "  /    /  AI CORE // 01   \\    \\  ",
    " :    :  ================  :    : ",
    " |    |  > AGENTIC SYSTEMS |    | ",
    " |    |  > MCP PROTOCOLS   |    | ",
    " |    |  > HIGH THROUGHPUT |    | ",
    " |    |  > CLOUD RUNTIMES  |    | ",
    " :    :  ================  :    : ",
    "  \\    \\  NEURAL ENGINE  /    /  ",
    "   '.   '----------------'   .'   ",
    "     '-.                  .-'     ",
    "       |  .------------.  |       ",
    "       |  | 0101010101 |  |       ",
    "       |  '------------'  |       ",
    "       '------------------'       ",
    "      [ STATUS: OPERATIONAL ]     ",
]

ROWS = [
    ("USER", "SANTHOSH M K", True, "#f8fafc"),
    ("ROLE", "Full-Stack & Agentic AI Engineer", True, "#38bdf8"),
    ("FOCUS", "Autonomous Agents, MCP Servers, Distributed APIs", False, "#cbd5e1"),
    ("TOOLCHAIN", "Linux (Arch), Docker, Git, VS Code, agy CLI", False, "#cbd5e1"),
    ("LANGUAGES", "Python, TypeScript, JavaScript, Go, C++, SQL", False, "#cbd5e1"),
    ("FRONTEND", "React, Next.js, Vue.js, Ionic, Tailwind CSS", False, "#cbd5e1"),
    ("BACKEND", "FastAPI, Node.js, Express, Cloudflare Workers", False, "#cbd5e1"),
    ("DATA &amp; AI", "LangChain, Qdrant, Neon Postgres, Redis, Groq", False, "#cbd5e1"),
    ("SCRAPING", "Playwright, Puppeteer, High-Volume Data Pipelines", False, "#cbd5e1"),
    ("PORTFOLIO", "78 Repositories • Open Source Systems", True, "#22c55e"),
]

def generate_dark_svg():
    ascii_svg = ""
    start_y = 82
    line_step = 11.5
    for i, line in enumerate(ASCII_ART):
        y = start_y + (i * line_step)
        escaped = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        ascii_svg += f'    <text x="182" y="{y:.1f}" text-anchor="middle" fill="#38bdf8" font-weight="600">{escaped}</text>\n'

    rows_svg = ""
    start_row_y = 112
    row_step = 26
    for i, (label, val, bold, color) in enumerate(ROWS):
        y = start_row_y + (i * row_step)
        weight = "700" if bold else "500"
        escaped_val = val.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        rows_svg += f"""    <text x="390" y="{y}" fill="#06b6d4" font-weight="700" letter-spacing="0.4">{label}</text>
    <text x="500" y="{y}" fill="{color}" font-weight="{weight}">{escaped_val}</text>\n"""

    svg = f"""<svg width="880" height="440" viewBox="0 0 880 440" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="darkBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080c14" />
      <stop offset="100%" stop-color="#0b1324" />
    </linearGradient>
    <linearGradient id="laserGlowDark" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0" />
      <stop offset="50%" stop-color="#38bdf8" stop-opacity="0.85" />
      <stop offset="100%" stop-color="#38bdf8" stop-opacity="0" />
    </linearGradient>
    <filter id="neonGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <style>
    .mono {{ font-family: 'JetBrains Mono', 'Fira Code', 'Cascadia Code', 'SF Mono', Consolas, Menlo, monospace; }}
    .ascii-text {{ font-size: 9.2px; }}
    .row-text {{ font-size: 11.5px; }}
  </style>

  <!-- Outer Window -->
  <rect x="1" y="1" width="878" height="438" rx="14" fill="url(#darkBg)" stroke="#1e293b" stroke-width="1.5" />
  
  <!-- Header Bar -->
  <path d="M1 15C1 7.26801 7.26801 1 15 1H865C872.732 1 879 7.26801 879 15V42H1V15Z" fill="#0d1527" stroke="#1e293b" stroke-width="1" />
  
  <!-- Window Dots -->
  <circle cx="25" cy="21" r="6" fill="#ff5f56" />
  <circle cx="45" cy="21" r="6" fill="#ffbd2e" />
  <circle cx="65" cy="21" r="6" fill="#27c93f" />

  <!-- Title -->
  <text x="440" y="26" text-anchor="middle" fill="#94a3b8" font-size="12.5" font-weight="500" class="mono">devsanthoshmk@terminal:~ (zsh)</text>

  <!-- Status Badge -->
  <rect x="760" y="11" width="102" height="21" rx="6" fill="#38bdf8" fill-opacity="0.1" stroke="#38bdf8" stroke-opacity="0.3" stroke-width="1" />
  <text x="811" y="25" text-anchor="middle" fill="#38bdf8" font-size="10.5" font-weight="700" class="mono">LIVE SYSTEM</text>

  <!-- Column Divider -->
  <line x1="365" y1="52" x2="365" y2="422" stroke="#1e293b" stroke-width="1.2" />

  <!-- Scanline Animation -->
  <g>
    <rect x="2" y="43" width="876" height="3" fill="url(#laserGlowDark)">
      <animate attributeName="y" values="43;425;43" dur="6s" repeatCount="indefinite" />
      <animate attributeName="opacity" values="0.1;0.9;0.9;0.1" dur="6s" repeatCount="indefinite" />
    </rect>
  </g>

  <!-- Left Panel: ASCII Art -->
  <g class="mono ascii-text" filter="url(#neonGlow)">
{ascii_svg}  </g>

  <!-- Right Panel: Terminal Prompt & Info Table -->
  <g class="mono">
    <!-- Prompt -->
    <text x="390" y="76" font-size="12.5">
      <tspan fill="#22c55e" font-weight="700">devsanthoshmk@archlinux</tspan><tspan fill="#64748b">:</tspan><tspan fill="#38bdf8">~</tspan><tspan fill="#f1f5f9">$ neofetch --system-info</tspan>
    </text>

    <!-- Table Rows -->
    <g class="row-text">
{rows_svg}    </g>

    <!-- Footer Note -->
    <line x1="390" y1="388" x2="855" y2="388" stroke="#1e293b" stroke-dasharray="4 4" stroke-width="1" />
    <text x="390" y="412" fill="#64748b" font-size="11">&gt; Live GitHub metrics, architectures &amp; source code below ↓</text>
  </g>
</svg>"""
    return svg

def generate_light_svg():
    ascii_svg = ""
    start_y = 82
    line_step = 11.5
    for i, line in enumerate(ASCII_ART):
        y = start_y + (i * line_step)
        escaped = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        ascii_svg += f'    <text x="182" y="{y:.1f}" text-anchor="middle" fill="#0284c7" font-weight="600">{escaped}</text>\n'

    rows_svg = ""
    start_row_y = 112
    row_step = 26
    for i, (label, val, bold, color) in enumerate(ROWS):
        y = start_row_y + (i * row_step)
        light_color = "#0f172a" if bold else "#334155"
        if label == "PORTFOLIO":
            light_color = "#16a34a"
        elif label == "ROLE":
            light_color = "#0284c7"
        weight = "700" if bold else "500"
        escaped_val = val.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        rows_svg += f"""    <text x="390" y="{y}" fill="#0369a1" font-weight="700" letter-spacing="0.4">{label}</text>
    <text x="500" y="{y}" fill="{light_color}" font-weight="{weight}">{escaped_val}</text>\n"""

    svg = f"""<svg width="880" height="440" viewBox="0 0 880 440" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="lightBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" />
      <stop offset="100%" stop-color="#f8fafc" />
    </linearGradient>
    <linearGradient id="laserGlowLight" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0284c7" stop-opacity="0" />
      <stop offset="50%" stop-color="#0284c7" stop-opacity="0.6" />
      <stop offset="100%" stop-color="#0284c7" stop-opacity="0" />
    </linearGradient>
  </defs>

  <style>
    .mono {{ font-family: 'JetBrains Mono', 'Fira Code', 'Cascadia Code', 'SF Mono', Consolas, Menlo, monospace; }}
    .ascii-text {{ font-size: 9.2px; }}
    .row-text {{ font-size: 11.5px; }}
  </style>

  <!-- Outer Window -->
  <rect x="1" y="1" width="878" height="438" rx="14" fill="url(#lightBg)" stroke="#cbd5e1" stroke-width="1.5" />
  
  <!-- Header Bar -->
  <path d="M1 15C1 7.26801 7.26801 1 15 1H865C872.732 1 879 7.26801 879 15V42H1V15Z" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1" />
  
  <!-- Window Dots -->
  <circle cx="25" cy="21" r="6" fill="#ef4444" />
  <circle cx="45" cy="21" r="6" fill="#f59e0b" />
  <circle cx="65" cy="21" r="6" fill="#10b981" />

  <!-- Title -->
  <text x="440" y="26" text-anchor="middle" fill="#475569" font-size="12.5" font-weight="500" class="mono">devsanthoshmk@terminal:~ (zsh)</text>

  <!-- Status Badge -->
  <rect x="760" y="11" width="102" height="21" rx="6" fill="#0284c7" fill-opacity="0.1" stroke="#0284c7" stroke-opacity="0.3" stroke-width="1" />
  <text x="811" y="25" text-anchor="middle" fill="#0284c7" font-size="10.5" font-weight="700" class="mono">LIVE SYSTEM</text>

  <!-- Column Divider -->
  <line x1="365" y1="52" x2="365" y2="422" stroke="#e2e8f0" stroke-width="1.2" />

  <!-- Scanline Animation -->
  <g>
    <rect x="2" y="43" width="876" height="2" fill="url(#laserGlowLight)">
      <animate attributeName="y" values="43;425;43" dur="6s" repeatCount="indefinite" />
      <animate attributeName="opacity" values="0.1;0.8;0.8;0.1" dur="6s" repeatCount="indefinite" />
    </rect>
  </g>

  <!-- Left Panel: ASCII Art -->
  <g class="mono ascii-text">
{ascii_svg}  </g>

  <!-- Right Panel: Terminal Prompt & Info Table -->
  <g class="mono">
    <!-- Prompt -->
    <text x="390" y="76" font-size="12.5">
      <tspan fill="#16a34a" font-weight="700">devsanthoshmk@archlinux</tspan><tspan fill="#64748b">:</tspan><tspan fill="#0284c7">~</tspan><tspan fill="#0f172a">$ neofetch --system-info</tspan>
    </text>

    <!-- Table Rows -->
    <g class="row-text">
{rows_svg}    </g>

    <!-- Footer Note -->
    <line x1="390" y1="388" x2="855" y2="388" stroke="#cbd5e1" stroke-dasharray="4 4" stroke-width="1" />
    <text x="390" y="412" fill="#64748b" font-size="11">&gt; Live GitHub metrics, architectures &amp; source code below ↓</text>
  </g>
</svg>"""
    return svg

def main():
    target_dir = os.path.dirname(os.path.abspath(__file__))
    dark_path = os.path.join(target_dir, "dark.svg")
    light_path = os.path.join(target_dir, "light.svg")

    with open(dark_path, "w", encoding="utf-8") as f:
        f.write(generate_dark_svg())
    print(f"Generated: {dark_path}")

    with open(light_path, "w", encoding="utf-8") as f:
        f.write(generate_light_svg())
    print(f"Generated: {light_path}")

if __name__ == "__main__":
    main()
