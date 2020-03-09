"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке
[0; 50). Выведите на экран исходный и отсортированный массивы.
"""

import random

def mergesort(mas):
    answer = []
    if len(mas) < 2:
        return mas
    mid = len(mas) // 2
    left = mergesort(mas[:mid])
    right = mergesort(mas[mid:])
    while (len(left) > 0) or (len(right) > 0):
        if len(left) > 0 and len(right) > 0:
            if left[0] > right[0]:
                answer.append(right[0])
                right.pop(0)
            else:
                answer.append(left[0])
                left.pop(0)
        elif len(right) > 0:
            for i in right:
                answer.append(i)
                right.pop(0)
        else:
            for i in left:
                answer.append(i)
                left.pop(0)
    return answer


MAS_LEN = 100
mas = [random.randint(0, 49) for _ in range(MAS_LEN)]
print("Исходный массив: {}".format(mas))
print("Отсортированый : {}".format(mergesort(mas)))
