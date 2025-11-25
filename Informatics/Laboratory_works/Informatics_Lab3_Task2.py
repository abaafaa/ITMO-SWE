# Author = Erkaev Azizjon Anvarovich
# Group = P3113
# Date = 10.11.2025

import re
import sys

# text = "Классное слово – обороноспособность, которое должно идти после слов: трава и молоко"
# text = "Привет друзья! Это тест на отсутствие."
# text = "Привет друзья! Полное отсутствие."
# text = "И и Быть быть молоко окко"
text = "Окно, трава; молоко быть после!"

G = []
for vp in 'аеёиоуыэюя':
    pattern = r'\b[бвгджзйклмнпрстфхцчшщъь' + vp + r']*[' + vp + r'][бвгджзйклмнпрстфхцчшщъь' + vp + r']*\b'
    G.extend(re.findall(pattern, text, re.IGNORECASE))

ls = sorted(G, key=lambda x: (len(x), x))

print(*ls, sep="\n")
