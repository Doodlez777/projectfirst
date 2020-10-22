
import time
import telebot
from telebot import types # кнопки
from string import Template

bot = telebot.TeleBot('1277655533:AAGQTmPqq6l83lMAIAGqUzG_vEKeVshZCjo')

user_dict = {}

class User:
    def __init__(self, city):
        self.city = city

        keys = ['fullname', 'phone', 'timeuser',
                'menu', 'taste']


        for key in keys:
            self.key = None

# если /help, /start
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('/about')
    itembtn2 = types.KeyboardButton('/smoke')
    itembtn3 = types.KeyboardButton('/discounts')
    markup.add(itembtn1, itembtn2, itembtn3)

    bot.send_message(message.chat.id, "Здравствуйте 🤝 "
    + message.from_user.first_name
    + ",\n Я 🤖 Кальянный Инспектор", reply_markup=markup)

# /about
@bot.message_handler(commands=['about'])
def send_about(message):
	bot.send_message(message.chat.id, '🕵️‍♂️Кальянный  Инспектор ждет Вас в заведении РЦ «Taler» и в кальян-баре «Модная Бочка» \n🧾Прокачиваем кальяны, снимаем развлекательный контент, производим кальяны Дымная Пушка \n👇ПРОДАЖА товаров для Дымных 🛍  \n http://h-inspector.com/')


@bot.message_handler(commands=['discounts'])
def send_discounts(message):
    bot.send_message(message.chat.id, '💨Дымный Понедельник - кальян классический 80 грн \n😤Среда 1+1 - 2 классических кальяна по цене 1го \n👨‍👩‍👧‍👧Для любителей много дымить - призаказе 2х кальянов, 3й в подарок!')




# /smoke
@bot.message_handler(commands=["smoke"])
def user_reg(message):
       markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
       itembtn1 = types.KeyboardButton('Таллер')

       markup.add(itembtn1)

       msg = bot.send_message(message.chat.id, 'Где хотите покурить?', reply_markup=markup)
       bot.register_next_step_handler(msg, process_city_step)

def process_city_step(message):
    try:
        chat_id = message.chat.id
        user_dict[chat_id] = User(message.text)

        # удалить старую клавиатуру
        markup = types.ReplyKeyboardRemove(selective=False)

        msg = bot.send_message(chat_id, 'Ваше имя', reply_markup=markup)
        bot.register_next_step_handler(msg, process_fullname_step)

    except Exception as e:
        bot.reply_to(message, 'ooops!!')

def process_fullname_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.fullname = message.text

        msg = bot.send_message(chat_id, 'Ваш номер телефона')
        bot.register_next_step_handler(msg, process_phone_step)

    except Exception as e:
        bot.reply_to(message, 'ooops!!')

def process_phone_step(message):
    try:


        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.phone = message.text

        msg = bot.send_message(chat_id, 'Через сколько вы будете?')
        bot.register_next_step_handler(msg, process_timeuser_step)

    except Exception as e:
        msg = bot.reply_to(message, 'Вы ввели что то другое. Пожалуйста введите номер телефона.')
        bot.register_next_step_handler(msg, process_phone_step)

def process_timeuser_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.timeuser = message.text

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Кальян классический 145 грн')
        itembtn2 = types.KeyboardButton('Кальян премиум light  170 грн')
        itembtn3 = types.KeyboardButton('Кальян премиум strong 200 грн')

        for item in [itembtn1, itembtn2, itembtn3]:
            markup.add(item)



        msg = bot.send_message(chat_id, 'Меню: ', reply_markup=markup)
        bot.register_next_step_handler(msg, process_menu_step)

    except Exception as e:
        bot.reply_to(message, 'ooops!!')

def process_menu_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.menu = message.text

        msg = bot.send_message(chat_id, 'Какой вкус?')
        bot.register_next_step_handler(msg, process_taste_step)

    except Exception as e:
        bot.reply_to(message, 'ooops!!')

def process_taste_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.taste = message.text

        bot.send_message(chat_id, getRegData(user, 'Ваш заказ', message.from_user.first_name), parse_mode="Markdown")

        time.sleep(1)

        bot.send_message(chat_id, 'Спасибо, мы вас ждем 👍')

        bot.send_message('@chat_hookahh', getRegData(user, 'Заявка от бота', bot.get_me().username), parse_mode="Markdown")





    except Exception as e:
        bot.reply_to(message, 'ooops!!')









# формирует вид заявки регистрации
# нельзя делать перенос строки Template
# в send_message должно стоять parse_mode="Markdown"
def getRegData(user, title, name):
    t = Template('$title *$name* \n Место: *$userCity* \n Имя: *$fullname* \n Телефон: *$phone* \n Время: *$timeuser* \n Меню: *$menu* \n Вкус: *$taste* ')

    return t.substitute({
        'title': title,
        'name': name,
        'userCity': user.city,
        'fullname': user.fullname,
        'phone': user.phone,
        'timeuser': user.timeuser,
        'menu': user.menu,
        'taste': user.taste,








    })

# произвольный текст
@bot.message_handler(content_types=["text"])
def send_help(message):
    bot.send_message(message.chat.id, 'О нас - /about\nПокурить - /smoke\nПомощь - /help')





if __name__ == '__main__':
    bot.polling(none_stop=True)
