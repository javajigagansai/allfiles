import random
import os

FILENAME = __file__

def roll():
    return random.randint(1, 6)

def self_mutate(extreme_luck: bool):
    with open(FILENAME, 'r') as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        if "random.randint(1, 6)" in line:
            if extreme_luck:
                lines[i] = "    return random.randint(2, 5)  # Balanced by code\n"
            else:
                lines[i] = "    return random.randint(1, 6)  # Reset to normal\n"
            break

    with open(FILENAME, 'w') as f:
        f.writelines(lines)

history = [roll() for _ in range(10)]
print("🎲 Rolls:", history)

# Detect if player is abnormally lucky/unlucky
if history.count(6) >= 5:
    print("🧿 Too lucky! The dice senses imbalance...")
    self_mutate(True)
elif history.count(1) >= 5:
    print("😞 Too unlucky. Resetting fate...")
    self_mutate(False)
else:
    print("🌀 Balance maintained.")
