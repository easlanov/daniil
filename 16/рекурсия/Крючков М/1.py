"""
https://education.yandex.ru/ege/task/d6acebec-814c-4706-9c36-975c410a4a28

"""
import sys

sys.setrecursionlimit(10000)

def F(n):
    if n <= 10:
        return n * 2
    if n % 2 == 0 and n > 10:
        return F(n - 3) - F(n - 9) * 2
    if n % 2 != 0 and n > 10:
        return F(n - 2) * 2 - F(n - 7)

print(len(F(3063)))
