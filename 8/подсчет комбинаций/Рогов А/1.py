"""
https://education.yandex.ru/ege/task/ec685268-8ab8-419d-a89e-b1ca5ff7d8b7

Определите количество пятизначных чисел, записанных в семеричной системе счисления, в записи которых ровно одна цифра 5,
при этом никакая чётная цифра не стоит рядом с цифрой 5.
"""
from itertools import *

# количество чисел удовлетворяющих условие задачи (ответ на задачу)
k = 0

# проходимся по каждому числу, которые создала функция product
for n in product("0123456", repeat=5):
    # убираем все числа начинающиеся на ноль
    if n[0] == '0':
        continue

    # если в числе "n" встречается цифра 5 НЕ один раз, то начинаем цикл сначала
    if n.count('5') != 1:
        continue

    # создаем строку
    n_str = "".join(n)
    # заменяем в строке все четные цифры на двойку
    n_str = n_str.replace("0", "+").replace("2", "+").replace("4", "+").replace("6", "+")

    # если в полученной строке не встречается "+5" и не встречается 5+, то это число нам подходит, увеличиваем счетчик
    if n_str.count("+5") == 0 and n_str.count("5+") == 0:
        k += 1

print(k)
