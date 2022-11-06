import telebot
from telebot import TeleBot
from modules.addition import addition
from modules.subtraction import subtraction
from modules.multiplication import multiplication
from modules.degree import degree
from modules.logger import logs


bot = TeleBot('5492834496:AAG2wn4wbnWNpAWfYcBf9M8sx3NNMEAsFKg')


@bot.message_handler(commands=['start'])
def first_message(message):
    bot.send_message(message.chat.id,
                     text=(f'Вас привествует дружелюбное отродье монстра Франкенштейна, притворяющееся калькулятором!.\n'
                           '\n'
                           'Калькулятор не работает с комплексными числами разных типов. '
                           'То есть не должно быть разных переменных в виде букв.\n'
                           'Для выполнения операций одного типа можно вводить более двух чисел.\n'
                           'Указывать через пробел, вот так: 512 6 17 32,134 8j 11 5j.\n'
                           '\n'
                           'Для умножения и деления комплексные числа необходимо указывать в таком формате:'
                           '-3+4j \n'
                           '\n'
                           '/start - вызов главного меню\n'
                           '/additions - сложение\n'
                           '/subtractions - вычитание\n'
                           '/multiplications - умножение\n'
                           '/degrees - деление\n'
                           '/logs - получить файл с историей операций\n'
                           '\n'
                           'Выберите команду.'))


@bot.message_handler(commands=['additions'])
def additions(message: telebot.types.Message):
    bot.send_message(chat_id=message.from_user.id, text='Укажите через пробел числа для сложения')
    bot.register_next_step_handler(callback=additions_result_send, message=message)


def additions_result_send(message: telebot.types.Message):
    bot.send_message(chat_id=message.from_user.id, text=addition(message.text))
    logs(message.text, 'additions', addition(message.text))


@bot.message_handler(commands=['subtractions'])
def subtractions(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text='Укажите через пробел числа для вычитания')
    bot.register_next_step_handler(callback=subtractions_result_send, message=msg)


def subtractions_result_send(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=subtraction(msg.text))
    logs(msg.text, 'subtractions', subtraction(msg.text))


@bot.message_handler(commands=['multiplications'])
def multiplications(message: telebot.types.Message):
    bot.send_message(chat_id=message.from_user.id, text='Укажите через пробел числа для умножения')
    bot.register_next_step_handler(callback=multiplications_result_send, message=message)


def multiplications_result_send(message: telebot.types.Message):
    bot.send_message(chat_id=message.from_user.id, text=multiplication(message.text))
    logs(message.text, 'multiplication', multiplication(message.text))


@bot.message_handler(commands=['degrees'])
def degrees(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text='Укажите через пробел числа для деления')
    bot.register_next_step_handler(callback=degrees_result_send, message=msg)


def degrees_result_send(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=degree(msg.text))
    logs(msg.text, 'degrees', degree(msg.text))


@bot.message_handler(commands=['logs'])
def bot_export_data(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id,
                     text='Держи логи, только не помни')
    bot.send_document(chat_id=msg.from_user.id, document=open('log.txt', 'rb'))


bot.polling()
