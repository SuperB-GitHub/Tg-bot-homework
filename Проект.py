import telebot
from telebot import types

API_TOKEN = '565:AAEWT6_zH3_-dzaKEMZ0Y'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start','helps'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Д\З 💾")
    btn2 = types.KeyboardButton("Помощь ❓")
    btn3 = types.KeyboardButton("Обратная связь 📞")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я 👾бот👾 для рассылки Д\З".format(message.from_user), reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Д\З 💾"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn22 = types.KeyboardButton("Показать Д\З")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn22, back)
        bot.send_message(message.chat.id, text="Для того чтобы использовать бота пользуйся 🔽кнопками🔽", reply_markup=markup)

    elif(message.text == "Помощь ❓"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Что ты такое?")
        btn2 = types.KeyboardButton("Как узнать Д\З?")
        btn3 = types.KeyboardButton("Кто твои создатели?")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)
    

    elif(message.text == "Что ты такое?"):
        bot.send_message(message.chat.id, "Привет! Я 👾бот👾 для рассылки Д\З")

    elif(message.text == "Обратная связь 📞"):
        bot.send_message(message.chat.id, "Отправляйте свои пожелания и предложения к нам на почту TipaVKB13PAK@ya.ru")    

    elif(message.text == "Показать Д\З"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn12 = types.KeyboardButton("Д\З на следующую неделю")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn12, back)
        bot.send_message(message.chat.id, '❄ 19 декабря ❄\n||  Деловая коммуникация: Зачёт \n||  Физкультура: Зачёт с оценкой ', parse_mode = 'html',reply_markup=markup)
        bot.send_message(message.chat.id, '❄ 20 декабря ❄\n||  Основы проектной деятельности: Зачёт с оценкой', parse_mode = 'html')
        bot.send_message(message.chat.id, '❄ 21 декабря ❄\n||  Иностранный язык: Зачёт ', parse_mode = 'html')
        bot.send_message(message.chat.id, '❄ 22 декабря ❄\n||  На это число нет ничего ', parse_mode = 'html')
        bot.send_message(message.chat.id, '❄ 23 декабря ❄\n||  Алгоритмы и структуры данных: Зачёт с оценкой', parse_mode = 'html')
        bot.send_message(message.chat.id, '❄ 24 декабря ❄\n||  На это число нет ничего', parse_mode = 'html')    
    
    elif(message.text == "Д\З на следующую неделю"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back)
        bot.send_message(message.chat.id, '❄ 26 декабря ❄\n||  Информатика: Экзамен', parse_mode = 'html',reply_markup=markup)
        bot.send_message(message.chat.id, '❄ 27 декабря ❄\n||  На это число нет ничего ', parse_mode = 'html')
        bot.send_message(message.chat.id, '❄ 28 декабря ❄\n||  На это число нет ничего ', parse_mode = 'html')
        bot.send_message(message.chat.id, '❄ 29 декабря ❄\n||  На это число нет ничего ', parse_mode = 'html')
        bot.send_message(message.chat.id, '❄ 30 декабря ❄\n||  На это число нет ничего ', parse_mode = 'html')
        bot.send_message(message.chat.id, '🎄 31 декабря 🎄\n||  На это число нет ничего ', parse_mode = 'html')    
    
    elif (message.text == "Как узнать Д\З?"):
        bot.send_message(message.chat.id, text="Следуй 🔽кнопкам🔽 по кнопке Д\З 💾 и у тебя всё получится!")

    elif (message.text == "Кто твои создатели?"):
        bot.send_message(message.chat.id, text="Мои создатели группа ПАК:\nПанарин Д.С.\nАртюхов А.С.\nКовалец И.А.")
    
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Д\З 💾")
        button2 = types.KeyboardButton("Помощь ❓")
        button3 = types.KeyboardButton("Обратная связь 📞")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="Ты что-то не так написал, попробуй пользоваться 🔽кнопками🔽\nТакже помощь представлена по 🔽кнопке Помощь ❓")

bot.polling(none_stop=True)
