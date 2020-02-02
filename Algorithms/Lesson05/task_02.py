import collections

class Hex_dict(dict):
    def __init__(self):
        super().__init__()
        self.update({1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 0: 0,
                     '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 0,
                     'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15,
                     'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15})
        self.reverse = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 0: '0',
                        10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F',
                        '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9',
                        '0': '0', '10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F'}


def hex_to_dec(hex: list):
    HEX = 16
    hex_dict = Hex_dict()
    answer = 0
    for idx, i in enumerate(hex[::-1]):
        answer += hex_dict[i] * (HEX ** idx)
    return answer


def dec_to_hex(dec: int):
    HEX = 16
    hex_dict = Hex_dict()
    answer = []
    while dec != 0:
        answer.append(hex_dict.reverse[dec % HEX])
        dec //= HEX
    return answer[::-1]


numbers = collections.defaultdict(list)

for i in input("Введи первое число: "):
    numbers['first'].append(i)
for i in input("Введи второе число: "):
    numbers['second'].append(i)
numbers['sum'] = dec_to_hex(hex_to_dec(numbers['first']) + hex_to_dec(numbers['second']))
numbers['mult'] = dec_to_hex(hex_to_dec(numbers['first']) * hex_to_dec(numbers['second']))

print("{first} + {second} = {sum}\n{first} * {second} = {mult}".format(first=numbers['first'],
                                                                       second=numbers['second'],
                                                                       sum=numbers['sum'],
                                                                       mult=numbers['mult']))
