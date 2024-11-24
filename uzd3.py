import re
from collections import Counter
from nltk.tokenize import TreebankWordTokenizer

tokenizer = TreebankWordTokenizer()

def tekstins(teksts):
    teksts = teksts.lower()
    teksts = re.sub(r'[^\w\s]', '', teksts)
    tokens = tokenizer.tokenize(teksts)
    return tokens

def saskaitam(teksts1, teksts2):
    vardi1 = tekstins(teksts1)
    vardi2 = tekstins(teksts2)
    skaits1 = Counter(vardi1)
    skaits2 = Counter(vardi2)

    vienaadie_vaardi = skaits1 & skaits2
    return vienaadie_vaardi

def liidziiba(teksts1, teksts2):
    vienaadie_vaardi = saskaitam(teksts1, teksts2)
    total_vardi = len(tekstins(teksts1)) + len(tekstins(teksts2))
    kopējie_vienaadie_vaardi = sum(vienaadie_vaardi.values())

    līdzība = (kopējie_vienaadie_vaardi * 2) / total_vardi * 100
    return līdzība

teksts1 = str(input("Ievadiet pirmo tekstu: "))
teksts2 = str(input("Ievadiet otro tekstu: "))
sakritiba = saskaitam(teksts1, teksts2)
līdzība = liidziiba(teksts1, teksts2)

print("Vārdu sakritība: ", sakritiba)
print(f"Līdzība procentos: {līdzība}%")