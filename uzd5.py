import re
from nltk.tokenize import TreebankWordTokenizer

tokenizer = TreebankWordTokenizer()

teksts = str(input("Ievadiet tekstu: "))

def nonemt_emoji(string):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  
                               u"\U0001F300-\U0001F5FF"  
                               u"\U0001F680-\U0001F6FF"  
                               u"\U0001F1E0-\U0001F1FF"  
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r' ', string)

def remove_unwanted(teksts):
    teksts = teksts.lower()
    teksts = re.sub(r'http\S+|[@!]', '', teksts)
    teksts = nonemt_emoji(teksts) 
    return teksts

teksts_cleaned = remove_unwanted(teksts)
print(teksts_cleaned)
