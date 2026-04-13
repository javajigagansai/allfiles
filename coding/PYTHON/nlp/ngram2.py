from collections import Counter
text = "I play football I play cricket I love games".split()
uni = Counter(text)
bi = Counter(zip(text[:-1], text[1:]))
tri = Counter(zip(text[:-2], text[1:-1], text[2:]))
print("Unigrams (1-word counts):", uni)
print("Bigrams (2-word counts):", bi)
print("Trigrams (3-word counts):", tri)

