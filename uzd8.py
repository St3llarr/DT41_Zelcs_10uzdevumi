import spacy
from deep_translator import GoogleTranslator

nlp = spacy.load("en_core_web_sm")

ievade = input("Ievadiet tekstu: ")
content = GoogleTranslator(source='lv', target='en').translate(ievade)

doc = nlp(content)

print("Personvārdi un organizācijas:")
for ent in doc.ents:
    if ent.label_ in ["PERSON", "ORG"]:
        print(f"{ent.text} ({ent.label_})")
