# J.A.R.V.I.S. — Web Interface

A sleek, single-page chat interface for an OpenAI-compatible AI backend. Inspired by the Arc Reactor / HUD aesthetic.

## Features

- **Streaming responses** — tokens appear in real-time as the model generates them
- **Markdown rendering** — code blocks, lists, headers, links, blockquotes
- **Text-to-speech (TTS)** — browser-native speech synthesis, optional auto-speak
- **Voice input** — Web Speech API microphone recording
- **File drop** — drag text files into the drop zone
- **Fullscreen mode** — hides chrome, full immersion
- **Persistent chat** — messages saved to `localStorage`
- **Settings panel** — Server URL, API endpoint, metrics URL, model, TTS voice/rate/pitch, toggles
- **System status panel** — connection health, server latency, system metrics
- **Clear chat** — reset conversation and local storage

## Requirements

- Any modern browser (Chrome, Firefox, Edge, Safari)
- An OpenAI-compatible API endpoint running on a server reachable from the browser
- The server must have CORS enabled (or be served from the same origin)

## Quick Start

1. Open `jarvis.html` in a browser (double-click, or serve it from any web server)
2. Open **Settings** (⚙) and configure:
   - **Server URL** — The address of your AI server (e.g. `http://192.168.55.43:8642`)
   - **Metrics URL** — Optional system metrics endpoint (e.g. `http://192.168.55.43:8643/system`)
   - **API Endpoint** — Auto-updates from Server URL; edit if needed
   - **API Key** — Shown masked; configured in the JavaScript source
   - **Model** — Select from available models (or leave on `auto`)
3. Start chatting. Press **Enter** to send, **Shift+Enter** for a new line.

## Configuration

All settings are saved to `localStorage` and persist across browser sessions.

| Setting | Description |
|---------|-------------|
| Server URL | Base URL of the AI server (used for chat API + health checks). Default: `http://192.168.55.43:8642` |
| Metrics URL | System metrics endpoint (optional). Default: `http://192.168.55.43:8643/system` |
| API Endpoint | Full URL for `/v1/chat/completions`. Auto-synced from Server URL |
| API Key | Bearer token sent with every request (set in source code) |
| Model | Model identifier; `auto` uses server default |
| TTS Voice | Browser speech synthesis voice (populated dynamically) |
| TTS Rate | Speech speed (0.5–2.0, default 1.05) |
| TTS Pitch | Voice pitch (0.5–1.5, default 0.9) |
| Auto-speak | Automatically read Jarvis replies aloud |
| Always-on listening | Keep the microphone active between messages |
| Fullscreen on start | Enter fullscreen mode when the page loads |

## Network Access

To access JARVIS from another device on your LAN:

1. **On the server**: ensure the AI API is bound to `0.0.0.0` (not `127.0.0.1`) and listens on the right port
2. **On your phone/laptop**: open `jarvis.html` in a browser
3. **In Settings**: enter the server's LAN IP as the **Server URL** (e.g. `http://192.168.55.43:8642`)
4. The API Endpoint and health check will auto-update to use this address

## Shortcuts

| Key | Action |
|-----|--------|
| `Enter` | Send message |
| `Shift+Enter` | New line in textarea |
| `Space` (while listening) | Stop microphone |
| `Esc` | Close settings / stats panel |

## Files

| File | Purpose |
|------|---------|
| `jarvis.html` | Single-file application (HTML + CSS + JS) |
| `README.md` | This manual |

## Notes

- This is a standalone HTML file with no build step or dependencies (except `marked.js` loaded from CDN for Markdown rendering)
- The API key is hardcoded in the JavaScript source — edit it directly for your setup
- Messages are stored in the browser's `localStorage` under the keys `jarvis_settings` and `jarvis_chats`
- Voice input requires a browser that supports the Web Speech API (Chrome, Edge, Safari)
- TTS uses the browser's built-in `speechSynthesis` — no external service required
- For HTTPS servers, the page must also be served over HTTPS (or the browser will block mixed content)
