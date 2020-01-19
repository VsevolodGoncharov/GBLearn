"""
Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество вводимых чисел и
цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&page-id=nW3croJj0OnDWIHHeWKa&title=AlgLesson02.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1-TpvLdCvoEcJjveuXeCKNDvJcY_twFr8%26export%3Ddownload
"""


def count(x, y):
    if not x:
        return 0
    if x % 10 == y:
        return count(x // 10, y) + 1
    else:
        return count(x // 10, y)


L = int(input("Введи длину последовательности\n"))
y = int(input("Введи подсчитываемую цифру\n"))
answer = 0

while L:
    x = int(input("Введи число\n"))
    answer += count(x, y)
    L -= 1

print("Во введенной последовательности чисел цифра {} встречается {} раз".format(y, answer))
