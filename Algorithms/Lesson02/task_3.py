"""
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено
число 3486, надо вывести 6843.
https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&page-id=nW3croJj0OnDWIHHeWKa&title=AlgLesson02.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1-TpvLdCvoEcJjveuXeCKNDvJcY_twFr8%26export%3Ddownload
"""

x = int(input("Введи число\n"))
origin = x
answer = 0

while x:
    answer *= 10
    answer += x % 10
    x //= 10

print("Искомое число: {}\nОбратное: {}".format(origin, answer))
