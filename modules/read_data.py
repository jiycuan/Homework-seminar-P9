def read_data():
    with open("database.txt", "r", encoding='UTF-8') as file:
        data = file.read()
        return data
