# # 1. Напишите программу, которая принимает на
# # вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# # Пример:
# # - 6 -> да
# # - 7 -> да
# # - 1 -> нет
# print('Введите число от 1 до 7')
# den = int(input())
# if den == 6 or den == 7:
#     print('Этот день - выходной')
#     if den==6:
#         print('А если быть точнее - суббота')
#     elif den==7:
#         print('А если быть точнее - воскресенье, и завтра на работу')
# else:
#     print('Вы ввели будний день')
#     print()
#     if den == 1:
#         print('А если быть точнее - понедельник')
#     elif den==2:
#         print('А если быть точнее - вторник')
#     elif den==3:
#         print('А если быть точнее - среда')
#     elif den==4:
#         print('А если быть точнее - четверг')
#     elif den==5:
#         print('Почти повезло, сегодня - пятница')

# print()


# # 2. Напишите программу для. проверки истинности 
# утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для 
# всех значений предикат. 
# ¬ - Отрицание ⋁ - логическое "Или" ⋀ - логическое "И"

print ('Введите число Х')
X3 = int(input())
print ('Введите число Y')
Y3 = int(input())
print ('Введите число Z')
Z3 = int(input())
if not (X3 or Y3 or Z3) == (not X3 and not Y3 and not Z3): 
    print ('Выражение истинно')
else:
    print('Выражение ложно')
print()




# # 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и
# # выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# # Пример:
# # - x=34; y=-30 -> 4
# # - x=2; y=4-> 1
# # - x=-34; y=-30 -> 3


# print('Введите координаты точки X и Y, причем координаты не равны 0')
# X = int(input())
# Y = int(input())
# if X ==0 or Y ==0:
#     print('Вы ввели недопустимые координаты')
# if X>0 and Y>0:
#     print('Точка находится в первой четверти')
# elif X>0 and Y<0:
#     print('Точка находится в четверной четверти')
# elif X<0 and Y<0:
#     print('Точка находится в третьей четверти')
# elif X<0 and Y>0:
#     print('Точка находится в второй четверти')

# print()


# # 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).


# print('Чтобы узнать диапазон координат введите номер четверти от 1 до 4')
# chet = int(input())
# if 1>chet>4:
#     print('Такой четверти не существует')
# if chet ==1:
#     print('Допустимые значения X и Y - больше 0')
# elif chet ==2:
#     print('В данной четверти X<0, а Y>0')
# elif chet==3:
#     print('В данной четверти X<0, а Y<0')
# elif chet==4:
#     print('В данной четверти X>0, а Y<0')

print()


# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


# import cmath
# import math
# print('Введите координату X первой точки')
# x1 = float(input())
# print('Введите координату Y первой точки')
# y1 = float(input())
# print('Введите координату X второй точки')
# x2 = float(input())
# print('Введите координату Y второй точки')
# y2 = float(input())
# vectorLenght = cmath.sqrt(((x2 - x1)**2)+((y2-y1)**2))
# #vectorLenght = round(vectorLenght, 2)
# print(f'Расстояние между точками = {vectorLenght}')
