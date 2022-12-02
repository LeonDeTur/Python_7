# Модуль записывает данные в два отдельных текстовых файла

import codecs
from add_contact import *
from find_contact import *

# Запись Имени и телефона в текстовый файл

def Wright_in_phonebook():
    name = Get_Name()
    number = Get_phone_number()
    with codecs.open('C:/Users/thebe/OneDrive/Рабочий стол/GIT/Python/Python_7/data/phonebook.txt', 'a', 'utf-8') as phonebook:
        phonebook.write(name + ' ' + number + '\n')

# Запись имени в отдельный список

def Find_in_name():
    with codecs.open('C:/Users/thebe/OneDrive/Рабочий стол/GIT/Python/Python_7/data/phonebook.txt', 'r', 'utf-8') as phonebook:
        with codecs.open('C:/Users/thebe/OneDrive/Рабочий стол/GIT/Python/Python_7/data/names.txt', 'r', 'utf-8') as name:
            i = 0
            for line_1 in phonebook:
                i += 1
                for line_2 in name:
                    if line_1 == line_2:
                        return i
                    else:
                        return i

print(Find_in_name())
