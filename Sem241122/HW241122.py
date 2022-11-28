# 1. Напишите программу, которая принимает на
# вход вещественное число и показывает сумму
# его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# print('Введите вещественное число:\n')
# number =  float(input())
# str1=str(number)
# print(str1)
# sum=0
# for element in str1:
#     if element.isdigit():
#         sum += int(element)
#         print(element)
# print("Сумма цифр равна: " ,sum)


# 2. Напишите программу, которая принимает на
# вход число N и выдает набор произведений
# чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# import math

# def mult(n: int) -> str:

#     str_mult = '1'
#     for i in range(2, n+1):
#         if i ==n:
#             str_mult += f'*(i)'
#         else:
#             str_mult += f'*(i)'
#         return

# n = int(input('Num:'))
# multiplications = 

###############################################


# print("Введите число N")
# print()
# numberN = int(input())
# str2 = list(range(1, numberN+1))
# print()

# for i in str2:
#     print(i**2, end=" ")
# print()


# 3. Задайте список из n чисел последовательности (1+1/n)^n
# и выведите на экран их сумму.
# Пример:
# - Для n = 6: [2.0, 2.25, 2.37037037037037, 2.44140625, 2.4883199999999994, 2.5216263717421135]

# print('Введите число N')
# chislo = int(input())
# for i in range(1, chislo+1):
#     lst = [((1+1/i)**i)]
#     print(sum(lst), end=" ")
# print()

# 4. Задайте список из N элементов, заполненных числами из промежутка
# [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
# (для продвинутых - с файлом, вариант минимум -
# ввести позиции в консоли)
#  -2 -1 0 1 2 Позиции: 0,1 -> 2

# path = 'THW241122.txt'
# data = open(path, 'r')
# for line in data:
#     print(line) #занести в список
# data.close()
# # exit()


# print("Введите число N")
# print()
# n1 = int(input())
# str3 = list(range(- n1, n1+1))
# s = len(str3)

# print(str3)
# print(len(str3))
# print("Введите позиции для подсчета из диапазона от 0 до", s-1)

# a = list(map(int, input().split()))
# print(a)
# proiz = 0
# for i in a:
#     proiz *= str3[i]
# print(proiz)
# poz1 = int(input())
# poz2 = int(input())

# for i in range(0, s-1):
#     if s < a[i] or a[i] < 0 or 0 > a[i] or a[i] > s:
#         print("Элементы вне допустимого диапазона")
    # elif poz1 > 0 or poz1 < s or poz2 < s and poz2 > 0:
    #     proiz = str3[poz1]*str3[poz2]
    #     print('Результат равен: ', proiz)
    #     break


# for i in range(0, s-1):
#     if s < poz1 or poz1 < 0 or 0 > poz2 or poz2 > s:
#         print("Элементы вне допустимого диапазона")
#     elif poz1 > 0 or poz1 < s or poz2 < s and poz2 > 0:
#         proiz = str3[poz1]*str3[poz2]
#         print('Результат равен: ', proiz)
#         break


# 5.Реализуйте алгоритм перемешивания списка.

# import random
# listRandom = ['a', 'b', 'c', 'd', 'e']
# random.shuffle(listRandom)
# print(listRandom)
