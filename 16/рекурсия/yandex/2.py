"""
https://education.yandex.ru/ege/task/d9162146-83b1-438f-a1f2-680d854581e4

"""
import sys

sys.setrecursionlimit(10000)


def F(n):
    if n <= 1:
        return 1
    if n > 1 and n % 2 == 0:
        return n * F(n-1) // 2

    return (n - 1) * F(n - 1) // 2

print(
    (F(2024) - F(2022)) // F(2021)
)
