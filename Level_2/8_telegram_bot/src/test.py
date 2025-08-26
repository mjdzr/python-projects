import os

import telebot
from dotenv import load_dotenv

from deep_translator import GoogleTranslator

ADMINS_USERNAMES = ["mjDzr"]

# Load environment variables from a .env file
load_dotenv()

bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(bot_token, parse_mode="HTML")

# Start/help reply
@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the bot! I'm Maj!")

# Reply to message using the message itself ONLY if the message is a reply
@bot.message_handler(func=lambda message: (
    message.reply_to_message is not None and
    'translate' in message.text.lower() and
    message.from_user.username.lower() in [admin.lower() for admin in ADMINS_USERNAMES]
))
def echo_all(message):
    translated_text = GoogleTranslator(source='auto', target='en').translate(message.reply_to_message.text)
    output = f"Replied to message: {message.reply_to_message.text}\n\n<b>Translation</b>: {translated_text}\n"
    bot.reply_to(message, output)

bot.infinity_polling()
