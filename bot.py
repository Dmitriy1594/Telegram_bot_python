import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Get your token
updater = Updater(token='TOKEN_HERE')
# For quicker access to the Dispatcher
dispatcher = updater.dispatcher

# when (and why) things don't work as expected
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

# start
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# add another handler that listens for regular messages
def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

# To start the bot, run
updater.start_polling()
