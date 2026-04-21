text = "this is a simple unigram model this is simple"
words = text.split()
total = len(words)
freq = {}

for w in words:
    freq[w] = freq.get(w, 0) + 1

for w in freq:
    print(w, freq[w] / total)

