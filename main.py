#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram.ext import Updater, CallbackQueryHandler
import logging


# Commands imports.
from commands.test.command import test_handler
from commands.start.command import start_handler
from commands.menu.command import menu_handler
from commands.menu.command import callbackQuery

# Logging and checkings.
logging.basicConfig(format='%(asctime)s - %(name)30s - %(levelname)8s [%(funcName)s] %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Main functions.

def main():
    updater = Updater(token='1254931161:AAEA4xHsN3vlEIcnE6il5g-T0J43a-HudTM', use_context=True)
    dispatcher = updater.dispatcher

    # Commands
    dispatcher.add_handler(test_handler)
    dispatcher.add_handler(start_handler)

    dispatcher.add_handler(menu_handler)
    dispatcher.add_handler(CallbackQueryHandler(callbackQuery))

    updater.start_polling()

    updater.idle()

if __name__ == "__main__":
    main()
