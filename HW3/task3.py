# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной 
# части элементов.

lst2 = list(map(float, input("Введите вещественные числа через запятую:\n").split(',')))
new_lst2 = [round(i%1,2) for i in lst2 if i%1 != 0]
print(f'Разница между максимальным и минимальным дробным значиением =', max(new_lst2) - min(new_lst2))