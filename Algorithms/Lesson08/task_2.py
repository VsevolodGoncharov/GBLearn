"""
Закодируйте любую строку по алгоритму Хаффмана
"""

import collections


class Point:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return 'point({},{})'.format(self.left, self.right)


def encode(text):
    chs = collections.Counter(text)
    alphabet = get_alphabet(to_tree(chs))
    encode_text = ''
    for ch in text:
        encode_text += alphabet[ch]
    return encode_text

def to_tree(chs):
    if len(chs) == 1:
        return chs.popitem()[0]

    new_chs = chs.copy()
    cost_lower = chs.most_common()[:-3:-1]
    for i in range(len(cost_lower)):
        new_chs.pop(cost_lower[i][0])
    new_chs[Point(cost_lower[0][0], cost_lower[1][0])] += cost_lower[0][1] + cost_lower[1][1]

    return to_tree(new_chs)


def get_alphabet(point, alphabet=None, stack=None):
    if not alphabet:
        alphabet = {}
    if not stack:
        stack = ''

    if isinstance(point.left, str):
        alphabet[point.left] = stack + '0'
    elif isinstance(point.left, Point):
        alphabet.update(get_alphabet(point.left, alphabet, stack + '0'))

    if isinstance(point.right, str):
        alphabet[point.right] = stack + '1'
    elif isinstance(point.right, Point):
        alphabet.update(get_alphabet(point.right, alphabet, stack + '1'))

    return alphabet


print(encode(input("Введи текст для кодирования: ")))
