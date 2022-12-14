# Напишите программу, которая будет преобразовывать 
# десятичное число в двоичное.


s = ""
n = int(input("Введите число:\n"))
while n != 0:
    s = str(n%2) + s
    n //=2
print(f'Число в двоичном коде =', s)


n = int(input("Введите число:\n"))
result = bin(n)
result = result[2:]
print (f'{n} in binary form: {result}')