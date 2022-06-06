import telebot, requests, speech_recognition as sr, datetime, pyttsx3, random

engine = pyttsx3.init()


def speak(what):
    print(what)
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()


speak_engine = pyttsx3.init()
bot = telebot.TeleBot('729706147:AAHtuBZtHpcoX6Dc_1UrmssT1YK2vwk1t_c')
#Клавиатуры
keyboard1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard1.row('Привет!','Погода')
keyboard1.row('Как тебя зовут?', "Расскажи анекдот!")
keyboard1.row('Мне нечего делать')
keyboard2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard2.row('👍✅❗','😐','👎🏻❌❎')
keyboard3 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard3.row('Ещё!', 'Меню')
keyboard4 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard4.row('Короткую', 'Полную!')
keyboard5 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard5.row('👍✅!!','😐','👎🏻❌❎')
keyboard5.row('Короткую', 'Меню')
keyboard6 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard6.row('👍✅!','😐','👎🏻❌❎')
keyboard6.row('Полную!', 'Меню')
keyboard7 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard7.row('Полную!', 'Меню')
keyboard8 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard8.row('Короткую', 'Меню')
keyboard9 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard9.row('Анекдот', 'Меню')


@bot.message_handler(commands=['start'])
def start(message):
    print(message)
    bot.send_message(message.from_user.id, "Привет! Ты написал боту который может делать некоторые команды")
    bot.send_message(message.from_user.id, "Так же не забудь отправить мне стикер)", reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    print(message)
    if message.text == "Привет!":
        bot.send_message(message.from_user.id, "Хеллоу!)", reply_markup=keyboard1)
        speak("Хеллоу!)")
    elif message.text == "Как тебя зовут?":
        markup = telebot.types.InlineKeyboardMarkup()
        my_btn = telebot.types.InlineKeyboardButton(text='От какого слова?', url='https://translate.google.ru/#view=home&op=translate&sl=ru&tl=ru&text=От%20слова%20Алиса%0AПривет%20я%20Алиса%2C%20ваш%20голосовой%20помощник)')
        markup.add(my_btn)
        bot.send_message(message.from_user.id, "Меня зовут Алис", reply_markup=markup)
        bot.send_message(message.from_user.id, ")", reply_markup=keyboard1)
    elif message.text == "Расскажи анекдот!":
        bot.send_message(message.from_user.id, "Сидит на рельсах лось1. Подхохит к нему лось3, лось1 спрашивает его 'Чего тебе надобно лосиный молодец?', лось2 молчит, а он и говорит ему 'Сам ты лосиный молодец! Лучше подвинься и дай поиграть во что-нибудь!' а лось 2 выскакивает и говорит, 'ПООЕЗД ЕДЕТ!!!!! что ж вы тут стоя сидите?' а они 'Это не важно!", reply_markup=keyboard2)
        bot.send_message(message.from_user.id, "Ну как? Понравилось?)")
    elif message.text == "👍✅❗":
        bot.send_message(message.from_user.id, "О круто!", reply_markup=keyboard3)
    elif message.text == "😐":
        bot.send_message(message.from_user.id, "Ну ты не обижайся, я ещё только учусь)")
        bot.send_message(message.from_user.id, "Можешь посмотреть мои другие анекдоты)", reply_markup=keyboard9)
    elif message.text == "👎🏻❌❎":
        bot.send_message(message.from_user.id, "Эх, печалька(((")
        bot.send_message(message.from_user.id, "Я нубик в анекдотах")
        bot.send_message(message.from_user.id, "Можешь посмотреть мои другие анекдоты)", reply_markup=keyboard9)
    elif message.text == "Ещё!":
        bot.send_message(message.from_user.id, "Тебе полную или котороткую версию анекдота?", reply_markup=keyboard4)
    elif message.text == "Меню":
        bot.send_message(message.from_user.id, "Ок", reply_markup=keyboard1)
    elif message.text == "Погода":
        markup = telebot.types.InlineKeyboardMarkup()
        my_btn = telebot.types.InlineKeyboardButton(text='Полная информация о погоде тут!', url='https://yandex.ru/pogoda/moscow')
        markup.add(my_btn)
        yandexpogoda = requests.get('https://yandex.ru/pogoda/moscow')
        text = '<span class="temp__value">'
        pose = yandexpogoda.text.find(text)
        answer = yandexpogoda.text[pose+26:pose+29]
        bot.send_message(message.from_user.id, "Сейчас в Москве " + answer + " градусов", reply_markup=keyboard1)
        bot.send_sticker(message.from_user.id, "CAADAgADdRoAAtjY4QABM5F8bzRy4S8C")
        bot.send_sticker(message.from_user.id, "CAADAgADdhoAAtjY4QABr_n93asLxWEC", reply_markup=markup)
    elif message.text == "Полную!":
        bot.send_message(message.from_user.id, "Цевелезованный росиянин конечно не топит печь, но иногда он выезжает за город например на дачу. Там у него неверняка есть печь. Так вот аникдото-рассказ как раз про них.")
        bot.send_message(message.from_user.id, "Был один россиянин, поехал он летом на дачу, там было холодно, решил он топить печь, нарубил дров, кинул их в печь и начал топить. . . Спустя пол часа звонит он своему знакомому Штирлицу и говорит 'Штирлиц, привет! Ты на даче?' а он говорит 'Да, а что?'  - Топишь печь?  - Да  - Сколько?  - Поль часа, А ЧТО?  - Да тут такое дело, что - нибудь с твоей  печью случилось?  - Ну да. . . - А что?  - Эх, ты наверно не поверишь, но...она взорвалась!  - Да поверю. х - х У меня то она просто сначало утонула! А потом ещё взлетела и сказала что полетела на Марс, так как мы (люди) её достали!!!  - Во мы уморы!")
        bot.send_message(message.from_user.id, "Ну как? Понравилось?)", reply_markup=keyboard5)
    elif message.text == "Короткую":
        bot.send_message(message.from_user.id, "Был штирлиц и россиянин, они топили печь ровно поль часа! После этого у штирлица печь взорвалась, а у россиянина печь утонула, а потом взлетела и сказала 'Вы меня люди уже достали! Я улетаю на Марс!!' и улетела на Марс.")
        bot.send_message(message.from_user.id, "Ну как? Понравилось?)", reply_markup=keyboard6)
    elif message.text == "👍✅!":
        bot.send_message(message.from_user.id, "Спасибо)", reply_markup=keyboard7)
    elif message.text == "👍✅!!":
        bot.send_message(message.from_user.id, "Спасибо)", reply_markup=keyboard8)
    elif message.text == "Анекдот":
        bot.send_message(message.from_user.id, "Тебе полную или котороткую версию анекдота?", reply_markup=keyboard4)
    elif message.text == "Мне нечего делать":
        bot.send_message(message.from_user.id, "Попробуй отправить мне стикер)")
    elif message.text == "sos" or message.text == "SOS" or message.text == "🆘":
        nomber_word = random.randint(0, 7)
        words = ["А?", "Что?", "ШО?", "А!?", "Начался КОСМИЧЕСКИЙ АПОКАЛИПСИС??!!", "ААААААААА! СТРААААШНААААААА", "ДА ЧТО СЛУЧИЛОСЬ ТО????????", 'АААААААААААаFFFFFFFFFFFfуцрапцслутдаьгdsythfjgn']
        bot.send_message(message.from_user.id, words[nomber_word], reply_markup=keyboard1)
    elif message.text == "Мем!" or message.text == "Хочу мем" or message.text == "Расскажи мем":
        nomber_word = random.randint(0, 8)
        words = ["А?", "Что?", "ШО?", "А!?", "Начался КОСМИЧЕСКИЙ АПОКАЛИПСИС??!!", "ААААААААА! СТРААААШНААААААА",
                 "ДА ЧТО СЛУЧИЛОСЬ ТО????????", 'АААААААААААаFFFFFFFFFFFfуцрапцслутдаьгdsythfjgn']
        bot.send_message(message.from_user.id, words[nomber_word], reply_markup=keyboard1)

    else:
        print(message)
        bot.send_message(message.from_user.id, "Ничего не понятно и не очень интересно..", reply_markup=keyboard1)


@bot.message_handler(content_types=['sticker'])
def get_sticker(message):
    print(message)
    if message.text == 'CAADAgADGwADem8WBPhrahZfHU31Ag':
        bot.send_message(message.from_user.id, "О! Это же мой любимый стикер из набора тачки!)")
        bot.send_message(message.from_user.id, "Id этого стикера: " + message.sticker.file_id, reply_markup=keyboard1)
    else:
        bot.send_message(message.from_user.id, "Прикольный стикер! Но мне больше нравится вот этот:")
        bot.send_sticker(message.from_user.id, "CAADAgADFQADem8WBJsMep7FcivIAg")
        bot.send_message(message.from_user.id, "Id этого стикера: " + message.sticker.file_id, reply_markup=keyboard1)


bot.polling(none_stop=True)
