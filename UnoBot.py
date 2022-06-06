# Бот, для того, чтобы с ним играть в Уно (не доделанный проект)


import telebot, random, datetime, traceback

while True:
    try:
        bot = telebot.TeleBot('1192869940:AAGBx2uzrpaLRBx93YngQ2xMs9A6Vn2SvoQ')

        # Клавиатуры
        keyboard_start = telebot.types.ReplyKeyboardMarkup(resize_keyboard=False, one_time_keyboard=True)

        keyboard_player_cards = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)

        keyboard_take_card = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)

        keyboard_congratulation = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        # Данные пользователей
        users = {}
        Users = open('Users.txt', 'r')
        for line in Users:
            line = line.split(', ')
            users.update({line[0]: [int(line[1]), int(line[2].strip())]})
        Users.close()


        # Выдаёт карту
        def cards(numeral=False):
            if not numeral:
                color = random.choice(
                    "🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛⬛⬛⬛")
                if color == '⬛':
                    if random.choice('4⚫') == '4':
                        return color + '+4'
                    else:
                        return color + '⚫'
                else:
                    sign = random.choice('000111222333444555666777888999↕↕🚫🚫++')
                    if sign == '+':
                        sign = '+2'
                    return color + sign
            else:
                return random.choice(
                    "🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩") + random.choice(
                    '0123456789')


        # Выводит карты
        def show_cards(posledniy_shans=False):
            global kol_vo_cards, card1, card2, card3, card4, card5, card6, card7, card8, card9, card10, card11, card12, card13, card14, card15, card16, card17, card18, card19, card20, card21, card22, card23, card24, card25, keyboard_player_cards, keyboard_take_card, users
            keyboard_player_cards = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            if kol_vo_cards >= 1:
                keyboard_player_cards.row(card1)
            if kol_vo_cards >= 2:
                keyboard_player_cards.row(card2)
            if kol_vo_cards >= 3:
                keyboard_player_cards.row(card3)
            if kol_vo_cards >= 4:
                keyboard_player_cards.row(card4)
            if kol_vo_cards >= 5:
                keyboard_player_cards.row(card5)
            if kol_vo_cards >= 6:
                keyboard_player_cards.row(card6)
            if kol_vo_cards >= 7:
                keyboard_player_cards.row(card7)
            if kol_vo_cards >= 8:
                keyboard_player_cards.row(card8)
            if kol_vo_cards >= 9:
                keyboard_player_cards.row(card9)
            if kol_vo_cards >= 10:
                keyboard_player_cards.row(card10)
            if kol_vo_cards >= 11:
                keyboard_player_cards.row(card11)
            if kol_vo_cards >= 12:
                keyboard_player_cards.row(card12)
            if kol_vo_cards >= 13:
                keyboard_player_cards.row(card13)
            if kol_vo_cards >= 14:
                keyboard_player_cards.row(card14)
            if kol_vo_cards >= 15:
                keyboard_player_cards.row(card15)
            if kol_vo_cards >= 16:
                keyboard_player_cards.row(card16)
            if kol_vo_cards >= 17:
                keyboard_player_cards.row(card17)
            if kol_vo_cards >= 18:
                keyboard_player_cards.row(card18)
            if kol_vo_cards >= 19:
                keyboard_player_cards.row(card19)
            if kol_vo_cards >= 20:
                keyboard_player_cards.row(card20)
            if kol_vo_cards >= 21:
                keyboard_player_cards.row(card21)
            if kol_vo_cards >= 22:
                keyboard_player_cards.row(card22)
            if kol_vo_cards >= 23:
                keyboard_player_cards.row(card23)
            if kol_vo_cards >= 24:
                keyboard_player_cards.row(card24)
            if kol_vo_cards >= 25:
                keyboard_player_cards.row(card25)
            if not posledniy_shans:
                keyboard_player_cards.row('Нет карты')
            else:
                keyboard_player_cards.row('Пропускаю ход.')


        # Переменные
        # Количество карт
        bot_kol_vo_cards = 7
        kol_vo_cards = 7
        # Генерация карт бота
        bot_card1 = cards()
        bot_card2 = cards()
        bot_card3 = cards()
        bot_card4 = cards()
        bot_card5 = cards()
        bot_card6 = cards()
        bot_card7 = cards()
        bot_card8 = cards()
        bot_card9 = cards()
        bot_card10 = cards()
        bot_card11 = cards()
        bot_card12 = cards()
        bot_card13 = cards()
        bot_card14 = cards()
        bot_card15 = cards()
        bot_card16 = cards()
        bot_card17 = cards()
        bot_card18 = cards()
        bot_card19 = cards()
        bot_card20 = cards()
        bot_card21 = cards()
        bot_card22 = cards()
        bot_card23 = cards()
        bot_card24 = cards()
        bot_card25 = cards()
        # Генерация карт игрока
        card1 = cards()
        card2 = cards()
        card3 = cards()
        card4 = cards()
        card5 = cards()
        card6 = cards()
        card7 = cards()
        card8 = cards()
        card9 = cards()
        card10 = cards()
        card11 = cards()
        card12 = cards()
        card13 = cards()
        card14 = cards()
        card15 = cards()
        card16 = cards()
        card17 = cards()
        card18 = cards()
        card19 = cards()
        card20 = cards()
        card21 = cards()
        card22 = cards()
        card23 = cards()
        card24 = cards()
        card25 = cards()
        congratulation, congratulation_message, congratulation_id, congratulation_kol_vo, congratulatory = False, False, 0, 0, ''


        # Приветствие
        @bot.message_handler(commands=['start'])
        def start(message):
            global kol_vo_cards, card1, card2, card3, card4, card5, card6, card7, card8, card9, card10, card11, card12, card13, card14, card15, card16, card17, card18, card19, card20, card21, card22, card23, card24, card25, bot_card1, bot_card2, bot_card3, bot_card4, bot_card5, bot_card6, bot_card7, bot_card8, bot_card9, bot_card10, bot_card11, bot_card12, bot_card13, bot_card14, bot_card15, bot_card16, bot_card17, bot_card18, bot_card19, bot_card20, bot_card21, bot_card22, bot_card23, bot_card24, bot_card25, keyboard_player_cards, keyboard_take_card, keyboard_start, users, Users, congratulation, congratulation_message, congratulation_id, congratulation_kol_vo, congratulatory
            print(message.from_user.first_name, message.from_user.last_name, message.from_user.username, message.text,
                  message.from_user.id, str(datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=3))))[:19])
            file = open('UnoBot_message.txt', 'a')
            file.write(str(message.from_user.first_name) + ' ' + str(message.from_user.last_name) + ' ' + str(
                message.from_user.username) + ' ' + str(message.text) + ' ' + str(message.from_user.id) + ' ' + str(
                datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=3))))[:19] + '\n')
            file.close()
            if not str(message.from_user.first_name) + ' ' + str(message.from_user.last_name) + ' ' + str(
                    message.from_user.username) in users:
                users.update({str(message.from_user.first_name) + ' ' + str(message.from_user.last_name) + ' ' + str(
                    message.from_user.username): [message.from_user.id, 7]})
                Users = open('Users.txt', 'a')
                Users.write(
                    '\n{} {} {}, {}, 7'.format(str(message.from_user.first_name), str(message.from_user.last_name),
                                               str(message.from_user.username), message.from_user.id))
                Users.close()
            keyboard_start = telebot.types.ReplyKeyboardMarkup(resize_keyboard=False, one_time_keyboard=True)
            keyboard_start.row('Ну тогда давай начнём?', 'Правила')
            bot.send_message(message.from_user.id,
                             "Привет! Я НЕ могу сыграть с тобой в уно. Бот находится в разработке, поэтому он не пока что может только выдать карты и объяснить правила",
                             reply_markup=keyboard_start)


        # Реакции на сообщения
        @bot.message_handler(content_types=['text'])
        def get_text_messages(message):
            global kol_vo_cards, card1, card2, card3, card4, card5, card6, card7, card8, card9, card10, card11, card12, card13, card14, card15, card16, card17, card18, card19, card20, card21, card22, card23, card24, card25, bot_card1, bot_card2, bot_card3, bot_card4, bot_card5, bot_card6, bot_card7, bot_card8, bot_card9, bot_card10, bot_card11, bot_card12, bot_card13, bot_card14, bot_card15, bot_card16, bot_card17, bot_card18, bot_card19, bot_card20, bot_card21, bot_card22, bot_card23, bot_card24, bot_card25, keyboard_player_cards, keyboard_take_card, keyboard_start, users, Users, congratulation, congratulation, congratulation_message, congratulation_id, congratulation_kol_vo, congratulatory
            print(message.from_user.first_name, message.from_user.last_name, message.from_user.username, message.text,
                  message.from_user.id, str(datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=3))))[:19])
            file = open('UnoBot_message.txt', 'a')
            file.write(str(message.from_user.first_name) + ' ' + str(message.from_user.last_name) + ' ' + str(
                message.from_user.username) + ' ' + str(message.text) + ' ' + str(message.from_user.id) + ' ' + str(
                datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=3))))[:19] + '\n')
            file.close()
            kol_vo_cards = users[str(message.from_user.first_name) + ' ' + str(message.from_user.last_name) + ' ' + str(
                message.from_user.username)][1]
            if message.text.capitalize() == "Поздравить!":
                keyboard_congratulation = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True,
                                                                            one_time_keyboard=True)
                keyboard_congratulation.row('Что происходит!?')
                for i in range(congratulation_kol_vo):
                    message_ = random.choice(congratulation_message)
                    if message_[:5] == 'CAACA':
                        bot.send_sticker(congratulation_id, message_, reply_markup=keyboard_congratulation)
                    else:
                        bot.send_message(congratulation_id, message_, reply_markup=keyboard_congratulation)
                congratulation, congratulation_message, congratulation_id, congratulation_kol_vo = False, False, 0, 0
                bot.send_message(message.from_user.id, 'Пользователь успешно поздравлен!')
            elif str(type(congratulation_message)) == "<class 'list'>":
                congratulation_message.append(str(message.text))

            elif congratulation:
                congratulation_id, congratulation_kol_vo = int(message.text.split()[0]), int(message.text.split()[1])
                keyboard_congratulation = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True,
                                                                            one_time_keyboard=True)
                keyboard_congratulation.row('Поздравить!')
                bot.send_message(message.from_user.id,
                                 "Отлично, теперь пишите сообщения, стикеры, которые хотите отправить этому человеку, и как только всё отправите, напишите Поздравить!",
                                 reply_markup=keyboard_congratulation)
                congratulation_message = []

            elif message.text.capitalize() == 'Что происходит!?':
                keyboard_start = telebot.types.ReplyKeyboardMarkup(resize_keyboard=False, one_time_keyboard=True)
                keyboard_start.row('(введи "/start" чтобы начать игру)')
                bot.send_message(message.from_user.id, "Вас поздравил пользователь" + ' ' + congratulatory,
                                 reply_markup=keyboard_start)

            elif message.text.capitalize() == "Поздравить":
                Users = open('Users.txt')
                bot.send_message(message.from_user.id, 'Список, кого можно поздравить:\n\n' + str(Users.read()))
                Users.close()
                bot.send_message(message.from_user.id,
                                 'Напишите id пользователя и сколько сообщений хотите отправить (не должно превышать 100) - через пробел')
                congratulation, congratulatory = True, str(message.from_user.first_name) + ' ' + str(
                    message.from_user.last_name) + ' ' + str(
                    message.from_user.username)

            elif message.text.capitalize() == "Ну тогда давай начнём?" or message.text.capitalize() == "Правила я понял, давай уже начнём?":
                bot.send_message(message.from_user.id, "Окей, выдаю карты.")
                # Количество карт
                kol_vo_cards = 7
                users[str(message.from_user.first_name) + ' ' + str(message.from_user.last_name) + ' ' + str(
                    message.from_user.username)][1] = kol_vo_cards
                Users = open('Users.txt', 'w')
                for i in users:
                    posledniy_user = i
                for i in users:
                    Users.write('{}, {}, {}'.format(i, users[i][0], users[i][1]))
                    if not i == posledniy_user:
                        Users.write('\n')
                Users.close()
                # Генерация карт бота
                bot_card1 = cards()
                bot_card2 = cards()
                bot_card3 = cards()
                bot_card4 = cards()
                bot_card5 = cards()
                bot_card6 = cards()
                bot_card7 = cards()
                bot_card8 = cards()
                bot_card9 = cards()
                bot_card10 = cards()
                bot_card11 = cards()
                bot_card12 = cards()
                bot_card13 = cards()
                bot_card14 = cards()
                bot_card15 = cards()
                bot_card16 = cards()
                bot_card17 = cards()
                bot_card18 = cards()
                bot_card19 = cards()
                bot_card20 = cards()
                bot_card21 = cards()
                bot_card22 = cards()
                bot_card23 = cards()
                bot_card24 = cards()
                bot_card25 = cards()
                # Генерация карт игрока
                card1 = cards()
                card2 = cards()
                card3 = cards()
                card4 = cards()
                card5 = cards()
                card6 = cards()
                card7 = cards()
                card8 = cards()
                card9 = cards()
                card10 = cards()
                card11 = cards()
                card12 = cards()
                card13 = cards()
                card14 = cards()
                card15 = cards()
                card16 = cards()
                card17 = cards()
                card18 = cards()
                card19 = cards()
                card20 = cards()
                card21 = cards()
                card22 = cards()
                card23 = cards()
                card24 = cards()
                card25 = cards()
                show_cards()
                bot.send_message(message.from_user.id, "Карты выданы!", reply_markup=keyboard_player_cards)
                if random.randint(1, 10) <= 5:
                    bot.send_message(message.from_user.id, "Ходите на " + cards(numeral=True),
                                     reply_markup=keyboard_player_cards)
                else:
                    bot.send_message(message.from_user.id, "Я хожу на " + cards(numeral=True),
                                     reply_markup=keyboard_player_cards)

            elif message.text.capitalize() == "Правила":
                keyboard_start = telebot.types.ReplyKeyboardMarkup(resize_keyboard=False, one_time_keyboard=True)
                keyboard_start.row('Правила я понял, давай уже начнём?')
                bot.send_message(message.from_user.id,
                                 '''Квадратик(🟥🟦🟨🟩⬛️) - цвет карты;
        Круг(⚫️) - карта, с помощью которой можно менять цвет
        Стрелочки(↕) - разворот хода (так как 2 игрока, то бот пропускает ход, и ты опять ходишь)
        Барьер(🚫) - пропуск хода''', reply_markup=keyboard_start)

            elif message.text.capitalize() == "Взять карту":
                kol_vo_cards += 1
                users[str(message.from_user.first_name) + ' ' + str(message.from_user.last_name) + ' ' + str(
                    message.from_user.username)][1] = kol_vo_cards
                Users = open('Users.txt', 'w')
                for i in users:
                    posledniy_user = i
                for i in users:
                    Users.write('{}, {}, {}'.format(i, users[i][0], users[i][1]))
                    if not i == posledniy_user:
                        Users.write('\n')
                Users.close()
                show_cards(posledniy_shans=True)
                bot.send_message(message.from_user.id, 'В итоге ходите?', reply_markup=keyboard_player_cards)

            elif message.text.capitalize() == "Нет карты":
                keyboard_take_card = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
                keyboard_take_card.row('Взять карту', 'Пропустить ход')
                bot.send_message(message.from_user.id, 'Выберите действие', reply_markup=keyboard_take_card)

            elif message.text.capitalize() == "Пропустить ход":
                show_cards()
                bot.send_message(message.from_user.id, 'Окей, я хожу', reply_markup=keyboard_player_cards)

            elif message.text.capitalize() == "Пропускаю ход.":
                show_cards()
                bot.send_message(message.from_user.id, 'Окей, я хожу', reply_markup=keyboard_player_cards)

            elif message.text.upper() == "SOS" or message.text == "🆘":
                nomber_word = random.randint(0, 7)
                words = ["А?", "Что?", "ШО?", "А!?", "Начался КОСМИЧЕСКИЙ АПОКАЛИПСИС??!!",
                         "ААААААААА! СТРААААШНААААААА",
                         "ДА ЧТО СЛУЧИЛОСЬ ТО????????", 'АААААААААААаFFFFFFFFFFFfуцрапцслутдаьгdsythfjgn']
                bot.send_message(message.from_user.id, words[nomber_word])

            elif message.text.capitalize() == "Не работай" or message.text.capitalize() == "Сломайся":
                quit()
                exit()

            elif message.text.capitalize() == "Ты работаешь?" or message.text.capitalize() == "Ты работаешь" or message.text.capitalize() == "Ты работешь?" or message.text.capitalize() == "Ты работешь":
                # bot.send_message(1316880892, 'И чтобы начать играть нужно ввести /start если что.)')
                bot.send_message(message.from_user.id, 'Да, работаю!')


        @bot.message_handler(content_types=['sticker'])
        def get_sticker(message):
            global kol_vo_cards, card1, card2, card3, card4, card5, card6, card7, card8, card9, card10, card11, card12, card13, card14, card15, card16, card17, card18, card19, card20, card21, card22, card23, card24, card25, bot_card1, bot_card2, bot_card3, bot_card4, bot_card5, bot_card6, bot_card7, bot_card8, bot_card9, bot_card10, bot_card11, bot_card12, bot_card13, bot_card14, bot_card15, bot_card16, bot_card17, bot_card18, bot_card19, bot_card20, bot_card21, bot_card22, bot_card23, bot_card24, bot_card25, keyboard_player_cards, keyboard_take_card, keyboard_start, users, Users, congratulation, congratulation_message, congratulation_id, congratulation_kol_vo, congratulatory
            print(message.from_user.first_name, message.from_user.last_name, message.from_user.username,
                  message.sticker.file_id, message.from_user.id,
                  str(datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=3))))[:19])
            file = open('UnoBot_message.txt', 'a')
            file.write(str(message.from_user.first_name) + ' ' + str(message.from_user.last_name) + ' ' + str(
                message.from_user.username) + ' ' + str(message.sticker.file_id) + ' ' + str(
                message.from_user.id) + ' ' + str(
                datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=3))))[:19] + '\n')
            file.close()
            if str(type(congratulation_message)) == "<class 'list'>":
                congratulation_message.append(str(message.sticker.file_id))
            else:
                bot.send_sticker(message.from_user.id, message.sticker.file_id)


        bot.polling(none_stop=True, timeout=1000)

    except:
        bot.send_message(369005503, 'У меня что-то сломалось🤷')
        bot.send_message(369005503, traceback.format_exc())
        print('Ошибка')
        print('Ошибка')
        traceback.print_exc()
        print('Ошибка')
        print('Ошибка')
