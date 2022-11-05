import telebot
from telebot import TeleBot
from modules.addition import addition
from modules.subtraction import subtraction
from modules.multiplication import multiplication
from modules.degree import degree


bot = TeleBot('5492834496:AAG2wn4wbnWNpAWfYcBf9M8sx3NNMEAsFKg')


@bot.message_handler(commands=['start'])
def first_message(message):
    bot.send_message(message.chat.id,
                     text=(f'Калькулятор запущен. \n'
                           '\n'
                           '/addition - сложение\n'
                           '/subtraction - вычитание\n'
                           '/multiplication - умножение\n'
                           '/degree - деление\n'
                           '/log - получить файл с историей операций'
                           '\n'
                           'В комплексных числах дробную часть необходимо отделять запятой, не точкой.\n '
                           '\n'
                           'Выберите команду.'))


@bot.message_handler(commands=['addition'])
def edit_one_line(message: telebot.types.Message):
    next_message = bot.send_message(chat_id=message.from_user.id, text='Укажите через пробел два числа для сложения' )
    bot.register_next_step_handler(callback=addition(message.text), message=next_message)
    bot.send_message(chat_id=message.from_user.id, text='Готово')


@bot.message_handler(commands=['log'])
def bot_export_data(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id,
                     text='Держи логи, только не помни')
    bot.send_document(chat_id=msg.from_user.id, document=open('log.txt', 'rb'))


bot.polling()