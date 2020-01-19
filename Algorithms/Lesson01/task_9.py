"""
Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого)

Блок схема
https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&page-id=MvXO6jT34W_8VfwduDVn&title=Untitled%20Diagram.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1mxnKBS6bcWi1IfPPKdaH650nDKq0NAaz%26export%3Ddownload
"""

a = int(input("Введи число a\n"))
b = int(input("Введи число b\n"))
c = int(input("Введи число c\n"))

if a > b:
    if a > c:
        if c > b:
            print("Среднее число c")
        else:
            print("Среднее число b")
    else:
        print("Среднее число a")
else:
    if b > c:
        if c > a:
            print("Среднее число c")
        else:
            print("Среднее число a")
    else:
        print("Среднее число b")
