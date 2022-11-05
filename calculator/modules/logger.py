import datetime
from datetime import datetime


def logs(data_from_user, command, result):
    current_datetime = datetime.now()
    temp = str(current_datetime)
    with open("log.txt", "a", encoding='windows-1251') as file:
        file.write(f'\n{temp} {", "} {data_from_user} {", "} {command} {", "} {result}')



