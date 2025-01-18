"""
https://education.yandex.ru/ege/task/2d4c8b35-1807-4960-8f25-dfae6342c9a7

Семен составляет слова путем перестановки букв в слове КОБУРА. Сколько слов может составить Семён, если гласные и
согласные буквы должны чередоваться? Под словом понимается любая буквенная последовательность, не обязательно
осмысленная.
"""
from itertools import *

k = 0
g = "ОУА"
s = "КБР"

for n in permutations("КОБУРА"):
    d1 = [
        n[0] in g,
        n[1] in s,
        n[2] in g,
        n[3] in s,
        n[4] in g,
        n[5] in s,
    ]
    d2 = [
        n[0] in s,
        n[1] in g,
        n[2] in s,
        n[3] in g,
        n[4] in s,
        n[5] in g,
    ]
    if all(d1) or all(d2):
        k += 1

print(k)
