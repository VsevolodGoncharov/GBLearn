"""
Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, в нем 3 четные
цифры (4, 6 и 0) и 2 нечетные (3 и 5).
https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&page-id=nW3croJj0OnDWIHHeWKa&title=AlgLesson02.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1-TpvLdCvoEcJjveuXeCKNDvJcY_twFr8%26export%3Ddownload
"""


def count(x, y):
    if not x:
        return 0
    if x % 10 % 2 == y:
        return count(x // 10, y) + 1
    else:
        return count(x // 10, y)


x = int(input("Введи число\n"))
even = count(x, 0)
odd = count(x, 1)
print("В числе {} {} четных цифр и {} нечетных".format(x, even, odd))
