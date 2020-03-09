"""
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
которые не меньше медианы, в другой — не больше медианы.
Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).
"""

import random

def quickselect(mas, x):
    if len(mas) == 1:
        return mas[0]
    low = []
    high = []
    for i in range(1, len(mas)):
        if mas[i] < mas[0]:
            low.append(mas[i])
        else:
            high.append(mas[i])
    if len(low) == x:
        return mas[0]
    elif len(low) > x:
        return quickselect(low, x)
    else:
        return quickselect(high, x - len(low) - 1)


m = 3
mas = [random.randint(1, 100) for _ in range(2 * m + 1)]
print("Массив: {}\nМедиана: {}".format(mas, quickselect(mas, len(mas) // 2)))
