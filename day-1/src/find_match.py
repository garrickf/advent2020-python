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

# Somewhat less naive: avoid duplicates by searching only from current index on
def triple_sum_to_forloop_2():
    for a_idx, a in enumerate(expenses):
        for b_idx, b in enumerate(expenses[a_idx + 1 :]):
            for c in expenses[b_idx + 1 :]:
                if a + b + c == 2020:
                    print(f"Found {a}, {b}, {c}; product: {a * b * c}")

triple_sum_to_forloop_2()

# Even better: a list comprehension
# TODO

# Likely the best: using a map/hashmap