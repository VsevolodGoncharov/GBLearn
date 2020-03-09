"""
Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.
https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&page-id=nW3croJj0OnDWIHHeWKa&title=AlgLesson02.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1-TpvLdCvoEcJjveuXeCKNDvJcY_twFr8%26export%3Ddownload
"""


def summ(n, x):
    if not n:
        return 0
    return summ(n - 1, x / -2) + x


n = int(input("Введи длину ряда\n"))
answer = summ(n, 1)
print("Сумма ряда их {} элементов равна {}".format(n, answer))
