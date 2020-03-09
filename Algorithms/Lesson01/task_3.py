"""
По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки

Блок схема
https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&page-id=MvXO6jT34W_8VfwduDVn&title=Untitled%20Diagram.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1mxnKBS6bcWi1IfPPKdaH650nDKq0NAaz%26export%3Ddownload
"""

x1 = int(input("Введи x1\n"))
x2 = int(input("Введи x2\n"))
y1 = int(input("Введи y1\n"))
y2 = int(input("Введи y2\n"))

if x1 == x2:
    print("x = {}".format(x1))
else:
    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2
    print("y = {}x - {}".format(k, b))
