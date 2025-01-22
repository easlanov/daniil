"""
https://education.yandex.ru/ege/task/2273f34b-ce38-42dd-a20d-d63c196554a1

Для какого наименьшего целого неотрицательного числа А выражение
(x >= 45) || (A > x)
тождественно истинно, то есть принимает значение 1 при любом целом неотрицательном x?
"""

for A in range(0, 1000):
    A_is_ok = True
    for x in range(0, 1000):
        r = (x >= 45) or (A > x)
        if not r:
            A_is_ok = False
            break
    if A_is_ok:
        print(A)
        break
