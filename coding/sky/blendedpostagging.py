import nltk
from nltk.corpus import treebank
nltk.download('treebank'); nltk.download('universal_tagset')

# Load data
data = treebank.tagged_sents(tagset='universal')
train, test = data[:3500], data[3500:]

# Build taggers
default = nltk.DefaultTagger('NOUN')
uni = nltk.UnigramTagger(train, backoff=default)
bi = nltk.BigramTagger(train, backoff=uni)

# Blend function (prefer bigram if available)
def blend_tag(sentence):
    u, b = uni.tag(sentence), bi.tag(sentence)
    return [(w, bt or ut) for ((w, bt), (_, ut)) in zip(b, u)]

# Test
sent = ["The", "cat", "sits", "on", "the", "mat"]
print("Blended POS Tags:", blend_tag(sent))
print("Accuracy:", bi.evaluate(test))