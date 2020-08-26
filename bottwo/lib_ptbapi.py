import telebot
from datetime import date
from config import API_KEY

MAIN_STATE = 'main'
WEATHER_DATE_STATE = 'weather_date-handler'
WEATHER_DATA = {
    'june': {
        6: '6 degrees',
        8: '8 degrees',
        10: '10 degrees',
    },
    'august': {
        26: '26 degrees'
    }
}

MONTHS = {
    7: 'july',
    8: 'august',
}

# simple echo bot on base pyTelegramBotAPI lib
bot = telebot.TeleBot(API_KEY)
states = {}

@bot.message_handler(func=lambda message: True)
def dispatcher(message):
    print(states)
    user_id = message.from_user.id
    state = states.get(user_id, 'main')
    print('current state', user_id, state)

    if state == MAIN_STATE:
        main_handler(message)
    elif state == WEATHER_DATE_STATE:
        weather_date(message)

def main_handler(message):
    m = message.text.lower()
    if m == '/start':
        bot.send_message(
            message.chat.id,
            'Welcome to weather bot. Bot can supply you with weather forecast for today and tomorrow',
            # reply_to_message_id=message.message_id
        )
    # elif any(word in m for word in ['hey', 'hello', 'hi']):
    #     bot.reply_to(message, f'Hey, {message.from_user.first_name}!')
    elif 'weather' in m:
        bot.send_message(message.from_user.id, 'Inpute date in format: "month day" for forecast')
        states[message.from_user.id] = WEATHER_DATE_STATE
    else:
        bot.send_message(message.from_user.id, "I don't understand")
    

def weather_date(message):
    m = message.text.lower()
    if any(word in m for word in ['today', 'now', 'this day']):
        today = date.today()
        month_name = MONTHS[today.month]
        bot.send_message(message.from_user.id, WEATHER_DATA[month_name][today.day])
        states[message.from_user.id] = MAIN_STATE
    elif 'tomorrow' in m:
        bot.reply_to(message, 'Weather for tomorrow')
        states[message.from_user.id] = MAIN_STATE
    else:
        month, day = m.split(' ')
        day = int(day.strip())
        bot.reply_to(message, WEATHER_DATA[month][day])


if __name__ == "__main__":
    bot.polling()

