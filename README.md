# Santhosh M K

Full-stack developer building AI agents, MCP servers, web scrapers, and edge applications. I turn messy public web data into products people can use, and I ship them on Cloudflare Workers, Python, and TypeScript.

[LinkedIn](https://www.linkedin.com/in/santhosh-m-k) | [LeetCode](https://leetcode.com/u/santhoshmk) | [Email](mailto:devsanthoshmk@gmail.com)

## What I work on

- AI agents and Model Context Protocol servers that call real tools.
- Scrapers for Google Maps, LinkedIn, and marketplaces, with export to Excel, CSV, and JSON.
- Edge services on Cloudflare Workers with D1, KV, and R2.
- Business apps for billing, retail, food ordering, and lead generation.

## Featured projects

- **[gmaps-mcp](https://github.com/devsanthoshmk/gmaps-mcp)**. Google Maps search and place details for AI agents, with no API key and no billing account. Python, MCP, aiohttp.
- **[wrangler-wrapper](https://github.com/devsanthoshmk/wrangler-wrapper)**. Switch Cloudflare Wrangler accounts and profiles with one command, with isolated OAuth sessions. Node.js, zero dependencies.
- **[cloudflaredjs](https://github.com/devsanthoshmk/cloudflaredjs)**. Persistent Cloudflare Quick Tunnels in Node, with automatic rotation when the tunnel drops. Node.js.
- **[m14u-workers-v4](https://github.com/devsanthoshmk/m14u-workers-v4)**. Edge audio streaming on Cloudflare Workers with sub-5ms sync for listen-along rooms. TypeScript, React, Kotlin.
- **[leadgen-basic](https://github.com/devsanthoshmk/leadgen-basic)**. Client-side lead generation for Google Maps with spreadsheet export, 1000+ requests in under a minute. Vue, Ionic, Capacitor.
- **[billing-software](https://github.com/devsanthoshmk/billing-software)**. Pharmaceutical wholesale POS with GST, batch expiry control, and 554 tests. Next.js, TypeScript, SQLite.

## AI agents and MCP servers

| Project | What it does | Stack |
| --- | --- | --- |
| [gmaps-mcp](https://github.com/devsanthoshmk/gmaps-mcp) | Google Maps tools for AI agents with stdio and HTTP transports | Python, MCP |
| [AgenticragChatbot](https://github.com/devsanthoshmk/AgenticragChatbot) | Agentic RAG chatbot with crawler, graph chunks, and citations | LangChain, Qdrant, Postgres |
| [skills](https://github.com/devsanthoshmk/skills) | Reusable skills for OpenCode, OpenChamber, and CLI agents | Markdown, YAML |
| [agy-subagent](https://github.com/devsanthoshmk/agy-subagent) | Headless subagents for terminal tasks through the Antigravity CLI | Bash, Markdown |
| [doc-gen](https://github.com/devsanthoshmk/doc-gen) | Generate DOCX documents from templates and plain text with an LLM | TypeScript, Hono, LangChain |
| [project-file-upload](https://github.com/devsanthoshmk/project-file-upload) | Upload an image and classify it as real or deepfake | Flask, PyTorch, ViT |
| [drug-classifier](https://github.com/devsanthoshmk/drug-classifier) | Predict drug pair viability from element properties and describe it | scikit-learn, TinyLlama |
| [nm-project](https://github.com/devsanthoshmk/nm-project) | Speech recognition on LibriSpeech with MFCC features and LSTMs | TensorFlow, Librosa |

## Scrapers and lead generation

| Project | What it does | Stack |
| --- | --- | --- |
| [gmapScraper](https://github.com/devsanthoshmk/gmapScraper) | Google Maps business extraction with website enrichment and lead scores | Python, aiohttp |
| [mapScraper-forked](https://github.com/devsanthoshmk/mapScraper-forked) | Maps scraper with an async /places fallback for missing contact data | Python, lxml |
| [mapScraper.js](https://github.com/devsanthoshmk/mapScraper.js) | Node.js Maps scraper with CSV export and concurrency limits | Node.js, JSDOM |
| [leadgen](https://github.com/devsanthoshmk/leadgen) | Multi-source B2B prospect finder with AI gap filling | Python, Flask, React |
| [leadgen-basic](https://github.com/devsanthoshmk/leadgen-basic) | On-device lead generation for Android, iOS, and web | Vue, Ionic, Capacitor |
| [linkedin-companies-scraper.js](https://github.com/devsanthoshmk/linkedin-companies-scraper.js) | LinkedIn company search through the Voyager GraphQL API | Node.js, Playwright |
| [linkedin-companies-scraper.py](https://github.com/devsanthoshmk/linkedin-companies-scraper.py) | Python port with session refresh and geo resolution | Python, curl-cffi |
| [places-data](https://github.com/devsanthoshmk/places-data) | Browser scraper that exports Maps listings to Excel | Vue, Vite |
| [places-data-app](https://github.com/devsanthoshmk/places-data-app) | Mobile places viewer with background scraping and XLSX export | Vue, Capacitor |
| [places-data-desktop](https://github.com/devsanthoshmk/places-data-desktop) | Desktop places scraper with native HTTP and phone normalization | Tauri, Vue, Rust |
| [map_project](https://github.com/devsanthoshmk/map_project) | Desktop Maps scraper with GUI and multiprocess Selenium | Python, CustomTkinter |
| [gmap-project](https://github.com/devsanthoshmk/gmap-project) | Flask and Vue app for Maps extraction to spreadsheets | Python, Vue |
| [map-project-final](https://github.com/devsanthoshmk/map-project-final) | Multi-core Selenium scraper that races browser sessions | Python, Selenium |
| [Project-best-product-finder](https://github.com/devsanthoshmk/Project-best-product-finder) | Compare Flipkart and Amazon listings with Gemini review scores | Python, Gemini |
| [telegtram-bot](https://github.com/devsanthoshmk/telegtram-bot) | Telegram bot that returns Maps search results as an Excel file | Python, pyTelegramBotAPI |

## Cloudflare and edge infrastructure

| Project | What it does | Stack |
| --- | --- | --- |
| [wrangler-wrapper](https://github.com/devsanthoshmk/wrangler-wrapper) | Multi-account Wrangler profiles with instant switching | Node.js |
| [cloudflaredjs](https://github.com/devsanthoshmk/cloudflaredjs) | Quick tunnel manager with health checks and rotation | Node.js |
| [m14u-workers-v4](https://github.com/devsanthoshmk/m14u-workers-v4) | Edge audio API and synced playback server | Workers, React |
| [kv-storage](https://github.com/devsanthoshmk/kv-storage) | HTTP key-value API on Workers KV with CORS and error contracts | Workers, TypeScript |
| [searchres-worker](https://github.com/devsanthoshmk/searchres-worker) | DuckDuckGo web and image search proxy without a headless browser | Workers, TypeScript |
| [no_socket_proxy](https://github.com/devsanthoshmk/no_socket_proxy) | HTTP streaming proxy with dynamic routes in KV | Workers, JavaScript |
| [cors-proxy](https://github.com/devsanthoshmk/cors-proxy) | CORS proxy for browser requests to third-party endpoints | Python, Bottle |
| [whatsapp-cloudflare-dashboard](https://github.com/devsanthoshmk/whatsapp-cloudflare-dashboard) | WhatsApp webhook console with service window and storage guards | Workers, D1, R2 |
| [techx-club](https://github.com/devsanthoshmk/techx-club) | Real-time quiz buzzer with clock sync and tunnel routing | Socket.IO, Vue, Cloudflare |

## Commerce and web applications

| Project | What it does | Stack |
| --- | --- | --- |
| [billing-software](https://github.com/devsanthoshmk/billing-software) | Pharma wholesale POS with GST, FEFO stock, and receipts | Next.js, TypeScript |
| [spacefurnio](https://github.com/devsanthoshmk/spacefurnio) | Furniture catalog with filters, cart, and admin portal | Vue, Neon, Workers |
| [MKS-Agency](https://github.com/devsanthoshmk/MKS-Agency) | Herbal wellness store with manual payment verification | Vue, Convex |
| [thivanacollections](https://github.com/devsanthoshmk/thivanacollections) | Clothing store with Supabase auth and Razorpay checkout | Vue, Supabase |
| [MS-Kichen](https://github.com/devsanthoshmk/MS-Kichen) | Restaurant ordering frontend with live admin dashboard | Vue, Express, SQLite |
| [wcff](https://github.com/devsanthoshmk/wcff) | Agency site and internship registration with email OTP | Vue, Express, Supabase |
| [wcff-internreg](https://github.com/devsanthoshmk/wcff-internreg) | Internship application portal with a CRUD API | Node.js, PostgreSQL |
| [dudemw](https://github.com/devsanthoshmk/dudemw) | Menswear storefront and admin dashboard | Next.js, Prisma |
| [oldskool-template](https://github.com/devsanthoshmk/oldskool-template) | Store template for Eleventy and Django with 10 layouts | Eleventy, Django |
| [pos-SuperMarket](https://github.com/devsanthoshmk/pos-SuperMarket) | Supermarket POS with inventory edits and sales charts | Python, Eel |
| [pos-for-teashop](https://github.com/devsanthoshmk/pos-for-teashop) | Tea shop POS with thermal receipts and analytics | Python, Eel |
| [whole-foods](https://github.com/devsanthoshmk/whole-foods) | Conversational grocery store with inventory locks | React, Workers, Gemini |

## Media, tools, and browser extensions

| Project | What it does | Stack |
| --- | --- | --- |
| [M14U-js](https://github.com/devsanthoshmk/M14U-js) | YouTube Music client with listen-along rooms and synced lyrics | React, Express |
| [M14U-in-vuejs](https://github.com/devsanthoshmk/M14U-in-vuejs) | Vue music player on a Flask extraction backend | Vue, Flask |
| [m14u-python-backend](https://github.com/devsanthoshmk/m14u-python-backend) | YouTube Music search and stream URL API | Flask, yt-dlp |
| [ytm-client](https://github.com/devsanthoshmk/ytm-client) | Self-hosted music player with QR access on the local network | Flask, Vue |
| [home360](https://github.com/devsanthoshmk/home360) | 360 degree real estate tour viewer with room hotspots | Pannellum, Vite |
| [VideoCrafter-googlecolab](https://github.com/devsanthoshmk/VideoCrafter-googlecolab) | Colab notebook for text to video generation | Python, PyTorch |
| [WA-automation](https://github.com/devsanthoshmk/WA-automation) | Scheduled WhatsApp broadcasts with rate limits and resume | Node.js, whatsapp-web.js |
| [insta-memory-fix-extension](https://github.com/devsanthoshmk/insta-memory-fix-extension) | Unmount off-screen reels to cut Instagram RAM use | Chrome MV3 |
| [InstaDe-tox](https://github.com/devsanthoshmk/InstaDe-tox) | Block reels and explore feeds on Instagram web | Chrome MV2 |
| [profit-hunt-ext](https://github.com/devsanthoshmk/profit-hunt-ext) | Evaluate paper trading rules on Neostox tables | Chrome MV3 |
| [Make_vCard-web](https://github.com/devsanthoshmk/Make_vCard-web) | Spreadsheet to vCard converter, live at make-vcard.sanpro.workers.dev | JavaScript, Workers |
| [Make_vCard](https://github.com/devsanthoshmk/Make_vCard) | Python CLI and BeeWare app for vCard export | Python, Toga |
| [Playwright](https://github.com/devsanthoshmk/Playwright) | Benchmarks for sync and async browser automation | Python, Playwright |
| [NM-HELPER](https://github.com/devsanthoshmk/NM-HELPER) | Batch file helper for Termux storage | Python |
| [NM-Automation](https://github.com/devsanthoshmk/NM-Automation) | Queue runner for SCORM course modules in Chromium | Python, Playwright |
| [auto-storage-cleanner](https://github.com/devsanthoshmk/auto-storage-cleanner) | Find files older than 90 days on Android storage | Python |
| [main](https://github.com/devsanthoshmk/main) | Driver for a PAW3204DB optical mouse sensor on ATmega328P | C++, PlatformIO |
| [pen-proj](https://github.com/devsanthoshmk/pen-proj) | Digital pen design for plain paper with BLE streaming | Embedded C, React Native |
| [dsa-journey](https://github.com/devsanthoshmk/dsa-journey) | Data structures and algorithms practice tracker | Markdown |
| [chess-history-project](https://github.com/devsanthoshmk/chess-history-project) | Chess history explorer with PGN import and branching moves | React, chess.js |

## Stack

Python, TypeScript, JavaScript, Vue, React, Next.js, Node.js, Flask, Cloudflare Workers, D1, KV, R2, PostgreSQL, SQLite, Supabase, Convex, LangChain, MCP, Playwright, Selenium, Docker.

## Contact

Open to work on AI tooling, scraping pipelines, and edge applications. Reach me on [LinkedIn](https://www.linkedin.com/in/santhosh-m-k) or by [email](mailto:devsanthoshmk@gmail.com).
