"""
Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами
на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
Примечания:
● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
"""


import random


def bublesort(mas):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(1, len(mas)):
            if mas[i] < mas[i - 1]:
                mas[i - 1], mas[i] = mas[i], mas[i - 1]
                is_sorted = False
    return mas


MAS_LEN = 100
mas = [random.randint(-100, 99) for _ in range(MAS_LEN)]
print("Исходный массив: {}".format(mas))
print("Отсортированый : {}".format(bublesort(mas)))
