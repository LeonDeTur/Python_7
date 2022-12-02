from view import init_phonebook as init

def init_txt():
    data = open('phonebook.txt', 'w+')
    data.close
    
init_txt()
init()
