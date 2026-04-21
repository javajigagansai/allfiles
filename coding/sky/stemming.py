from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

stemmer = PorterStemmer()
words = word_tokenize("The boys are playing in the playground")
for w in words:
    print(w, "→", stemmer.stem(w))