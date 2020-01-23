"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""

# Генерация массивов
dividend_min = 2
dividend_max = 99
dividers = [i for i in range(2, 10)]

for divider in dividers:
    count = 0
    scorer = divider

    # На случай, если диапазон изменится и нижний предел будет выше, чем нижний предел диапазона делителей.
    while dividend_min > scorer:
        scorer += divider

    # Счетчик делимых для текущего делителя
    while scorer <= dividend_max:
        count += 1
        scorer += divider

    print("В обозначенном диапазоне {} чисел кратны {}".format(count, divider))
