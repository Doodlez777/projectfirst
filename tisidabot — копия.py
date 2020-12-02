
import telebot
from telebot import types


bot = telebot.TeleBot('')



@bot.message_handler(commands=['start'])
def Start(message):
    startmenu = types.ReplyKeyboardMarkup(True, True)
    startmenu.row('В зал')
    bot.send_message(message.chat.id, 'Добро пожаловать в спа-центр "Тисида"!✋🏻 \nг.Славянск👨🏻‍🏫\nЯ - ознакомительный бот \nСделаю тебе экскурсию', reply_markup=startmenu)

@bot.message_handler(content_types=['text'])
def Zal(message):
    if message.text == 'В зал':
        send = bot.send_message(message.chat.id, 'Введите ваше имя:')
        bot.register_next_step_handler(send, next2)

    elif message.text == '💪О фитнес - центре':
        if fit == 'fit':
            vibor1 = types.ReplyKeyboardMarkup(True, False)
            vibor1.row('⬅Назад')
            bot.send_photo(message.chat.id, 'https://slavgorod.com.ua/Images/StaticPages/sHL/sHLQGucWlw/content/pR1w36Da1K54.jpg')
            bot.send_message(message.chat.id, 'Это место жизненной силы и несомненного успеха. \nВ нашем центре Вы окунетесь в удивительный мир \nспокойствия, гармонии и релаксации. \nВ центре действует гибкая система скидок и услуга.' , reply_markup=vibor1)
    elif message.text == '📋Услуги и цены':
        if fit == 'fit':
            vibor2 = types.ReplyKeyboardMarkup(True, False)
            keyboards = types.InlineKeyboardMarkup(True)
            vibor2.row('⬅Назад')
            url_btn1 = types.InlineKeyboardButton(text='SPA-зона', url='http://tisida.com.ua/spa-zone')
            url_btn2 = types.InlineKeyboardButton(text='SPA-программы', url='http://tisida.com.ua/spa-program')
            url_btn3 = types.InlineKeyboardButton(text='Массажи', url='http://tisida.com.ua/massage')
            url_btn4 = types.InlineKeyboardButton(text='Занятия в воде ', url='http://tisida.com.ua/water_aerobics')
            url_btn5 = types.InlineKeyboardButton(text='Тренажерный зал', url='http://tisida.com.ua/gym')
            url_btn6 = types.InlineKeyboardButton(text='Сертификаты', url='http://tisida.com.ua/certificates')
            url_btn7 = types.InlineKeyboardButton(text='Правила посещения', url='http://tisida.com.ua/rules')

            keyboards.add(url_btn1, url_btn2, url_btn3, url_btn4, url_btn5, url_btn6, url_btn7)
            bot.send_message(message.chat.id, 'Что вам интересно?', reply_markup=vibor2)
            bot.send_message(message.chat.id, '📄', reply_markup=keyboards)
    elif message.text == '🕖Расписание работы':
        if fit == 'fit':
            vibor3 = types.ReplyKeyboardMarkup(True, False)
            vibor3.row('⬅Назад')
            bot.send_message(message.chat.id, 'Каждый день С 10:00 до 22:00', reply_markup=vibor3)
    elif message.text == '📞Связаться с нами':
        if fit == 'fit':
            vibor4 = types.ReplyKeyboardMarkup(True, False)
            vibor4.row('⬅Назад')
            bot.send_message(message.chat.id, 'Телефон - 095 800 7001 \nСайт - http://tisida.com.ua \nFacebook - https://www.facebook.com/spatisida/ \nПочта - tisidaspa13@gmail.com', reply_markup=vibor4)
    elif message.text == '⬅Назад':
        next2(message)







def next2(message):
    global fit
    fit = 'fit'
    vibor = types.ReplyKeyboardMarkup(True, False)
    vibor.row('💪О фитнес - центре')
    vibor.row('📋Услуги и цены')
    vibor.row('🕖Расписание работы')
    vibor.row('📞Связаться с нами')
    # Отправляем сообщение и отправляем подключение клавиатуры
    bot.send_message(message.chat.id, "Хорошо 🤝 " + message.from_user.first_name + ",чем могу помочь?", reply_markup=vibor)


bot.polling()






