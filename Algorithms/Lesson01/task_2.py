"""
Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6. Выполнить над числом 5 побитовый сдвиг
вправо и влево на два знака

Блок схема
https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Untitled%20Diagram.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1mxnKBS6bcWi1IfPPKdaH650nDKq0NAaz%26export%3Ddownload
"""

answer = 5 & 6
print("Результат выполнения {} для чисел 5 и 6 равен {}".format("логического И", answer))

answer = 5 | 6
print("Результат выполнения {} для чисел 5 и 6 равен {}".format("логического ИЛИ", answer))

answer = 5 ^ 6
print("Результат выполнения {} для чисел 5 и 6 равен {}".format("XOR", answer))

answer = 5 >> 2
print("Результат выполнения сдвига вправо для числа 5 равен {}".format(answer))

answer = 5 << 2
print("Результат выполнения сдвига влево для числа 5 равен {}".format(answer))
