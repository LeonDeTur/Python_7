# Модуль принимает на вход данные(имя и номер телефона) и записывает их в текстовый файл

import codecs

# Ввод имени

def Get_Name():
    name = input('Введите ФИО: ')
    return name

# Ввод номера телефона

def Get_phone_number():
    phone_number = input('Введите номер телефона(11 цифр): ')
    number = ''
    for _ in range(len(phone_number)):
        if phone_number[_].isdigit():
            number += phone_number[_]
        else:
            continue

    if len(number) == 11:
        return number
    else:
        return 'Вы ввели не 11 цифр. Пожалуйста, введите номер из 11 цифр.'

# Запись Имени и телефона в текстовый файл

def Wright_data():
    name = Get_Name()
    number = Get_phone_number()
    data = codecs.open('C:/Users/thebe/OneDrive/Рабочий стол/GIT/Python/Python_7/data/phonebook.txt', 'a', 'utf-8')
    data.write(name + ' ' + number + '\n')
    data.close

    
