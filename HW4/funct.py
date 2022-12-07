import sympy
from random import randint as rnd


def create_polinom(k: int, simple: bool = True) -> str:
    """"Функция генерирует полином со случайным коэффициентом степени к
    simple = false вернет полином без сокращения нулевых коэффициентов"""
    polinom = ''
    for i in range(k, -1, -1):
        polinom += f'{rnd(0,2)}*x**{i}+'
        if i == 0:
            polinom += f'{rnd(0,100)}*x**{i}'
        if simple:
            return str(sympy.simplify(polinom))
        else:
            return str(polinom)

def create_polinom_file(polinom: str, filename: str = 'new'):
    """"Записывает в полином файл, дополнительно можно указать имя файла
    и путь к этому файлу"""
    with open(f'hw4/{filename}.txt', 'w') as f:
        f.write(polinom)
