text = input("Enter a sentence: ").split()
n = int(input("Enter n: "))

for i in range(len(text) - n + 1):
    print(text[i:i+n])
