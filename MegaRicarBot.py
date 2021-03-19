import telebot
import config
import random
import requests
import json

bot = telebot.TeleBot(config.token)

data = requests.request('GET', 'https://api.openweathermap.org/data/2.5/weather?q=Kyiv&appid=793e66c0125054fe522cf07a9b852d59')
current_weather = json.loads(data.text)
temp = round(current_weather['main']['temp'] - 273.15)
feels_like = round(current_weather['main']['feels_like'] - 273.15)
clouds = current_weather['clouds']['all']
wind_speed = current_weather['wind']['speed']

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Саламалексус, твою мать ебали Форклес и Алекс')
    return(chat_id)

@bot.message_handler(content_types=['text'])
def get_text_message(message):
    name = message.from_user.first_name
    chat_id = message.chat.id

    first_message = "<b>{}</b>, сделай мне минет, пж 🥺".format(name)
    second_message = "<b>{}</b>, пукни в пакет, пж 🤨".format(name)
    third_message = "Пидора ответ 😈"

    message_list = [first_message, second_message, third_message]

    if message.text == 'Привет':
        bot.send_message(chat_id, "{}".format(random.choice(message_list)), parse_mode='HTML')
    elif message.text == "/help":
        bot.send_message(chat_id, "Напиши Привет")
    elif message.text == 'Ребята':
        bot.send_message(chat_id, "Хуята")
    elif message.text == 'Ребят':
        bot.send_message(chat_id, "Хуят")
    elif message.text == 'Нет':
        bot.send_message(chat_id, "Шлюхи аргумент 😎")
    elif message.text == 'Ок':
        bot.send_message(chat_id, "Хуёк 🥱")
    elif message.text == 'Погода':
        bot.send_message(chat_id, 'Сейчас температура воздуха - {} градусов, ощущается как {} градусов, облачность - {}%, скорость ветра - {}м/с'.format(temp, feels_like, clouds, wind_speed))

bot.polling(none_stop=True)