from flask import Flask, request
from telegram import Update

from dispatcher import bot, dispatcher

app = Flask(__name__)


@app.route('/', methods=['POST'])
def hello_world():  # put application's code here
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return {"result": "ok"}
