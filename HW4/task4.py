# #  Задана натуральная степень k. С
# # формировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# # Пример:
# # k=2 => 2*x*2 + 4*x + 5 = 0 или x2 + 5 = 0 или 10*x*2 = 0
# # k=3 => 2*x*3 + 4*x*2 + 4*x + 5 = 0 5'. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# # В file1.txt :
# # 2*x**2 + 4*x + 5
# # В file2.txt:
# # 4*x**2 + 1*x + 4
# # Результирующий файл:
# # 6*x**2 + 5*x + 9

# from funct import create_polinom_file
# from funct import create_polinom

# k =  int(input())
# # n = int(input())

# print(f'Сгенерированный полином {create_polinom(k)}')
# create_polinom_file(create_polinom(k), 'fileForTask')
# # create_polinom_file(create_polinom(k), 'fileFiveTasks')