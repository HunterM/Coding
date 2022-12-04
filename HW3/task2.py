# Напишите программу, которая найдёт
# произведение пар чисел списка.
# Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.

import numpy as np 
lst1 = np.random.randint(0, 10, 5).tolist()
print(lst1)


def proizved(nums: list) -> int:
    newlist = []
    iterations = int(round((len(nums))+1)/2)
    print(iterations)
    for i in range(iterations):
        newlist.append(lst1[i]*lst1[len(lst1)-1-i])
    return newlist


print(proizved(lst1))
