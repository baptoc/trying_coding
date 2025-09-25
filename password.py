name = input("Задайте имя: ")
password = input('Задайте пароль: ')
while 1 == 1:
    nameguess=''
    passwordguess=''
    key=''
    while (nameguess != name) or (passwordguess != password):
        nameguess = input('Имя? ')
        passwordguess = input('Пароль? ')
    print('Добро пожаловать,', name, '. Введите lock, чтобы заблокировать.')
    while key != 'lock':
        key = input('')