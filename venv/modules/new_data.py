def new_data():
    lot = int(input('Справочник содержит ФИО, номер телефона и комментарий. Чтобы ввести все в одну строку введите 1. Если надо по строке на каждый тип данных - 0.'))
    print('')
    if lot == 1:
        data_for_file_0 = str(input('Укажите через запятую: ФИО, номер телефона, комментарий к внесенным данным: '))
        with open("database.txt","a", encoding='UTF-8') as file:
            file.write(f'\n{data_for_file_0}')
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