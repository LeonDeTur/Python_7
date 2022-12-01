# Модуль принимает на вход данные(имя и номер телефона) и записывает их в текстовый файл

def Get_Name():
    name = input('Введите ФИО: ')
    return name

def Get_phone_number():
    phone_number = input('Введите номер телефона(8 цифр): ')
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
    
def Wright_data():
    name = Get_Name()
    number = Get_phone_number()
    wright = open('C:\Users\thebe\OneDrive\Рабочий стол\GIT\Python\Python_7\data')
