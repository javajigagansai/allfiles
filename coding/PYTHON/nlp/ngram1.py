from collections import Counter

def smooth_methods(data, pair):
    words = data.split()
    bigrams = [(words[i], words[i+1]) for i in range(len(words)-1)]
    c = Counter(bigrams)
    V, N = set(words), sum(c.values())
    x = c[pair]

    add_one = (x+1)/(N+len(V)**2)
    good_turing = (x+1)/(N+1)
    kneser_ney = max(x-0.75,0)/N
    return add_one, good_turing, kneser_ney

data = "I like NLP I like AI I love coding"
print("Sentence: ",data)
print("\tAdd on,\t\tGood turing,\tkneser ney")
print(smooth_methods(data, ("I","like")))
