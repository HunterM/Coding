# 1. Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму 
# элементов списка, стоящих на нечётной позиции.

def summary(number: list[int]) -> int:
# на вход принимает целочисленное значение
    return sum(number[1::2])

import numpy as np # импорт из библиотеки  Numerical Python и присваиваем для сокращения np
lst = np.random.randint(-10, 10, 10) #выводим рандомный список из 10 чисел в промежутке от -10 до 10

print(f'Список элементов: ',lst)
print(f'Сумма нечетных элементов: ', summary(lst))