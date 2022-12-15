import os
import random
import csv
# import logger


# print("Текущая деректория:", os.getcwd())
path = "D:/Coding/Coding/Sem151222/"
file = open("UsersFile.csv", "w", encoding='utf-8')

NewString = "ID; ||; NAME;||; TELEPHONE ;||; Должность ;||; E-mile\n"
file.writelines(NewString)


name_users = ['UserA', 'UserB', 'UserC',  'UserD',  'UserI',  'UserF', 'UserH', 'UserH',
              'UserW', 'UserY']
second_name = ['NameA', 'NameB', 'NameC', 'NameD',
               'NameI', 'NameF', 'NameH', 'NameK', 'NameN', 'NameO']
job_title = ['Менеджер', 'Директор', 'Стажер', 'Практикант',
               'Уборщик', 'Школьник']

emale_name = ['@gmail', '@mail', '@yandex', '@rambler']


def list_of_numbers():
    randomPhone = random.randint(7900000000, 8000000000)
    return str(randomPhone)


def skleyka_strok():
    skl = ""
    skl = (skl + ';' + random.choice(second_name) + ';' + random.choice(name_users) + ';' + list_of_numbers() + ';' 
          + random.choice(job_title) + ';' + random.choice(second_name) + random.choice(emale_name))
    return skl


def start():
    for i in range(20):
        stroka = f'{str(i + 1)},{skleyka_strok()}\n'
        file.write(stroka)
    file.close()

def newMass(base, result):
    base.remove(result)
    return base


def edit_str(base, result):
    base[base[base.index(result)].index(input('Введите элемент который хотите заменить'))] = input(f'Введите новое значение: ') #base.index вщзвращает результат
    return base



def read_stroka():
    my_lines = []
    with open('Coding\Sem151222\LecFile.csv', 'r') as f:
            for i in f:
                my_lines.append(i.split(';'))
    print(my_lines)

start()

# os.replace("UsersFile.csv", "D:/Coding/Coding/Sem151222/LecFile.csv")
file.close()
