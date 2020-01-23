"""
Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5,
(индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.
"""

import random


# Так же вне конкурса добавил кастомный принт, что бы элементы массивов выводились сопоставленными - элемент к индексу
# Кастомный принт перестанет работать, если установить максимальную величину элементов больше 9999
def custom_print(first_mas, second_mas):
    print("\nКастомный вывод:")
    print("Первый массив: [", end="")
    for item in first_mas:
        print("{:>4},".format(item), end="")
    print("]")

    last_item = 0
    first_run = True
    print("Второй массив: [", end="")
    for item in second_mas:
        if first_run:
            string = "{:>" + str((item + 1) * 5 - 1) + "},"
            first_run = False
        else:
            string = "{:>" + str((item - last_item) * 5 - 1) + "},"
        print(string.format(item), end="")
        last_item = item
    print("]")


# Генерация массивов
MAS_LENGTH = 100
MIN_VALUE = 0
MAX_VALUE = 999
first_mas = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(MAS_LENGTH)]
second_mas = []

for idx, item in enumerate(first_mas):
    if item % 2 == 0:
        second_mas.append(idx)

print("Первый массив: {}\nВторой массив: {}".format(first_mas, second_mas))
custom_print(first_mas, second_mas)
