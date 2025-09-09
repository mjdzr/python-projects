import os
from dotenv import load_dotenv
import telebot
from deep_translator import GoogleTranslator
from utils.constants import WELCOME_MESSAGE, ADMINS_USERNAMES, GROUPS

def load_config():
    load_dotenv()
    return os.getenv("TELEGRAM_BOT_TOKEN")

def create_bot(bot_token):
    return telebot.TeleBot(bot_token, parse_mode="HTML")

def setup_handlers(bot):
    @bot.message_handler(commands=["start", "help"])
    def start_help(message):
        bot.reply_to(message, WELCOME_MESSAGE)

    @bot.message_handler(func=should_translate_message)
    def echo_translation(message):
        handle_translation(message, bot)

    @bot.message_reaction_handler(func=lambda message: True)
    def handle_reaction(message: telebot.types.Message):
        if not message.reaction:
            return
        reaction = message.new_reaction[-1].emoji
        print(reaction)
        if reaction == "👍":
            bot.reply_to(message, "You liked this message!")
        elif reaction == "👎":
            bot.reply_to(message, "You disliked this message!")

def should_translate_message(message):
    """Determine if a message should be translated and replied to."""
    return (
        message.reply_to_message is not None and
        'translate' in message.text.lower() and
        message.from_user.username.lower() in [admin.lower() for admin in ADMINS_USERNAMES] and
        message.chat.username in [group.lower() for group in GROUPS]
    )

def handle_translation(message, bot):
    """Translate the replied-to message and reply with the translation."""
    translated_text = GoogleTranslator(source='auto', target='en').translate(message.reply_to_message.text)
    output = f"Replied to message: {message.reply_to_message.text}\n\n<b>Translation</b>: {translated_text}\n"
    bot.reply_to(message, output)

def main():
    bot_token = load_config()
    bot = create_bot(bot_token)
    setup_handlers(bot)
    bot.infinity_polling(
        allowed_updates=['message', 'message_reaction'],
        restart_on_change=True
    )

if __name__ == "__main__":
    main()
