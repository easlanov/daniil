'''
Яндекс Учебник
Артём составляет пятибуквенные слова из букв своего имени. Он ввёл два правила: не повторять буквы в одном слове и не
ставить гласные первыми и последними одновременно.

Сколько таких слов может составить Артём?
'''

from itertools import product

letters = "артём"
glassnie = "аё"

words = list(product(letters, repeat=5))

count = 0
for word in words:
    if len(set(word)) != 5:
        continue
    if word[0] in glassnie and word[4] in glassnie:
        continue
    count += 1

print(count)
