#!/usr/bin/python3

from flask import Flask, request, jsonify

from TGBot import Bot
from config import TOKEN
from bitcoin_parser import parse_bitcoin


app = Flask(__name__)
bot = Bot(TOKEN)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        r = request.get_json()
        bot.handle_message(r)
        return jsonify(r)
    return "<h1>Flask application.</h1>"


def say_hi():
    return "Hello, friend"


if __name__ == "__main__":
    bot.add_handler("Hello", say_hi)
    bot.add_handler("/bitcoin", parse_bitcoin)
    app.run()
