text = "playing played player playful enjoyment enjoyable joy joyful"
words = text.split()
prefixes = [w[:3] for w in words]  
suffixes = [w[-3:] for w in words]  
print("Given sentence: ",text)
print("Prefix counts:", {p: prefixes.count(p) for p in set(prefixes)})
print("Suffix counts:", {s: suffixes.count(s) for s in set(suffixes)})
