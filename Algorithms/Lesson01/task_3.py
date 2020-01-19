"""
По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки

Блок схема
https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Untitled%20Diagram.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1mxnKBS6bcWi1IfPPKdaH650nDKq0NAaz%26export%3Ddownload
"""

x1 = int(input("Введи x1\n"))
x2 = int(input("Введи x2\n"))
y1 = int(input("Введи y1\n"))
y2 = int(input("Введи y2\n"))

a = x2 - x1
k = (y2 - y1) / a
b = (x2 * y1 - x1 * y1) / a

if b > 0:
    print("Уравнение прямой для введенных точек принимает вид y = {}x - {}".format(k, b))
else:
    if b == 0:
        print("Уравнение прямой для введенных точек принимает вид y = {}x".format(k))
    else:
        print("Уравнение прямой для введенных точек принимает вид y = {}x + {}".format(k, -b))
