# def ModelBook():
import os
import random
import csv
import logger



# print("Текущая деректория:", os.getcwd())

ModelBook = open("UsersFile.csv", "w")
NewString = "ID, NAME, TELEPHONE\n"
ModelBook.write(NewString)
# # ModelBook.write("In this place you can look instant contacts")
# # ModelBook.close()



# with open('UsersFile.txt', 'w') as data:
#     data.write('User1\n')
#     data.write('User2\n')
#     data.write('User3\n')
#     data.write('User4\n')
#     data.write('User5\n')
#     data.write('User6\n')
#     data.write('User7\n')
#     data.write('User8\n')
#     data.write('User9\n')
#     data.write('User10\n')
# ModelBook.close()
name_users = ['UserA', 'UserB', 'UserC', 'UserD', 'UserI', 'UserF', 'UserH', 'UserH',\
            'UserW', 'UserY']
second_name = ['NameA', 'NameB', 'NameC', 'NameD',\
                 'NameI', 'NameF', 'NameH', 'NameK', 'NameN', 'NameO']

def list_of_numbers():
    randomPhone = random.randint(7900000000, 8000000000)
    return str(randomPhone)

def skleyka_strok():
    skl = ""
    skl = skl + random.choice(second_name) + ','+ random.choice(name_users) + ',' + random.choice(list_of_numbers) + ',' + random.choice(second_name)
    return skl

def start():
    for i in range(20):
        stroka = f'{str(i+1)}, {skleyka_strok}\n'
        ModelBook.write(stroka)
    ModelBook.close()

start()

os.replace("UsersFile.csv", "D:/Coding/Coding/HW7/UsersFile.csv")
ModelBook.close()

# os.replace("UsersFile.txt", "D:\Coding\Coding\HW7\UsersFile.txt")
# ModelBook.close()


# with open("InstatFile.txt", "w") as a:
#     users_names1 = a.read()
#     users_names = []
#     users_names.append(users_names1)
#     print(users_names)


