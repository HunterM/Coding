from funct import create_polinom_file #копируем функцию из funct.py
from funct import create_polinom #копируем функцию из funct.py
from sympy import simplify #импортируем встроенную библиотеку

print(f'Введите коэффициент первого полинома')
k = int(input()) # вводим первый коэффициент
print(f'Введите коэффициент второго полинома')
n = int(input()) # вводим второй коэффициент

print(f'Сгенерированный полином {create_polinom(k)}')
print(f'Сгенерированный полином {create_polinom(n)}')
pol1 = create_polinom_file(create_polinom(k), 'FirstfileFiveTask') #создали 1 файл
pol2 = create_polinom_file(create_polinom(n), 'SecondfileFiveTasks') #создали 2 файл

sumFile = 'SumPolinom' #присвоили 3 файл имя
file1 = 'FirstfileFiveTask'
file2 = 'SecondfileFiveTasks'

create_polinom_file(pol1, file1)
create_polinom_file(pol2, file2)


with open(f'coding/HW4/{file1}.txt', 'r') as f1:
    f_pol= f1.read()
with open(f'coding/HW4/{file2}.txt', 'r') as f2:
    f_pol= f2.read()    

sumpolinom = simplify(file1 + '+' + file2)
sumpolinom = str(sumpolinom)

print(f'Сумма полиномов {sumpolinom}')


with open(f'coding/HW4/{sumFile}.txt', 'w') as s:
    s.write(sumpolinom)