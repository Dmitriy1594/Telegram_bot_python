from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import apiai, json

# Commands
def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Hi!')

# Text message
def textMessage(bot, update):
     # Token API to Dialogflow
    request = apiai.ApiAI('TOKEN_HERE').text_request()
    # language
    request.lang = 'en'
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


if __name__ == '__main__':
    # Create the Updater and pass it your bot's token.
    updater = Updater(token='TOKEN_HERE')
    dispatcher = updater.dispatcher
    # add handlers
    dispatcher.add_handler(CommandHandler('start', startCommand))
    dispatcher.add_handler(MessageHandler(Filters.text, textMessage))
    # set updater
    updater.start_polling(clean=True)
    # stop bot
    updater.idle()
