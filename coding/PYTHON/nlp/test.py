words = ["happy", "kind", "teach", "help", "use"]
prefixes = ["un", "re"]
suffixes = ["er", "ful", "ness"]
print("Prefix and Suffix Word Generation:\n")
for word in words:
    for pre in prefixes:
        print(f"{pre + word}")
    for suf in suffixes:
        print(f"{word + suf}")
    print()  