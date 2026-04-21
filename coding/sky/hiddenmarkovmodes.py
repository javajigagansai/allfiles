import nltk
from nltk.corpus import treebank
from nltk.tag import hmm

# Download the Treebank corpus (for training data)
nltk.download('treebank')

# Load tagged sentences
data = treebank.tagged_sents()

# Split into training and testing data
train_data = data[:3000]
test_data = data[3000:]

# Train an HMM POS tagger
trainer = hmm.HiddenMarkovModelTrainer()
hmm_tagger = trainer.train_supervised(train_data)

# Test the tagger on a sentence
sentence = ["The", "quick", "brown", "fox", "jumps"]
tags = hmm_tagger.tag(sentence)

# Print the results
print("HMM POS Tagging:")
for word, tag in tags:
    print(f"{word:10} --> {tag}")
