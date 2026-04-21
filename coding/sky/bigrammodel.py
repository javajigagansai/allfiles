text = input("Enter a sentence: ")

words = text.split()
bigrams = []

for i in range(len(words) - 1):
    pair = (words[i], words[i + 1])
    bigrams.append(pair)

print("Bigrams:")
for b in bigrams:
    print(b)
