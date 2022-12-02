# Интерефейс телефонной книги

from tkinter import *
from tkinter import scrolledtext
import codecs  

def clicked():
    search_by_name_lbl.configure(text = "Поиск по ФИО: ")

window = Tk()
window.title('Телефонная книга')
window.geometry('720x480')

# Кнопка поиска по имени

search_by_name_lbl = Label(window, text = 'Поиск по ФИО: ', font=('TimesNewRoman', 12))
search_by_name_lbl.grid(column = 0, row = 0)

search_by_name = Entry(window, width = 25, state = 'normal')
search_by_name.grid(column = 1, row = 0)
search_by_name.focus

search_by_name_btn = Button(window, text = 'Искать', command = clicked, bg = 'white', fg = 'black')
search_by_name_btn.grid(column = 2, row = 0)

# Кнопка поиска по номеру телефона

search_by_phone_lbl = Label(window, text = 'Поиск по номеру: ', font=('TimesNewRoman', 12))
search_by_phone_lbl.grid(column = 3, row = 0)

search_by_phone = Entry(window, width = 15, state = 'normal')
search_by_phone.grid(column = 4, row = 0)
search_by_phone.focus

search_by_phone_btn = Button(window, text = 'Искать', command = clicked, bg = 'white', fg = 'black')
search_by_phone_btn.grid(column = 5, row = 0)

# Загловок ФИО
name_lbl = Label(window, text = 'ФИО: ', font=('TimesNewRoman', 12))
name_lbl.grid(column = 0, row = 2)

# Заголовок номера

phone_number_lbl = Label(window, text = 'Номер телефона: ', font=('TimesNewRoman', 12))
phone_number_lbl.grid(column = 1, row = 2)

# Вывод списка номеров и телефонов
result_list = scrolledtext.ScrolledText(window,width=50,height=20)
result_list.grid(column = 0, row = 3)

with codecs.open('C:/Users/thebe/OneDrive/Рабочий стол/GIT/Python/Python_7/data/phonebook.txt', 'r', 'utf-8') as data:
    result_list.insert(0.0, data.read())

# Кнопка добавления контакта

add_phone_phone_btn = Button(window, text = 'Добавить', command = clicked, bg = 'white', fg = 'black')
add_phone_phone_btn.grid(column = 0, row = 4)


window.mainloop()