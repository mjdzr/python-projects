import os
from dotenv import load_dotenv
import telebot
from deep_translator import GoogleTranslator
import utils.constants as constants

def load_config():
    load_dotenv()
    return os.getenv("TELEGRAM_BOT_TOKEN")

def create_bot(bot_token):
    return telebot.TeleBot(bot_token, parse_mode="HTML")

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

    # for handling reactions
    @bot.message_reaction_handler(func=lambda message: message.new_reaction and is_valid_reaction_user(message))
    def handle_reaction(message: telebot.types.Message):
        reaction = message.new_reaction[-1].emoji
        print(reaction)
        if reaction == "👍":
            bot.reply_to(message, "You liked this message!")
        elif reaction == "👎":
            bot.reply_to(message, "You disliked this message!")

def is_group_valid(message):
    """Determine if a message is from a valid group."""
    return message.chat.username.lower() in [group.lower() for group in constants.GROUPS]

def is_valid_reaction_user(message):
    """Determine if a user is valid for reacting to a message."""
    return message.user.username.lower() in [admin.lower() for admin in constants.ADMINS_USERNAMES] and \
        is_group_valid(message)

def is_valid_reply(message):
    """Determine if a an admin has replied to a message."""
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
        restart_on_change=True
    )

if __name__ == "__main__":
    print(constants.BOT_RUNNING_MESSAGE)
    main()
