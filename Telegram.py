# Задание для школы

import telebot
import requests

bot = telebot.TeleBot('секрет же')
# Клавиатуры
keyboard1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard1.row('Погода', 'Когда встречаемся?')
keyboard1.row('Хочу выполнить другую команду')
keyboard2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard2.row("Можешь отправлять!")
filename = 'message.txt'


@bot.message_handler(commands=['start'])
def start(message):
    # file = open(filename, 'a')
    # file.write(str(message.chat.title) + '\n' + str(message.from_user.first_name) + "    " + str(
    #     message.from_user.username) + '\n' + str(message.text) + '\n' + "------------------------" + '\n')
    # file.close()
    # print(str(message.chat.title) + '\n' + str(message.from_user.first_name) + "    " + str(
    #     message.from_user.username) + '\n' + str(message.text) + '\n' + "------------------------" + '\n')
    bot.send_message(message.from_user.id, "Привет! Это бот помощник!", reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    file = open(filename, 'a')
    file.write(str(message.chat.title) + '\n' + str(message.from_user.first_name) + "    " + str(
        message.from_user.username) + '\n' + str(message.text) + '\n' + "------------------------" + '\n')
    file.close()
    print(str(message.chat.title) + '\n' + str(message.from_user.first_name) + "    " + str(
        message.from_user.username) + '\n' + str(message.text) + '\n' + "------------------------" + '\n')
    if message.text == 'Погода':
        markup = telebot.types.InlineKeyboardMarkup()
        my_btn = telebot.types.InlineKeyboardButton(text='Полная информация о погоде тут!',
                                                    url='https://yandex.ru/pogoda/moscow')
        markup.add(my_btn)
        yandexpogoda = requests.get('https://yandex.ru/pogoda/moscow')
        text = '<span class="temp__value">'
        pose = yandexpogoda.text.find(text)
        answer = yandexpogoda.text[pose + 26:pose + 29]
        bot.send_message(message.from_user.id, "Сейчас в Москве " + answer + " градусов", reply_markup=markup)
    elif message.text == 'Хочу выполнить другую команду':
        bot.send_message(message.from_user.id,
                         "Напишите, какую команду вы хотите выполнить, и я скажу разработчику, чтобы он добавил эту функцию😉",
                         reply_markup=keyboard1)
        if message.text != 'Можешь отправлять!':
            file = open(filename, 'a')
            file.write(str(message.chat.title) + '\n' + str(message.from_user.first_name) + "    " + str(
                message.from_user.username) + '\n' + str(message.text) + '\n' + "------------------------" + '\n')
            file.close()
            print(str(message.chat.title) + '\n' + str(message.from_user.first_name) + "    " + str(
                message.from_user.username) + '\n' + str(message.text) + '\n' + "------------------------" + '\n')
        else:
            bot.send_message(message.from_user.id, "Спасибо!", reply_markup=keyboard1)
    elif message.text == 'Когда встречаемся?':
        bot.send_message(message.from_user.id, "Встреча возможно сегодня!", reply_markup=keyboard1)
    elif message.text == 'Бот':
        bot.send_message(message.from_user.id, "Привет! Это бот помощник!", reply_markup=keyboard1)
    elif message.text == 'Файл':
        bot.send_document(message.from_user.id, str(message.txt), reply_markup=keyboard1)
    elif message.text.capitalize() == 'Шп':

    elif message.chat.title == 'Перовская ОМЦ':
        file = open(filename, 'a')
        file.write('Перовская ОМЦ' + '\n')
        file.close()
        print('Перовская ОМЦ')
    elif message.chat.title == 'Боты':
        file = open(filename, 'a')
        file.write('Боты' + '\n')
        file.close()
        print('Боты')
    # else:
    #     file = open(filename, 'a')
    #     file.write(str(message.chat.title) + '\n' + str(message.from_user.first_name) + "    " + str(
    #         message.from_user.username) + '\n' + str(message.text) + '\n' + "------------------------" + '\n')
    #     file.close()
    #     print(str(message.chat.title) + '\n' + str(message.from_user.first_name) + "    " + str(
    #         message.from_user.username) + '\n' + str(message.text) + '\n' + "------------------------" + '\n')


@bot.message_handler(content_types=['stiker'])
def get_text_stiker(message):
    if message.stiker == 'ddd':
        print(1 + 2)
    else:
        file = open(filename, 'a')
        file.write(str(message.from_user.username) + '\n' + str(message.stiker) + '\n')
        file.close()
        print(message.from_user)
        print(message.stiker)


bot.polling(none_stop=True)
