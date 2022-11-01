
from telebot import TeleBot
from modules.read_data import read_data
from modules.new_data import new_data
from modules.export_data import export_data
from modules.import_data import import_data


bot = TeleBot('5771267528:AAEpt6yUkxZcavAtrnYz7PLlgrM9eqCa6sI')

@bot.message_handler(commands=['start'])
def first_message(message):
    bot.send_message(message.chat.id,
                     text=(f'Это телефонный справочник "ДТП Акеруса"! Вот список команд: \n'
                           '\n'
                           '/read \n'
                           '/edit \n'
                           '/export \n'
                           '/import \n'
                           '\n'
                           'Выберите команду'))


@bot.message_handler(commands=['read'])
def bot_read_data(message):
    bot.send_message(message.chat.id,
                     text='Мне очень больно')


@bot.message_handler(commands=['edit'])
def bot_edit_data(message):
    bot.send_message(message.chat.id,
                     text='Мне правда очень больно')


@bot.message_handler(commands=['export'])
def bot_export_data(message):
    bot.send_message(message.chat.id,
                     text='Мне действительно очень больно')


@bot.message_handler(commands=['import'])
def bot_import_data(message):
    bot.send_message(message.chat.id,
                     text='Мне очень-очень больно')


bot.polling()

