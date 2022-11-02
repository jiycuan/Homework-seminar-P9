def export_data():
    with open("database.txt", "r", encoding='UTF-8') as file:
        data = file.read()
    data = data.replace('\n', '')
    data = data.split(', ')
    data_result = data[0]
    count = 1

    for i in range(1, len(data) - 1):
        data_result = data_result + ('\n') + str(data[i])
        count = count + 1
        if count % 3 == 0:
            data_result = data_result + ('\n')

    export_file = open("../export_result.txt", "w")
    export_file.write(data_result)
    export_file.close()