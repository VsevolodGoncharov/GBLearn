"""
Проанализировать скорость и сложность одного любого алгоритма
из разработанных в рамках домашнего задания первых трех уроков.
Примечание. Идеальным решением будет:
● выбрать хорошую задачу, которую имеет смысл оценивать,
● написать 3 варианта кода (один у вас уже есть),
● проанализировать 3 варианта и выбрать оптимальный,
● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
● написать общий вывод: какой из трёх вариантов лучше и почему.
"""
"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

import random
import timeit
import cProfile

# Обход массива с поиском максимального и минимального элемента с последующей заменой
def calc1(mas):
    min_idx = 0
    max_idx = 0
    for idx, item in enumerate(mas):
        if item < mas[min_idx]:
            min_idx = idx
        if item > mas[max_idx]:
            max_idx = idx
    mas[max_idx], mas[min_idx] = mas[min_idx], mas[max_idx]

# Отдельный обход для поиска максимального и отдельный для минимального элемента с последующей заменой
def calc2(mas):
    min_idx = 0
    for idx, item in enumerate(mas):
        if item < mas[min_idx]:
            min_idx = idx
    max_idx = 0
    for idx, item in enumerate(mas):
        if item > mas[max_idx]:
            max_idx = idx
    mas[max_idx], mas[min_idx] = mas[min_idx], mas[max_idx]

# В одну строку! Как тебе такое, Илон Маск?
def calc3(mas):
    mas[mas.index(min(mas))], mas[mas.index(max(mas))] = mas[mas.index(max(mas))], mas[mas.index(min(mas))]


# Генерация массива
SIZE = 100000
MIN_VALUE = 0
MAX_VALUE = 99
mas = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(SIZE)]


# Замеры производительности
print(timeit.timeit('calc1(mas)', number=100, globals=globals()))
# calc1(100) 0.0009737
# calc1(100000) 1.0215922
# calc1(10000000) 102.740969
print(timeit.timeit('calc2(mas)', number=100, globals=globals()))
# calc1(100) 0.0012347
# calc1(100000) 1.407363
# calc1(10000000) 137.2594995
print(timeit.timeit('calc3(mas)', number=100, globals=globals()))
# calc1(100) 0.0006551
# calc1(100000) 0.4055386
# calc1(10000000) 40.6953707


cProfile.run('calc1(mas)')
# calc1(100000)
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.011    0.011 <string>:1(<module>)
#         1    0.011    0.011    0.011    0.011 task_1.py:20(calc1)
#         1    0.000    0.000    0.011    0.011 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('calc2(mas)')
# calc2(100000)
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.014    0.014 <string>:1(<module>)
#         1    0.014    0.014    0.014    0.014 task_1.py:31(calc2)
#         1    0.000    0.000    0.014    0.014 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('calc3(mas)')
# calc3(100000)
# calls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.004    0.004 <string>:1(<module>)
#         1    0.000    0.000    0.004    0.004 task_1.py:43(calc3)
#         1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
#         2    0.002    0.001    0.002    0.001 {built-in method builtins.max}
#         2    0.002    0.001    0.002    0.001 {built-in method builtins.min}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         4    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}

"""
Внезапно самым быстрой оказалась однострочная реализация. Предположу это связано с тем, что встроенные функции
min, max и index скомпилированы на C и выполняются гораздо быстрее, чем аналог на Python.
Асимптотика всех алгоритмов линейная
"""
