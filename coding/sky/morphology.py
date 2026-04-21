import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
nltk.download('wordnet')
nltk.download('omw-1.4')

# Sample words
words = ["running", "flies", "cats", "better", "studies"]

# Initialize stemmer and lemmatizer
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

print("Word\tStem\tLemma")
for word in words:
    print(f"{word}\t{stemmer.stem(word)}\t{lemmatizer.lemmatize(word)}")
