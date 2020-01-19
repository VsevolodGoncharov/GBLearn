"""
Определить, является ли год, который ввел пользователь, високосным или не високосным

Блок схема
https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Untitled%20Diagram.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1mxnKBS6bcWi1IfPPKdaH650nDKq0NAaz%26export%3Ddownload
"""

x = int(input("Введи год\n"))

if x % 4 == 0:
    if x % 100 == 0:
        if x % 400 == 0:
            print("Год високосный")
        else:
            print("Год невисокосный")
    else:
        print("Год високосный")
else:
    print("Год невисокосный")
