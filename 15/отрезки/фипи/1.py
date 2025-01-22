"""
https://education.yandex.ru/ege/task/ad49b4d3-62dc-420f-aa97-519d891a80f5

На числовой прямой даны два отрезка: P = [20;67] и Q = [33;98] Укажите наименьшую возможную длину такого отрезка A,
для которого логическое выражение
(x ∈ P) → (((x ∈ Q) ∧ ¬ (x ∈ A)) → ¬ (x ∈ P))
истинно (т. е. принимает значение 1) при любом значении переменной x.

вот тут есть устное решение https://inf-ege.sdamgia.ru/problem?id=13364
вот тут есть условные обозначения операций в Python на 3 странице
https://shkola44pol.ucoz.ru/inf_ege/2022/ispolzovanie_python_dlja_reshenija_zadanii_kegeh_2.pdf
"""

P = range(20, 68)
Q = range(33, 98)
A = []

for x in range(1, 150):
    r = (x in P) <= (((x in Q) and not(x in A)) <= (not(x in P)))
    if not r:
        A.append(r)

print(A)
print(len(A) - 1)
