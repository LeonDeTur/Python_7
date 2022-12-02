# Модуль принимает на вход данные(имя и номер телефона) и записывает их в текстовый файл

import codecs

# Ввод имени

def Get_Name(name):
    return name

# Ввод номера телефона

def Get_phone_number(phone_number):
    number = ''
    for _ in range(len(phone_number)):
        if phone_number[_].isdigit():
            number += phone_number[_]
        else:
            continue

    if len(number) == 11:
        return number
    else:
        return ''


    
