#!/usr/bin/env python3
"""JARVIS with API proxy to port 3001."""
import os
from flask import Flask, send_from_directory, request, Response
import requests as http_requests

app = Flask(__name__, static_folder='.')

API_BASE = 'http://192.168.55.43:3001/v1'
API_KEY = 'freellmapi-475bfc0f36bd5559f17fee9a2f92a33d52ab404869205e2f'

@app.route('/')
def index():
    return send_from_directory('.', 'jarvis.html')

@app.route('/jarvis.html')
def jarvis_html():
    return send_from_directory('.', 'jarvis.html')

@app.route('/v1/<path:path>', methods=['GET', 'POST'])
def proxy_api(path):
    url = f'{API_BASE}/{path}'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer *** '
    }
    # Forward request
    resp = http_requests.request(
        method=request.method,
        url=url,
        headers=headers,
        data=request.get_data(),
        params=request.args,
        timeout=120
    )
    return Response(resp.content, status=resp.status_code, headers=dict(resp.headers))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082)
