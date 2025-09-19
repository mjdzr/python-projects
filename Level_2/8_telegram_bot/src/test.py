import os

import telebot
from deep_translator import GoogleTranslator
from dotenv import load_dotenv
from utils.llm import call_llm

import utils.constants as constants
from utils.db import DBHandler


def load_config():
    load_dotenv()
    return os.getenv("TELEGRAM_BOT_TOKEN")

db_handler = DBHandler()

def create_bot(bot_token):
    return telebot.TeleBot(bot_token, parse_mode="markdown")

def setup_handlers(bot):
    # for adding to database
    # @bot.message_handler(func=lambda message: True)
    # def store_message(message):
    #     pass
    #     # TODO: store messages to database

    # for getting help
    @bot.message_handler(commands=["start", "help"])
    def start_help(message):
        bot.reply_to(message, constants.WELCOME_MESSAGE)

    # for translation
    @bot.message_handler(func=lambda message: should_translate_message(message))
    def echo_translation(message):
        handle_translation(message, bot)

    # database for storing messages
    @bot.message_handler(func=lambda message: True)
    def store_message(message):
        json_data = message.json
        db_handler.store_messages(json_data)

    # for handling reactions
    @bot.message_reaction_handler(func=lambda message: message.new_reaction and is_valid_reaction_user(message))
    def handle_reaction(message: telebot.types.Message):
        reaction = message.new_reaction[-1].emoji
        print(reaction)
        if reaction not in ["👍"]:
            return
        message_text_db = db_handler.get_message(message.message_id)
        if message_text_db:
            message_text = message_text_db.get('text')
            reply = bot.reply_to(message, constants.PROCESSING_MESSAGE)
            response = call_llm(message_text)
            bot.edit_message_text(chat_id=reply.chat.id, message_id=reply.id, text=response)

def is_group_valid(message):
    """Determine if a message is from a valid group."""
    return message.chat.username.lower() in [group.lower() for group in constants.GROUPS]

def is_valid_reaction_user(message):
    """Determine if an admin is reacting to the message."""
    return message.user.username.lower() in [admin.lower() for admin in constants.ADMINS_USERNAMES] and \
        is_group_valid(message)

def is_valid_reply(message):
    """Determine if an admin has replied to a message."""
    my_logic = message.reply_to_message is not None and \
            message.from_user.username.lower() in [admin.lower() for admin in constants.ADMINS_USERNAMES] and \
                is_group_valid(message)
    return my_logic

def should_translate_message(message):
    return ('translate' in message.text.lower() and is_valid_reply(message))

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
        #restart_on_change=True
    )

if __name__ == "__main__":
    print(constants.BOT_RUNNING_MESSAGE)
    main()
