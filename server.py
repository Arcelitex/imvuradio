import requests
from flask import Flask, Response

SOURCE = "https://sleeping.radiostream123.com/"

app = Flask(__name__)

@app.route("/")
def home():
    return "Radio Proxy Running"

@app.route("/radio.mp3")
def stream():
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "*/*",
        "Icy-MetaData": "1"
    }

    upstream = requests.get(SOURCE, stream=True, headers=headers)

    def generate():
        for chunk in upstream.iter_content(chunk_size=16384):
            if chunk:
                yield chunk

    return Response(
        generate(),
        mimetype="audio/mpeg",
        headers={
            "icy-metaint": "0",
            "icy-name": "IMVU Radio Proxy",
            "icy-genre": "Radio",
            "Connection": "close",
            "Cache-Control": "no-cache"
        }
    )
