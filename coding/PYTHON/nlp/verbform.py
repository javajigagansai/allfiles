words = ["play", "playing", "played", "run", "running", "ran"]
base, past, cont = [], [], []
for w in words:
    if w.endswith("ing"): cont.append(w)
    elif w.endswith("ed") or w in ["ran"]: past.append(w)
    else: base.append(w)
print("Base:", base)
print("Past:", past)
print("Continuous:", cont)