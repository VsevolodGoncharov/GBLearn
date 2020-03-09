"""
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
"""

import random

# Генерация массива
MAS_LENGTH = 100
MIN_VALUE = -99
MAX_VALUE = 99
mas = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(MAS_LENGTH)]

max_item = float('-inf')
max_idx = None
for idx, item in enumerate(mas):
    if max_item < item < 0:
        max_item = item
        max_idx = idx

print("Массив: {}".format(mas))
if max_idx:
    print("Максимальный отрицательный элемент: {} с индексом {}".format(max_item, max_idx))
else:
    print("В нем нет отрицательных элементов")