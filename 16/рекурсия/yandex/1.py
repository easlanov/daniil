"""
https://education.yandex.ru/ege/task/e47e5c06-40f3-4803-bca7-dd00e56852aa

Алгоритм вычисления значения функции F(n), где n — целое число, задан следующими соотношениями:
F(n)=1, если n < 2
F(n)=F(n−2)+F(n−1), если n≥2

Чему равно значение выражения F(5)?
"""

def F(n):
    if n < 2:
        return 1
    if n >= 2:
        return F(n-2)+ F(n-1)

print(F(5))
