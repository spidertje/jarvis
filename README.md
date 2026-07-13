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
- **Settings panel** — API endpoint, model, TTS voice/rate/pitch, toggles
- **System status panel** — connection health, server latency, system metrics
- **Clear chat** — reset conversation and local storage

## Requirements

- Any modern browser (Chrome, Firefox, Edge, Safari)
- An OpenAI-compatible API endpoint running locally or on your network
- HTTPS not required for local use; works with plain HTTP

## Quick Start

1. Open `jarvis.html` in a browser (double-click the file, or serve it from any web server)
2. Open **Settings** (⚙) and configure your API endpoint:
   - **API Endpoint** — e.g. `http://127.0.0.1:8642/v1/chat/completions`
   - **API Key** — shown masked; configured in the JavaScript source
   - **Model** — select from available models (or leave on `auto`)
3. Start chatting. Press **Enter** to send, **Shift+Enter** for a new line.

## Configuration

All settings are saved to `localStorage` and persist across browser sessions.

| Setting | Description |
|---------|-------------|
| API Endpoint | Full URL of your OpenAI-compatible `/v1/chat/completions` endpoint |
| API Key | Bearer token sent with every request (set in source code) |
| Model | Model identifier; `auto` uses server default |
| TTS Voice | Browser speech synthesis voice (populated dynamically) |
| TTS Rate | Speech speed (0.5–2.0, default 1.05) |
| TTS Pitch | Voice pitch (0.5–1.5, default 0.9) |
| Auto-speak | Automatically read Jarvis replies aloud |
| Always-on listening | Keep the microphone active between messages |
| Fullscreen on start | Enter fullscreen mode when the page loads |

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
