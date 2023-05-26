import telebot
import parse
from telebot import types
from requests import get

token = "6142858271:AAFqIxhHfhNyMu-fQtwEdbQzEaGjEDYycI4"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Мотивация")
    markup.add(btn1)
    bot.send_message(message.chat.id, "Привет ✌️ Хочешь замотивироваться?".format(message.from_user),
                     reply_markup=markup)


@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == "Мотивация":
        img = parse.random_img()
        bot.send_photo(message.chat.id, get(img).content)


bot.polling(none_stop=True)
