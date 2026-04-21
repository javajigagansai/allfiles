facts = ["All humans are mortal", "Socrates is a human"]
rule = "If all humans are mortal and Socrates is a human, then Socrates is mortal"

print("Facts:")
for f in facts:
    print("-", f)

print("\nApplying rule of deduction...")
print("→ Therefore, Socrates is mortal.")