from modules.read_data import read_data
from modules.new_data import new_data
from modules.export_data import export_data
from modules.import_data import import_data


def verify():
    number = input("Укажите пункт меню: ")
    if number.isdigit():
        number = int(number)
    else:
        print("Неверный ввод, повторите попытку")
        verify()
    return number


def ui():

    while True:
        print("")
        print("Какой будет следующая операция?")

        number = verify()
        if number not in [1, 2, 3, 4]:
            print("Неверный ввод, повторите попытку")
            number = verify()

        if number == 1:
            read_data()

        if number == 2:
            new_data()

        if number == 3:
            export_data()

        if number == 4:
            import_data()