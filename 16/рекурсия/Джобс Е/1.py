"""
https://education.yandex.ru/ege/task/331b792d-6dda-40b9-9e6b-8f1808a73c94

Алгоритм вычисления значения функции F(n) задан следующими соотношениями:
F(n)=1 при n <− 100000;
F(n)=F(n−1)+3⋅F(n−3)+2 при n > 10
F(n)=−F(n−1) для остальных случаев.

Чему равно значение функции F(20)?
"""
import sys

sys.setrecursionlimit(1000000)

def F(n):
    if n < -100000:
        return 1
    if n > 10:
        return F(n -1) + 3 * F(n - 3) + 2

    return -(F(n - 1))

print(F(20))
