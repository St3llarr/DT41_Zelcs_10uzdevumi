from transformers import pipeline, set_seed
from deep_translator import GoogleTranslator

lat_teksts = input("Ievadie sākuma frāzi: ")
eng_teksts = GoogleTranslator(source='lv', target='en').translate(lat_teksts)
generator = pipeline('text-generation', model='gpt2')
set_seed(42)
generated_text = generator(eng_teksts,max_length=100,num_return_sequences=1,temperature=0.7,truncation=True,pad_token_id=generator.tokenizer.eos_token_id)[0]["generated_text"]
finala_teksts = GoogleTranslator(source='en', target='lv').translate(generated_text)
print(finala_teksts)