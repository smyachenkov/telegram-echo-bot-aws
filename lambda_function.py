import os
import json
import requests

TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']


def send_message(chat_id, text):
    params = {
        "text": text,
        "chat_id": chat_id,
        "parse_mode": "MarkdownV2"
    }
    requests.get(
        "https://api.telegram.org/bot" + TELEGRAM_TOKEN + "/sendMessage",
        params=params
    )


def process_event(event):
    message = json.loads(event['body'])
    chat_id = message['message']['chat']['id']
    text = message['message']['text']

    if text == "/start":
        send_message(chat_id, "Hello, I am echo bot!")
        return

    if text is None:
        return

    send_message(chat_id, text)


def lambda_handler(event, context):
    process_event(event)
    return {
        'statusCode': 200
    }
