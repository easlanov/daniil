"""
https://education.yandex.ru/ege/task/a8c96097-e410-484b-8fe6-9d1034a9e228

Значение арифметического выражения 7**170+7*100-x, где x – целое положительное число, не превышающее 2030, записали в
7-ричной системе счисления. Определите наибольшее значение x, при котором в 7-ричной записи числа, являющегося значением
данного арифметического выражения, содержится ровно 71 нуль. В ответе запишите число в десятичной системе счисления.
"""

d = "0123456"
r = []
for x in range(1, 2031):
    n = 7**170 + 7**100 - x

    k = ''
    while n > 0:
        k = d[n % 7] + k
        n //= 7

    if str(k).count('0') == 71:
        r.append(x)

print(max(r))
