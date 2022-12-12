# Создайте программу для игры с конфетами человек против человека.
# *' Условие задачи: На столе лежит 117 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.

count_of_candy = int(input('Введите количество конфет для игры: '))
gamer_1, gamer_2 = input('Введите имя 1 игрока: '), input(
    'Введите имя 2 игрока: ')
print(f'Вы можете вводить колисечтво конфет от 1 до 28')
current_gamer = gamer_1
while count_of_candy > 0:
    print('Количество оставшихся конфет: {}'.format(count_of_candy))
    while True:
        number_to_delete = int(
            input('ход игрока {} (1 - 28): '.format(current_gamer)))
        if number_to_delete >= 1 and number_to_delete <= 28:
            break
    count_of_candy -= number_to_delete
    current_gamer = gamer_2 if current_gamer == gamer_1 else gamer_1

print('Победил {}'.format(current_gamer))
