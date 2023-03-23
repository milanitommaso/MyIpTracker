from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

def telegram_message(new_ip):
    import requests
    import json
    import os

    # Read the Telegram bot token from telegram_data.json
    with open('telegram_data.json') as data:
        telegram_data = data.read()
    telegram_data = json.loads(telegram_data)

    bot_token = telegram_data["token"]
    chat_id = telegram_data["chat_id"]

    # Compose the Telegram message
    message = 'Your public IP has changed to {}'.format(new_ip)

    # Create the Telegram bot
    updater = Updater(bot_token)

    # Send the message to the Telegram bot
    updater.bot.send_message(chat_id, message)
    