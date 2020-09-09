from telegram.ext import CommandHandler, CallbackContext
from telegram import Update, ParseMode


def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.message.chat_id, text='<b>Bienvenido usuario.</b>\n¡Usa /test o /menu para probar el bot!', parse_mode=ParseMode.HTML)


start_handler = CommandHandler('start', start)
