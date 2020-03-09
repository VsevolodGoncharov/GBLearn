"""
Получив добро на самостоятельный выбор алгоритма для выполнения задания, я решил выбрать актуальную на данный момент
для себя задачу: задание из ЕГЭ. В рамках ДЗ представлено 3 варианта решения задачи:
1.Алгоритм корректный с точки зрения функционала, но не оптимальный по условию задачи
2.Моя реализация оптимального алгоритма
3.Реализация алгоритма из решебника
Фактических отличий моей реализации от реализации решебника не так много. Из существенных - использование модуля
collections.
Ниже представлено условие задачи.
"""

"""
На вход программы поступает последовательность из N целых положительных чисел, все числа в последовательности различны. 
Рассматриваются все пары различных элементов последовательности, находящихся на расстоянии не меньше чем 4 
(разница в индексах элементов пары должна быть 4 или более, порядок элементов в паре неважен). 
Необходимо определить количество таких пар, для которых произведение элементов делится на 29.

Описание входных и выходных данных:
В первой строке входных данных задаётся количество чисел N (4 <= N <= 1000). 
В каждой из последующих N строк записано одно целое положительное число, не превышающее 10000.
В качестве результата программа должна вывести одно число: количество пар элементов, 
находящихся в последовательности на расстоянии не меньше чем 4, в которых произведение элементов кратно 29.

Пример входных данных:
N(7) Массив(58 2 3 5 4 1 29)

Пример выходных данных для приведённого выше примера входных данных:
5

Требуется написать эффективную по времени и памяти программу для решения описанной задачи.
Программа считается эффективной по времени, если при увеличении количества исходных чисел N в k раз 
время работы программы увеличивается не более чем в k раз.
Программа считается эффективной по памяти, если память, необходимая для хранения всех переменных программы, 
не превышает 1 килобайта и не увеличивается с ростом N.
"""

import collections
import sys
import timeit


# Вариант 1. Формально верное, но не оптимизированное решение
def work1():
    DIVIDER = 29
    PIT = 4
    counter = 0
    N = int(input("Введи длину массива: "))
    mas = [0] * N
    for i in range(N):
        mas[i] = int(input("Введи элемент массива: "))
    for i in range(N - PIT):
        for j in range(N - i - PIT):
            if mas[i] * mas[j + i + PIT] % DIVIDER == 0:
                counter += 1
    print("Функция work1 затратила {} байт памяти".format(custom_getsizeof(DIVIDER,
                                                                           PIT,
                                                                           counter,
                                                                           N,
                                                                           mas)))
    return counter


# Вариант 2. Мой вариант оптимизированного решения
def work2():
    DIVIDER = 29
    PIT = 4
    counter = 0
    ok_items_counter = 0
    in_pit = collections.deque([False] * PIT, PIT)
    N = int(input("Введи длину массива: "))
    for i in range(N):
        if int(input("Введи элемент массива: ")) % DIVIDER == 0:
            in_pit.append(True)
            if N - i - PIT > 0:
                counter += N - i - PIT
            if i - PIT > 0:
                counter += i - PIT - ok_items_counter
                for last_ok in in_pit:
                    if last_ok:
                        counter += 1
            ok_items_counter += 1
        else:
            in_pit.append(False)
    print("Функция work2 затратила {} байт памяти".format(custom_getsizeof(DIVIDER,
                                                                           PIT,
                                                                           counter,
                                                                           ok_items_counter,
                                                                           in_pit,
                                                                           N)))
    return counter


# Вариант 3. Вариант оптимизированного решения из решебника
def work3():
    DIVIDER = 29
    PIT = 4
    mas = [0] * PIT
    counter = 0
    n = int(input("Введи длину массива: "))
    for i in range(PIT):
        mas[i] = int(input("Введи элемент массива: "))
    n29 = 0
    for i in range(PIT, n):
        k = i % PIT
        if mas[k] % DIVIDER == 0:
            n29 = n29 + 1
        a = int(input("Введи элемент массива: "))
        if a % DIVIDER == 0:
            counter += i - PIT + 1
        else:
            counter += n29
        mas[i % PIT] = a
    print("Функция work3 затратила {} байт памяти".format(custom_getsizeof(DIVIDER,
                                                                           PIT,
                                                                           mas,
                                                                           counter,
                                                                           n,
                                                                           n29,
                                                                           k)))
    return counter


