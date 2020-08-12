import telebot
from config import API_KEY

# simple echo bot on base pyTelegramBotAPI lib
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(func=lambda message: True)
def echo(message):
    if message.text == '/start':
        bot.reply_to(message, 'Welcome to weather bot. Bot can supply with weather forecast for today and tomorrow')
    elif 'hey' in message.text.lower():
        bot.reply_to(message, 'Hey, pal!')
    elif 'today' in message.text.lower():
        bot.reply_to(message, 'Weather for today')
    elif 'tomorrow' in message.text.lower():
        bot.reply_to(message, 'Weather for tomorrow')
    else:
        bot.reply_to(message, 'I dont understand')


bot.polling()

