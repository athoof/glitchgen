from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

import random
import json
import os
from zalgo_text import zalgo   

from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("TOKEN")
updater = Updater(token = TOKEN, use_context=True)

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

dispatcher = updater.dispatcher

def glitchText(update, context):
  g = zalgo.zalgo().zalgofy(update.message.text)
  context.bot.send_message(chat_id=update.effective_chat.id, text=g)
  
def glitchImage(update, context):
  context.bot.send_photo(chat_id=update.effective_chat.id, photo=update.message.photo)
  
def start(update, context): 
  context.bot.send_message(chat_id=update.effective_chat.id, text="Send image or text to glitch")
  
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

glitchText_handler = MessageHandler(Filters.text & (~Filters.command), glitchText)
dispatcher.add_handler(glitchText_handler)

glitchImage_handler = MessageHandler(Filters.photo & (~Filters.command), glitchImage)
dispatcher.add_handler(glitchImage_handler)
 
updater.start_polling()
