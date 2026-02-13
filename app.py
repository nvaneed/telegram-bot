from flask import Flask, request
import requests
import os

app = Flask(__name__)

TOKEN = os.environ.get("BOT_TOKEN")
API = f"https://api.telegram.org/bot{TOKEN}"

# VERY IMPORTANT — this route MUST match webhook url
@app.route(f"/{TOKEN}", methods=["POST"])
def telegram_webhook():
    data = request.get_json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        requests.post(API + "/sendMessage", json={
            "chat_id": chat_id,
            "text": f"Echo: {text}"
        })

    return "OK", 200


@app.route("/")
def home():
    return "Bot running", 200
