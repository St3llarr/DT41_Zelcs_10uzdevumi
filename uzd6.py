from transformers import pipeline
from deep_translator import GoogleTranslator

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

teksts = str(input("Ievadiet tekstu: "))
teksts_eng = GoogleTranslator(source='lv', target='en').translate(teksts)
rezumesana = summarizer(teksts_eng, min_length=5, max_length=30)
rezumesana_text = rezumesana[0]['summary_text']
teksts_lv = GoogleTranslator(source='en', target='lv').translate(rezumesana_text)
print(f"Kopsavilkums:{teksts_lv}")