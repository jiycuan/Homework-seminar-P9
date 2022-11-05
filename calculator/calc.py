import telebot
from telebot import TeleBot
from modules.addition import addition
from modules.logger import logs


bot = TeleBot('5492834496:AAG2wn4wbnWNpAWfYcBf9M8sx3NNMEAsFKg')


@bot.message_handler(commands=['start'])
def first_message(message):
    bot.send_message(message.chat.id,
                     text=(f'Калькулятор запущен. \n'
                           '\n'
                           '/additions - сложение\n'
                           '/subtractions - вычитание\n'
                           '/multiplications - умножение\n'
                           '/degrees - деление\n'
                           '/logs - получить файл с историей операций'
                           '\n'
                           'Дробную часть числа необходимо отделять точкой, не запятой.\n '
                           '\n'
                           'Выберите команду.'))


@bot.message_handler(commands=['additions'])
def additions(message: telebot.types.Message):
    bot.send_message(chat_id=message.from_user.id, text='Укажите через пробел числа для сложения')
    bot.register_next_step_handler(callback=additions_result_send, message=message)


def additions_result_send(message: telebot.types.Message):
    bot.send_message(chat_id=message.from_user.id, text=addition(message.text))
    logs(message.text, 'additions', addition(message.text))


@bot.message_handler(commands=['logs'])
def bot_export_data(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id,
                     text='Держи логи, только не помни')
    bot.send_document(chat_id=msg.from_user.id, document=open('log.txt', 'rb'))


bot.polling()
