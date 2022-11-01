def import_data():
    with open("export_result.txt", "r", encoding='UTF-8') as file:
        data = file.read()
    export_file = open("database.txt", "w")
    export_file.write(data)
    export_file.close()