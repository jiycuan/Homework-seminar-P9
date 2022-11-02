import telebot
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
                           '/read - посмотреть справочник\n'
                           '/edit - внести новые данные в справочник\n'
                           '/export - получить справочник в виде файла\n'
                           '/import - прислать файл, данные из которого попадут в справочник\n'
                           '\n'
                           'Выберите команду'))


@bot.message_handler(commands=['read'])
def bot_read_data(message):
    bot.send_message(message.chat.id,
                     text=read_data())


@bot.message_handler(commands=['edit'])
def bot_edit_data(message):
    bot.send_message(message.chat.id,
                     text='Справочник содержит ФИО, номер телефона и комментарий. \n'                          
                          'В каком формате будете вносить данные? \n'
                          '/one_line - чтобы указать через запятую: ФИО, телефон, комментарий \n'
                          '/three_lines - каждый пункт займет отдельную строчку в файле\n')


@bot.message_handler(commands=['one_line'])
def edit_one_line(message: telebot.types.Message):
    next_message = bot.send_message(chat_id=message.from_user.id, text='Укажите через запятую: ФИО, номер, комментарий:' )
    bot.register_next_step_handler(callback=new_data_one, message=next_message)


def new_data_one(message):
    new_data(1, message.text)


@bot.message_handler(commands=['three_lines'])
def edit_three_lines(message):
    next_message = bot.send_message(chat_id=message.from_user.id, text='Укажите через запятую: ФИО, номер, комментарий:' )
    bot.register_next_step_handler(callback=new_data_three, message=next_message)


def new_data_three(message):
    new_data(0, message.text)


@bot.message_handler(commands=['import'])
def bot_import_data(msg):
    file = bot.get_file(msg.document.file_id)
    downloaded_file = bot.download_file(file.file_path)
    path = "export/" + msg.document.file_name
    with open(path, "wb") as f_out:
        f_out.write(downloaded_file)
    import_interface(path)
    bot.send_message(chat_id=msg.from_user.id, text="Данные импортированы")


@bot.message_handler(commands=['export'])
def bot_export_data(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id,
                     text='Справочник Акеруса в виде файла! Чудеса да и только')
    bot.send_document(chat_id=msg.from_user.id, document=open('database.txt', 'rb'))


bot.polling()

