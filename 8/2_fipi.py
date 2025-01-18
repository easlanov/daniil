'''
ФИПИ
Все пятибуквенные слова, в составе которых могут быть только буквы Б, А, Т, Ы, Р, записаны в алфавитном порядке и
пронумерованы начиная с 1.

Ниже приведено начало списка.

ААААА
ААААБ
ААААР
ААААТ
ААААЫ
АААБА
…
Под каким номером в списке идёт первое слово, которое не содержит ни одной буквы Ы и не содержит букв А, стоящих рядом?
'''

from itertools import product

letters = "БАТЫР"

words = list(product(letters, repeat=5))
words.sort()

counter = 0
for word in words:
    counter += 1
    word_string = "".join(word)
    if 'Ы' in word_string:
        continue
    if 'АА' in word_string:
        continue
    print(word_string)
    break

print(counter)

