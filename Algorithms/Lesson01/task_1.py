"""
Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь

Блок схема
https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Untitled%20Diagram.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1mxnKBS6bcWi1IfPPKdaH650nDKq0NAaz%26export%3Ddownload
"""

x = int(input("Введи целое трехзначное число\n"))

answer = (x // 100) + (x // 10 % 10) + (x % 10)
print("Сумма цифр числа {} равна {}".format(x, answer))

answer = (x // 100) * (x // 10 % 10) * (x % 10)
print("Произведение цифр числа {} равно {}".format(x, answer))
