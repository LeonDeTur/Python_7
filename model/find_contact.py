# Модуль осуществляет поиск контакта пл имени или номеру телефона

import codecs

# Поиск по имени

def Find_by_name ():
    name = input('Введите имя: ')
    num_line_list =[]
    with codecs.open('C:/Users/thebe/OneDrive/Рабочий стол/GIT/Python/Python_7/data/phonebook.txt', 'r', 'utf-8') as phonebook:
        _ = 0
        for line in phonebook:
            _ += 1
            if name in line:
                num_line_list.append(_)
    
    return num_line_list

# Поиск по номеру телефона

def Find_by_name ():
    number = input('Введите имя: ')
    num_line_list =[]
    with codecs.open('C:/Users/thebe/OneDrive/Рабочий стол/GIT/Python/Python_7/data/phonebook.txt', 'r', 'utf-8') as phonebook:
        _ = 0
        for line in phonebook:
            _ += 1
            if number in line:
                num_line_list.append(_)
    
    return num_line_list
