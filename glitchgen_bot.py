from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

import random
import json
import os

from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("TOKEN")
updater = Updater(token = TOKEN, use_context=True)

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

dispatcher = updater.dispatcher

