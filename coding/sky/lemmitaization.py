import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
text=["running","walking","dancing","cats","better"]
lemma=WordNetLemmatizer()
for word in text:
    print(word,"->",lemma.lemmatize(word))