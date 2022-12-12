import telebot
from telebot import types
from data import data
from utils import *

bot = telebot.TeleBot('5701363036:AAETkkefvAj08y5hCUTw2UPJyR2j-NSdAzw')

state = State()

@bot.message_handler(commands = ['start', 'help'])
def start(message):
    mess = f'Привет, {message.from_user.first_name}'
    bot.send_message(message.chat.id, mess)


@bot.message_handler(commands=['type'])
def type(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("УВП-111")
    btn2 = types.KeyboardButton("УВП-112")
    btn3 = types.KeyboardButton("УВВ-111")
    btn4 = types.KeyboardButton("УИС-111")
    btn5 = types.KeyboardButton("УИС-112")

    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.chat.id, text="{0.first_name}, выберете свою группу :)".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):

    if not message.text in valid_groups and not message.text in valid_days:
        # Отправка сообщения с ошибкой "неверная команда"
        print(message.text)
        return

    if state.group == "" and state.week_day == "":
        state.group = message.text

        markup = create_reply_keyboard(items=["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"], resize_keyboard=True)
        bot.send_message(message.chat.id, text="{0.first_name}, выберете день недели :)".format(message.from_user), reply_markup=markup)

    elif state.group != "" and state.week_day == "":
        state.week_day = message.text
        bot.send_message(message.chat.id, text=data[state.group][state.week_day])
        state.reset()

@bot.message_handler()
def get_user_text(message):
    if message.text == "Привет" or message.text == "привет":
        bot.send_message(message.chat.id, "Привет!")
    # elif message.text == "photo" or message.text == "Photo":
    #     foto = open("Снимок экрана 2022-10-07 в 14.20.11.png", "rb")
    #     bot.send_photo(message.chat.id, foto)
    else:
        bot.send_message(message.chat.id, "я не понимаю тебя")





bot.polling(none_stop = True)
