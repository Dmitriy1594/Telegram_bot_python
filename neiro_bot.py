from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove
import apiai, json
import logging
import webbrowser

# when (and why) things don't work as expected
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

language = 'us'
translate = False

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)

# Generate flag emojis from country codes
def flag(code):
    OFFSET = 127462 - ord('A')
    code = code.upper()
    return chr(ord(code[0]) + OFFSET) + chr(ord(code[1]) + OFFSET)

def translateMessage(bot, update):
    # API to Dialogflow
    text = ''
    if translate == True:
        text = 'TOKEN_HERE'
    else:
        text = 'TOKEN_HERE'
    request = apiai.ApiAI(text).text_request()
    # In what language will the request be sent?
    request.lang = language
    # ID Dialog sessions (you need to learn the bot later)
    request.session_id = 'Neiro_bot'
    # We send request to AI with the message from the user
    request.query = update.message.text
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    # Parse JSON and pull out the answer.
    response = responseJson['result']['fulfillment']['speech']
    # If there is a response from the bot, we send it to the user;
    # if not, the bot did not understand it
    if response:
        bot.send_message(chat_id=update.message.chat_id, text=response)
    else:
        bot.send_message(chat_id=update.message.chat_id, text='I did not quite understand you!')

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Hi!')

def endCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Hope to see you again)')

def help(bot, update):
    txt = 'Commands:\nstart: /start\nmenu: /menu\nend: /end'
    update.message.reply_text("Use /start to run this bot.")

def menu(bot, update):
    keyboard = [[InlineKeyboardButton("Change language", callback_data='1')],
                 [InlineKeyboardButton("Translate function", callback_data='2')],
                [InlineKeyboardButton("Sites", callback_data='3')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('MENU:\nPlease choose:', reply_markup=reply_markup)

def us(bot, update):
    global language
    language = 'us'
    bot.send_message(chat_id=update.message.chat_id, text='Change language: done!')

def de(bot, update):
    global language
    language = 'de'
    bot.send_message(chat_id=update.message.chat_id, text='Change language: done!')

def ru(bot, update):
    global language
    language = 'ru'
    bot.send_message(chat_id=update.message.chat_id, text='Change language: done!')

def button(bot, update):
    query = update.callback_query

    if query.data == '1':
        txt = 'Change language:\n' + flag('us') + ' /us\n'
        txt += flag('de') + ' /de\n' + flag('ru') + ' /ru'
        bot.edit_message_text(text=txt,
                              chat_id=query.message.chat_id,
                              message_id=query.message.message_id)
    elif query.data == '2':
        text = ''
        global translate
        if translate == True:
            # global translate
            translate = False
            text = 'Translate function: on -> off!'
        else:
            # global translate
            translate = True
            text = 'Translate function: off -> on!'
        bot.edit_message_text(text=text,
                              chat_id=query.message.chat_id,
                              message_id=query.message.message_id)
    elif query.data == '3':
        webbrowser.open('https://puzzle-english.com')
        webbrowser.open('https://www.ted.com')

def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater(token='TOKEN_HERE')
    # For quicker access to the Dispatcher
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('menu', menu))
    dispatcher.add_handler(CallbackQueryHandler(button))
    dispatcher.add_handler(CommandHandler('help', help))
    dispatcher.add_handler(MessageHandler(Filters.text, translateMessage))
    dispatcher.add_handler(CommandHandler('us', us))
    dispatcher.add_handler(CommandHandler('de', de))
    dispatcher.add_handler(CommandHandler('ru', ru))
    dispatcher.add_handler(CommandHandler('end', endCommand))
    dispatcher.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()
