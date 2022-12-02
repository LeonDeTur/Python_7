from view import init_phonebook as init
import os

def init_txt():
    data = open('phonebook.txt', 'w+')
    data.close
    
if os.path.isfile('phonebook.txt') != True:
    init_txt()

init()
