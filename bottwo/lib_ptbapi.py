import telebot
from config import API_KEY

# simple echo bot on base pyTelegramBotAPI lib
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(func=lambda message: True)
def echo(message):
    m = message.text.lower()
    if m == '/start':
        bot.send_message(
            message.chat.id,
            'Welcome to weather bot. Bot can supply you with weather forecast for today and tomorrow',
            # reply_to_message_id=message.message_id
        )
    elif any(word in m for word in ['hey', 'hello', 'hi']):
        bot.reply_to(message, f'Hey, {message.from_user.first_name}!')
    elif any(word in m for word in ['today', 'now', 'this day']):
        bot.reply_to(message, 'Weather for today')
    elif 'tomorrow' in m:
        bot.reply_to(message, 'Weather for tomorrow')
    else:
        bot.reply_to(message, "I don't understand")


bot.polling()

