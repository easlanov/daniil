"""
https://education.yandex.ru/ege/task/a696a437-e1ef-4840-9c18-14868467d8a1

Все четырёхбуквенные слова, составленные из букв А, Б записаны в алфавитном порядке и пронумерованы.

АААА
АААБ
ААБА
ААББ
Под каким номером будет слово ББББ.
"""
from itertools import *

for i, v in enumerate(sorted(product("АБ", repeat=4))):
    v_str = "".join(v)
    if v_str == "ББББ":
        print(i + 1)
