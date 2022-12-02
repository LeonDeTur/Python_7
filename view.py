# Интерефейс телефонной книги

from tkinter import *
from tkinter import scrolledtext
import codecs  
from controller import *
from tkinter import ttk
from tkinter import messagebox

def init_phonebook():

    # Основное окно

    window = Tk()
    window.title('Телефонная книга')
    window.geometry('720x480')

    # Вывод списка номеров и телефонов

    result_list = scrolledtext.ScrolledText(window,width=70,height=20)
    result_list.grid(column = 0, row = 3, columnspan=6)

    def clicked_name_search():
        inp = search_by_name.get()
        name_search(inp)

        with codecs.open('tmp_list', 'r', 'utf-8') as tmp_data:
            result_list.insert(0.0, tmp_data.read())

        return


    def clicked_phone_search():
        inp = search_by_phone.get()
        phone_search(inp)

        with codecs.open('tmp_list', 'r', 'utf-8') as tmp_data:
            result_list.insert(0.0, tmp_data.read())

        return

    def clicked_add():
        name_inp = add_name.get()
        phone_inp = add_phone.get()
        if Wright_data(name_inp, phone_inp) != 0:
            messagebox.showinfo('Добавление контакта', 'Контакт успешно записан')
        else:
            messagebox.showinfo('Добавление контакта', 'Ошибка: Введите номер из 11 цифр')
        with codecs.open('phonebook.txt', 'r', 'utf-8') as data:
            result_list.insert(0.0, data.read())
        
        return


    # Кнопка поиска по имени

    search_by_name_lbl = Label(window, text = 'Поиск по ФИО: ', font=('TimesNewRoman', 12))
    search_by_name_lbl.grid(column = 0, row = 0)

    search_by_name = ttk.Entry(window, width = 25, state = 'normal')
    search_by_name.grid(column = 1, row = 0)
    search_by_name.focus

    search_by_name_btn = ttk.Button(window, text = 'Искать', command = clicked_name_search)
    search_by_name_btn.grid(column = 2, row = 0)

    # Кнопка поиска по номеру телефона

    search_by_phone_lbl = Label(window, text = 'Поиск по номеру: ', font=('TimesNewRoman', 12))
    search_by_phone_lbl.grid(column = 3, row = 0)

    search_by_phone = ttk.Entry(window, width = 20, state = 'normal')
    search_by_phone.grid(column = 4, row = 0)
    search_by_phone.focus

    search_by_phone_btn = ttk.Button(window, text = 'Искать', command = clicked_phone_search)
    search_by_phone_btn.grid(column = 5, row = 0)

    # Загловок ФИО
    name_lbl = Label(window, text = 'ФИО: ', font=('TimesNewRoman', 12))
    name_lbl.grid(column = 0, row = 2)

    # Заголовок номера

    phone_number_lbl = Label(window, text = 'Номер телефона: ', font=('TimesNewRoman', 12))
    phone_number_lbl.grid(column = 2, row = 2)

    # Вывод списка номеров и телефонов
    result_list = scrolledtext.ScrolledText(window,width=70,height=20)
    result_list.grid(column = 0, row = 3, columnspan=6)

    with codecs.open('phonebook.txt', 'r', 'utf-8') as data:
        result_list.insert(0.0, data.read())

    # Кнопка добавления контакта

    add_phone_phone_btn = Button(window, text = 'Добавить', command = clicked_add, bg = 'white', fg = 'black')
    add_phone_phone_btn.grid(column = 0, row = 4)

    # Загловок добавления ФИО
    name_lbl = Label(window, text = 'ФИО: ', font=('TimesNewRoman', 12))
    name_lbl.grid(column = 1, row = 4)

    # Строка добавления ФИО

    add_name = ttk.Entry(window, width = 25, state = 'normal')
    add_name.grid(column = 2, row = 4)
    add_name.focus

    # Заголовок добавления номера

    phone_number_lbl = Label(window, text = 'Номер телефона: ', font=('TimesNewRoman', 12))
    phone_number_lbl.grid(column = 3, row = 4)

    # Строка добавления номера

    add_phone = ttk.Entry(window, width = 20, state = 'normal')
    add_phone.grid(column = 4, row = 4)
    add_phone.focus

    window.mainloop()