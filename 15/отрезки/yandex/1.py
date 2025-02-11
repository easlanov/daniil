"""
https://education.yandex.ru/ege/task/33086ce1-73ee-4621-a158-c9344f666df8

На числовой прямой дан отрезок: B=[5;22]
Укажите наибольшую длину такого отрезка А, для которого логическое выражение

(x ∈ B) ∧ ¬ (x ∈ A)
ложно (т. е. принимает значение 0) при любом значении переменной x.
"""

B = range(5, 23)
A = []

for x in range(1, 150):
    r = (x in B) and (not(x in A))
    if r:
        A.append(r)
print(len(A) - 1)
