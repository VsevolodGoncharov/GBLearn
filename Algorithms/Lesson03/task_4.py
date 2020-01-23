"""
Определить, какое число в массиве встречается чаще всего.
"""

import random

# Генерация массива
MAS_LENGTH = 100
MIN_VALUE = 0
MAX_VALUE = 49
mas = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(MAS_LENGTH)]

scorer = {}
max_score = 0
max_item = None
for item in mas:
    scorer[item] = scorer.setdefault(item, 0) + 1
    if max_score < scorer[item]:
        max_score = scorer[item]
        max_item = item

print("Массив: {}\nЧаще всего встречается число {}. {} раз".format(mas, max_item, max_score))
