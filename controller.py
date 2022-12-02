import codecs
from model.add_contact import *
from model.find_contact import Find_by_name
from model.find_contact import Find_by_phone

def name_search(name):
    string_result_list = Find_by_name(name)

    with codecs.open('phonebook.txt', 'r', 'utf-8') as data:
        data = data.readlines()
        tmp_data = codecs.open('tmp_list', 'w+', 'utf-8')
        for _ in range(len(string_result_list)):
            i = string_result_list[_]
            tmp_data.write(data[i-1] + '\n')
        tmp_data.close
    return

def phone_search(phone):
    string_result_list = Find_by_phone(phone)

    with codecs.open('phonebook.txt', 'r', 'utf-8') as data:
        data = data.readlines()
        tmp_data = codecs.open('tmp_list', 'w+', 'utf-8')
        for _ in range(len(string_result_list)):
            i = string_result_list[_]
            tmp_data.write(data[i-1] + '\n')
        tmp_data.close
    return
    
# Запись Имени и телефона в текстовый файл

def Wright_data(name, number):
    name = Get_Name(name)
    number_checked = Get_phone_number(number)
    if number_checked != '':
        data = codecs.open('phonebook.txt', 'a', 'utf-8')
        data.write('\n' + name + ' ' + number_checked)
        data.close
        return 1
    else:
        return 0
    