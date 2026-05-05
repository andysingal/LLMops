[browser-harness](https://www.opensourceprojects.dev/post/732c1ccf-a367-41e8-ad5e-5cf20b682788)

```
Getting started is straightforward:

1. Clone the repo:
git clone https://github.com/browser-use/browser-harness
2. Install dependencies:
cd browser-harness && npm install
(or your preferred package manager)
3. Set your LLM API key in a
.env
file
4. Run a task:
node index.js --task "Find the cheapest flights from NYC to London next Friday"
```
[donutbrowser](https://github.com/zhom/donutbrowser)

- Unlimited browser profiles — each fully isolated with its own fingerprint, cookies, extensions, and data
- Chromium & Firefox engines — Chromium powered by Wayfern, Firefox powered by Camoufox, both with advanced fingerprint spoofing
- Proxy support — HTTP, HTTPS, SOCKS4, SOCKS5 per profile, with dynamic proxy URLs
- VPN support — WireGuard configs per profile
- Local API & MCP — REST API and Model Context Protocol server for integration with Claude, automation tools, and custom workflows
- Profile groups — organize profiles and apply bulk settings
- Import profiles — migrate from Chrome, Firefox, Edge, Brave, or other Chromium browsers
- Cookie & extension management — import/export cookies, manage extensions per profile
- Default browser — set Donut as your default browser and choose which profile opens each link
- Cloud sync — sync profiles, proxies, and groups across devices (self-hostable)
- E2E encryption — optional end-to-end encrypted sync with a password only you know
- Zero telemetry — no tracking or device fingerprinting
