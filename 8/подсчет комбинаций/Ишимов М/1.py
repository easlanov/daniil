"""
https://education.yandex.ru/ege/task/57def1bb-965c-46f2-ab36-a9c134a4cb7c

Сколько существует тринадцатеричных шестизначных чисел, не содержащих в своей записи более одной цифры 5, в которых
никакие две нечётные цифры не стоят рядом?
"""

from itertools import *

k = 0
for n in product("0123456789ABC", repeat=6):
    if n[0] == '0':
        continue

    if n.count('5') > 1:
        continue

    n_str = "".join(n)
    n_str = n_str.replace("1", "+").replace("3", "+").replace("5", "+").replace("7", "+").replace("9", "+").replace("B", "+")

    if "++" not in n_str:
        k += 1

print(k)
