"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

import random

# Генерация массива
MAS_LENGTH = 10
MIN_VALUE = 0
MAX_VALUE = 99
mas = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(MAS_LENGTH)]

print("Оригинальный массив : {}".format(mas))
min_idx = 0
max_idx = 0
for idx, item in enumerate(mas):
    if item < mas[min_idx]:
        min_idx = idx
    if item > mas[max_idx]:
        max_idx = idx

mas[max_idx], mas[min_idx] = mas[min_idx], mas[max_idx]

print("Максимальный элемент: {}\nМинимальный элемент : {}\nИтоговый массив     : {}".format(mas[min_idx],
                                                                                            mas[max_idx],
                                                                                            mas))
