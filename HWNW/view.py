import os
import random
import model
from os import system
system("cls")

path = "D:/Coding/Coding/HWNW/UsersFile.csv"
file = open("UsersFile.csv", "w", encoding="utf-8")

NewString = "ID || NAME || SecondName || TELEPHONE || Email || Должность\n"
file.writelines(NewString)

def choice_mode():
    return input(f'Введите режим работы: 1 - добавление, 2 - поиск, 3 - редактирование, 4 - удаление, 5 - показать все, 0 - выход')

def addcontact():
    # id = int(base[len(base)-1][0])+1
    name = input('Введите имя: ')
    secondname = input('Введите фамилию: ')
    phonenumber = input('Введите телефон: ')
    email = input('Введите почтовый ящик: ')
    options = input('Введите должность: ')
    return f'{name} || {secondname} || {phonenumber} || {email} || {options}'

file.close()

def contact_to_s():
    return input('Введите информацию для поиска')


# def start():    
#     for i in range(100):
#         stroka =  f'{str(i+1)}, {skleyka_strok()}\n'
#         file.write(stroka)

def showcontact(position):
    show = ""
    for i in position:
        show += str(i) + " "
    print(show)


def findcontact(base, contact):
    base = base.split('\n')
    flag = True
    results = []
    for i in base:
        if contact in i:
            flag = False
            results.append(i)
    if flag:
        results.append(f'Контакт |{contact}| не найден')
    return results


# def deletecontact(base):
#     findcontact(base)
#     findid = input('Введите id контакта к удалению: ')
#     for contact in base:
#         if findid in contact:
#             base.remove(contact)

# def correctcontact(base):
#     contact_to_s(base)
#     id = input('Введите id контакта, которое нужно исправить: ')
#     for contact in base:
#         if id in contact:
#             command = input("Выберите что хотите изменить(1 - имя, 2 - фамилию, 3 - телефон, 4 - почту, 5 - должность): ")
            
#             matсh command.split():
#                 case ["1"]: contact[1] = input('Введите имя')
#                 case ["2"]: contact[1] = input('Введите фамилию')
#                 case ["3"]: contact[1] = input('Введите телефон')
#                 case ["4"]: contact[1] = input('Введите email')
#                 case ["5"]: contact[1] = input('Введите должность')

