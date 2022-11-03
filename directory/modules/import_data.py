def import_data():
    with open("import_data.txt", "r") as file:
        data = file.read()
    export_file = open("database.txt", "a")
    export_file.write(data)
    export_file.close()

