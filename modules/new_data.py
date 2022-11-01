def new_data(lot, data_for_file):
    if lot == 1:
        with open("database.txt","a", encoding='UTF-8') as file:
            file.write(f'\n{data_for_file}')
    else:
        data_for_file = str(input('Укажите ФИО: '))
        with open("database.txt","a", encoding='UTF-8') as file:
            file.write(f'\n{data_for_file}')
        data_for_file_1 = str(input('Укажите номер телефона: '))
        with open("database.txt","a", encoding='UTF-8') as file:
            file.write(f'\n{data_for_file_1}')
        data_for_file_2 = str(input('Укажите комментарий: '))
        with open("database.txt","a", encoding='UTF-8') as file:
            file.write(f'\n{data_for_file_2}')
            file.write('\n')