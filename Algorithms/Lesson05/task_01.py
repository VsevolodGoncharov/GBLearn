import collections

organization = collections.namedtuple('organization', 'name qr_money year_money')
money = collections.namedtuple('money', 'qr1 qr2 qr3 qr4')
N = int(input("Сколько будет организаций?\n"))

mas = []
sum_money = 0
for i in range(N):
    mas.append(organization(name=input("Введи наименование {} организации: ".format(i + 1)),
                            qr_money=money(int(input("Введи прибыль за 1 квартал для {} организации: ".format(i + 1))),
                                           int(input("Введи прибыль за 2 квартал для {} организации: ".format(i + 1))),
                                           int(input("Введи прибыль за 3 квартал для {} организации: ".format(i + 1))),
                                           int(input("Введи прибыль за 4 квартал для {} организации: ".format(i + 1)))),
                            year_money=0))
    mas[i] = mas[i]._replace(year_money=sum(mas[i].qr_money))
    sum_money += mas[i].year_money

average_money = sum_money / len(mas)
print("Организации с прибылью выше среднего:")
for item in mas:
    if item.year_money > average_money:
        print("{} - {}".format(item.name, item.year_money))
print("Организации с прибылью ниже среднего:")
for item in mas:
    if item.year_money < average_money:
        print("{} - {}".format(item.name, item.year_money))
