import re
from collections import Counter
from nltk.tokenize import TreebankWordTokenizer

tokenizer = TreebankWordTokenizer()

teksts = str(input("Ievadiet tekstu: "))
teksts = teksts.lower()
teksts = re.sub(r'[^\w\s]','',teksts)
vārdi = tokenizer.tokenize(teksts)
vārdu_skaits = Counter(vārdi)
print("Vārdu biežums: ", vārdu_skaits)
