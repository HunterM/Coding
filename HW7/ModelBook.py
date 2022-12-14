import os
import random
import csv
import logger


# print("Текущая деректория:", os.getcwd())

file = open("UsersFile.csv", "w")
NewString = "ID, NAME, TELEPHONE\n"
file.writelines(NewString)


name_users = ['UserA', 'UserB', 'UserC', 'UserD', 'UserI', 'UserF', 'UserH', 'UserH',
              'UserW', 'UserY']
second_name = ['NameA', 'NameB', 'NameC', 'NameD',
               'NameI', 'NameF', 'NameH', 'NameK', 'NameN', 'NameO']


def list_of_numbers():
    randomPhone = random.randint(7900000000, 8000000000)
    return str(randomPhone)


def skleyka_strok():
    skl = ""
    skl = skl + random.choice(second_name) + ',' + random.choice(name_users) + list_of_numbers()
    return skl


def start():
    for i in range(20):
        stroka = f'{str(i + 1)},{skleyka_strok()}\n'
        file.write(stroka)
    file.close()


start()

os.replace("UsersFile.csv", "D:/Coding/Coding/HW7/UsersFile.csv")
file.close()

# os.replace("UsersFile.txt", "D:\Coding\Coding\HW7\UsersFile.txt")
# ModelBook.close()


# with open("InstatFile.txt", "w") as a:
#     users_names1 = a.read()
#     users_names = []
#     users_names.append(users_names1)
#     print(users_names)