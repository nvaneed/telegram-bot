from flask import Flask, request
import requests
import os

TOKEN = os.environ.get("BOT_TOKEN")
TELEGRAM_API = f"https://api.telegram.org/bot{TOKEN}"

app = Flask(__name__)

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    data = request.json

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        requests.post(
            TELEGRAM_API + "/sendMessage",
            json={"chat_id": chat_id, "text": f"You said: {text}"}
        )

    return "OK", 200


@app.route("/")
def home():
    return "Bot is running"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
