"""
Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции вводятся
пользователем. После выполнения вычисления программа не завершается, а запрашивает новые данные для вычислений.
Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. Если пользователь вводит
неверный знак (не '0', '+', '-', '*', '/'), программа должна сообщать об ошибке и снова запрашивать знак операции.
Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.
https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&page-id=nW3croJj0OnDWIHHeWKa&title=AlgLesson02.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1-TpvLdCvoEcJjveuXeCKNDvJcY_twFr8%26export%3Ddownload
"""

input_error = False

while True:
    if not input_error:
        a = int(input("Введи первое число\n"))
        b = int(input("Введи второе число\n"))
    ch = input("Введи действие (+,-,*,/) или 0 для выхода\n")

    input_error = False

    if ch == '+':
        print("{} + {} = {}".format(a, b, a + b))
    elif ch == '-':
        print("{} - {} = {}".format(a, b, a - b))
    elif ch == '*':
        print("{} * {} = {}".format(a, b, a * b))
    elif ch == '/':
        print("{} / {} = {}".format(a, b, a / b))
    elif ch == '0':
        break
    else:
        print("Ошибка ввода\n")
        input_error = True