# Функция для проверки используемой памяти. Почти полностью скопипасчена с занятия, только добавлена возможность
# обрабатывать сразу несколько объектов.
def custom_getsizeof(*args):
    answer = 0
    for item in args:
        answer += sys.getsizeof(item)
        print("type={}, size={}".format(type(item), answer))
        if hasattr(item, '__iter__'):
            if not isinstance(item, str):
                if hasattr(item, 'items'):
                    for key, value in item.items():
                        answer += custom_getsizeof(key, value)
                else:
                    for value in item:
                        answer += custom_getsizeof(value)
    return answer


# При одинаковых входных данных (N(7) Массив(58 2 3 5 4 1 29)) функции употребили следующее количество памяти:
work1()  # 420 байт - при увеличении N потребление памяти растет
work2()  # 864 байт - сильно проигрывает по памяти из-за использования deque(736 байт). От N не зависит
work3()  # 368 байт - вариант из решебника самый оптимальный по памяти. От N не зависит


"""
Ниже, в качестве факультатива, представлено исспледование на предмет асимптотики.
Функции подразумевают ввод данных пользователем, что не подходит для замера времени. Поэтому функции были изменены
таким образом, что бы пользовательские данные подавались на вход ввиде аргументов. Данные версии функций именованы 
test_*funcName*. Так же убраны вызовы функции custom_getsizeof.

Неоптимальное решение имеет квадратичную асимптотику. Оптимизированные решения имеют линейную асимптотику.
"""


def test_work1(N, mas):
    DIVIDER = 29
    PIT = 4
    counter = 0
    for i in range(N - PIT):
        for j in range(N - i - PIT):
            if mas[i] * mas[j + i + PIT] % DIVIDER == 0:
                counter += 1
    return counter


def test_work2(N, mas):
    DIVIDER = 29
    PIT = 4
    counter = 0
    ok_items_counter = 0
    in_pit = collections.deque([False] * PIT, PIT)
    for i in range(N):
        if mas[i] % DIVIDER == 0:
            in_pit.append(True)
            if N - i - PIT > 0:
                counter += N - i - PIT
            if i - PIT > 0:
                counter += i - PIT - ok_items_counter
                for last_ok in in_pit:
                    if last_ok:
                        counter += 1
            ok_items_counter += 1
        else:
            in_pit.append(False)
    return counter


def test_work3(N, mas):
    DIVIDER = 29
    PIT = 4
    counter = 0
    new_mas = mas[:4]
    n29 = 0
    for i in range(PIT, N):
        k = i % PIT
        if new_mas[k] % DIVIDER == 0:
            n29 = n29 + 1
        a = mas[i]
        if a % 29 == 0:
            counter += i - PIT + 1
        else:
            counter += n29
        new_mas[i % PIT] = a
    return counter


k = 1  # 10, 1000

print(timeit.timeit('test_work1(7*k, [58, 2, 3, 5, 4, 1, 29]*k)', number=5, globals=globals()))
# k = 1     0.0000169
# k = 10    0.0018741
# k = 1000  24.155232
print(timeit.timeit('test_work2(7*k, [58, 2, 3, 5, 4, 1, 29]*k)', number=5, globals=globals()))
# k = 1     0.0000198
# k = 10    0.0001018
# k = 1000  0.0105923
print(timeit.timeit('test_work3(7*k, [58, 2, 3, 5, 4, 1, 29]*k)', number=5, globals=globals()))
# k = 1     0.0000105
# k = 10    0.0000986
# k = 1000  0.0110799
