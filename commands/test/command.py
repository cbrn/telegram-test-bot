from telegram.ext import CommandHandler, CallbackContext
from telegram import Update


def test(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.message.chat_id, text='¡Mensaje de prueba! 🎉')


test_handler = CommandHandler('test', test)
