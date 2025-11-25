# Author = Erkaev Azizjon Anvarovich
# Group = P3113
# Date = 10.11.2025

# print(503806 % 3) = 1

import re
from collections import defaultdict
from functools import reduce

suff = ['ив', 'ев', 'ов', "оват", "еват", "ев", "овит", "евит", "чив", "лив", "ат", "чат", "ист", "к", "ч", "оньк",
          "чн", "ск", "чат", "чев", "лев", "ан", "ян", "инн", "ынн", "анн", "янн", "инн", "ынн", "онн", "енн", ""]
ends = ["ой", "ое", "ый", "ий", "ее", "ая", "яя", "ые", "ие", "ого", "его", "ей", "ых", "их", "ому", "ему", "ым", "им",
        "ую", "юю", "ыми", "ими", "ом", "ем"]
suffends = [x + y for x in suff for y in ends]

P = r"\b((\w+)(?:" + "|".join(re.escape(e) for e in suffends) + r"))\b"

def f(n, text: str):
    matches = re.findall(P, text, re.IGNORECASE)
    adjectives = [(mas[1], mas[0]) for mas in matches if mas[1]]

    d = defaultdict(list)
    for begin, full_word in adjectives:
        d[begin.lower()].append(full_word.lower())

    adjectives = [pair for pair in adjectives if len(d[pair[0].lower()]) >= 2]

    if not adjectives or n >= len(adjectives) or n < 0:
        print("Вы ввели неверное число!")
        return

    t1 = adjectives[n][0].lower()
    T = adjectives[n][1]

    w = [pair for i, pair in enumerate(adjectives) if i != n and pair[0].lower() == t1]

    text = reduce(lambda t, pair: re.sub(re.escape(pair[1]), T, t, count=1, flags=re.IGNORECASE), w, text)

    print("Измененный текст:")
    print(text)


# Пример использования с новыми тестами (первый оставлен, остальные новые)
tests = [("""
Футбольный  клуб  «Реал  Мадрид»  является  15-кратным  обладателем  главного футбольного европейского трофея – Лиги Чемпионов. Данный турнир организован Союзом европейских футбольных ассоциаций (УЕФА). Идея о континентальном футбольном турнире пришла к журналисту Габриэлю Ано в 1955 году.
""", 2),
         ("""
большой, большого, большая, большая
""", 1),
         ("""
Красный, красного, красная, красной
""", 1),
         ("""
Сухой воздух сухого климата сухим ветром
""", 0),
         ("""
Одинокий путник одинокого пути
""", 3)
         ]
for a in tests:
    f(a[1] - 1, a[0])