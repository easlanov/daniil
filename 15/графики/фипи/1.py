"""
https://education.yandex.ru/ege/task/de253bda-d45a-4a92-a139-ba96506c8f57

Для какого наименьшего целого неотрицательного числа A выражение
(x + 2y < A) || (y > x) || (x > 60)
тождественно истинно, т.е. принимает значение 1 при любых целых неотрицательных x и y.
"""

for A in range(0, 1000):
    A_is_ok = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            r = (x + 2 * y < A) or (y > x) or (x > 60)
            if not r:
                A_is_ok = False
                break
        if not A_is_ok:
            break
    if A_is_ok:
        print(A)
        break
