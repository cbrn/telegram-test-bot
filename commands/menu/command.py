from telegram.ext import CommandHandler, CallbackQueryHandler, CallbackContext
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update

def menu(update: Update, context: CallbackContext):
    keyboard = [[InlineKeyboardButton("🇪🇸", callback_data='🇪🇸'),
                 InlineKeyboardButton("🇺🇸", callback_data='🇺🇸')],

                [InlineKeyboardButton("🇵🇹", callback_data='🇵🇹')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Selecciona un idioma:', reply_markup=reply_markup)


def callbackQuery(bot, update):
    query = bot.callback_query
    query.answer()

    query.edit_message_text(text="Idioma seleccionado: {}".format(query.data))

menu_handler = CommandHandler('menu', menu)
