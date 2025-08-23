import os

import telebot

bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(bot_token, parse_mode="HTML")

# Start/help reply
@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the bot! I'm Maj!")

# Reply to message using the message itself ONLY if the message is a reply
@bot.message_handler(func=lambda message: message.reply_to_message)
def echo_all(message):
    print('replied to message:')
    output = f"Original message: {message.reply_to_message.text}\nYour reply: {message.text}"
    bot.reply_to(message, output)

bot.infinity_polling()
