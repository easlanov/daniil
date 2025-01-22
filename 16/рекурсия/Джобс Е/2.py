"""
https://education.yandex.ru/ege/task/7addf107-5674-4e91-bdd5-ed8f202934df

Алгоритмы вычисления значения функций  F(n) и G(n) заданы следующими соотношениями:
F(n)=1, если n ≥ 3210;
G(n)=n, если n<10;
F(n)=F(n+3)+7, если n<3210;
G(n)=G(n−3)+5, если n≥10.

Чему равно значение выражения F(15)−G(3000)?
"""

import sys

sys.setrecursionlimit(1000000)

def F(n):
    if n >= 3210:
        return 1
    if n < 3210:
        return F(n + 3) + 7

def G(n):
    if n < 10:
        return n
    if n >= 10:
        return G(n - 3) + 5

print(F(15) - G(3000))
