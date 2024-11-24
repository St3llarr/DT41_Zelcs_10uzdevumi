import torch
from transformers import AutoTokenizer, AutoModel
import numpy as np

tokenizer = AutoTokenizer.from_pretrained('bert-base-multilingual-cased')
model = AutoModel.from_pretrained('bert-base-multilingual-cased')

def get_word_vectors(words):
    inputs = tokenizer(words, return_tensors='pt', padding=True, truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
    embeddings = outputs.last_hidden_state
    word_vectors = {word: embeddings[0, i, :].numpy() for i, word in enumerate(words)}
    return word_vectors

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def find_most_similar_pair(word_vectors):
    similarities = {}
    words_list = list(word_vectors.keys())
    for i, word1 in enumerate(words_list):
        for j, word2 in enumerate(words_list):
            if i < j:
                sim = cosine_similarity(word_vectors[word1], word_vectors[word2])
                similarities[f"{word1}-{word2}"] = sim
                print(f"Similarity between '{word1}' and '{word2}': {sim:.4f}")
    
    most_similar_pair = max(similarities, key=similarities.get)
    highest_similarity = similarities[most_similar_pair]
    return most_similar_pair, highest_similarity

words = input("Ievadiet vārdus, atdalot tos ar atstarpi (vai atstājiet tukšu priekš piemēra): ").strip().split()
if not words:
    words = ["māja", "dzīvoklis", "jūra"]
    print(f"Izmantojam piemēra vārdus: {words}")

word_vectors = get_word_vectors(words)
most_similar_pair, highest_similarity = find_most_similar_pair(word_vectors)

print(f"\nThe most semantically similar pair is '{most_similar_pair}' with a similarity of {highest_similarity:.4f}.")