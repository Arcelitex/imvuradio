import requests
from flask import Flask, Response, stream_with_context

# Your original radio stream URL
SOURCE = "https://sleeping.radiostream123.com/"

app = Flask(__name__)

@app.route("/")
def home():
    return "Radio Proxy Running"

@app.route("/radio.mp3")
def proxy_stream():
    upstream = requests.get(SOURCE, stream=True, headers={
        "User-Agent": "Mozilla/5.0"
    })
    
    return Response(
        stream_with_context(upstream.iter_content(chunk_size=1024)),
        mimetype="audio/mpeg",
        headers={
            "Cache-Control": "no-cache",
            "Accept-Ranges": "bytes"
        }
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
