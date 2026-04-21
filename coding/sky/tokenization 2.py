import nltk
nltk.download('punkt')
nltk.download('punkt_tab')   # 👈 new requirement in latest NLTK

from nltk.tokenize import word_tokenize, sent_tokenize

text = "NLP is fun. It involves text processing."
print("Word Tokenization:", word_tokenize(text))
print("Sentence Tokenization:", sent_tokenize(text))