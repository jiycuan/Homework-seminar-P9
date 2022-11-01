def export_data():
    with open("database.txt", "r", encoding='UTF-8') as file:
        data = file.read()
    data = data.replace('\n', '')
    data = data.split(', ')
    data_result = data[0]
    count = 1

    lot = int(input('Если построковое отображение нужно разбить по пунктам - нажмите 1. Если требуется объединение всех данных о кадре в одну строку - нажмите 0. '))
    if lot == 1:
        for i in range(1, len(data) - 1):
            data_result = data_result + ('\n') + str(data[i])
            count = count + 1
            if count % 3 == 0:
                data_result = data_result + ('\n')
    else:
        data_result = data_result + (', ')
        for i in range(1, len(data) - 1):
            data_result = data_result + str(data[i]) + (', ')
            count = count + 1
            if count % 3 == 0:
                data_result = data_result + ('\n')
    export_file = open("../export_result.txt", "w")
    export_file.write(data_result)
    export_file.close()
    print('Готово! Данные выгружены в файл "export_result"')