# Telegram_bot_python
Python telegram bots

## Description
### In all bots I use framework python-telegram-bot
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)

### talkbot.py
#### What you need to run this bot?
#### Steps:
0. open link:
- [dialogflow](https://dialogflow.com)

<image src='/photo/1.png'>
<image src='/photo/2.png'>

Sign up there, create agent and copy token:
```python
# Text message
def textMessage(bot, update):
    # Token API to Dialogflow
    request = apiai.ApiAI('TOKEN_HERE').text_request()
```
1. Write in telegram to BotFather:
- [BotFather](https://t.me/botfather)
Create bot and copy token:
```python
if __name__ == '__main__':
    # Create the Updater and pass it your bot's token.
    updater = Updater(token='TOKEN_HERE')
```
2. git clone this repository
4. open terminal or command line and write this to run the bot:
```
$ python talkbot.py
```

### neiro_bot.py
### All steps are the same as in talkbot.py
### But in 0 step you need create 2 different agents and copy:
```python
def translateMessage(bot, update):
    # API to Dialogflow
    text = ''
    if translate == True:
    text = 'TOKEN_HERE'
    else:
    text = 'TOKEN_HERE'
```
### Don't forget about tetegram token:
```python
def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater(token='TOKEN_HERE')
```
## Links:
- [Dialogflow](https://dialogflow.com)
- [Habr](https://habr.com/post/346606/)
- [ProgLib](https://proglib.io/p/telegram-bot/)
- [Tproger](https://tproger.ru/translations/telegram-bot-create-and-deploy/)
- [Where to host Telegram Bots](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Where-to-host-Telegram-Bots)
- [Tutorial to create your first Bot](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions-–-Your-first-Bot)
