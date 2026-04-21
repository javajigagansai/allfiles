text = input("Enter a sentence: ")

words = text.split()

for i in range(len(words) - 2):
    print(words[i], words[i + 1], "→", words[i + 2])
