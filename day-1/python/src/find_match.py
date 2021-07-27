"""Read input and find two numbers that sum to 2020
"""

with open("../data/input.txt", "r") as f:
    lines = f.readlines()

expenses = [int(l.strip()) for l in lines]

# Naive way: nested for-loop, O(n^2) and O(n^3) for the second part below!
for a in expenses:
    for b in expenses:
        if a + b == 2020:
            print(f"Found {a}, {b}; product: {a * b}")

for a in expenses:
    for b in expenses:
        for c in expenses:
            if a + b + c == 2020:
                print(f"Found {a}, {b}, {c}; product: {a * b * c}")
