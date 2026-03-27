from itertools import product
s1 = input().strip()
s2 = input().strip()

target = s1.count('+') - s1.count('-')

q_idx = [i for i, c in enumerate(s2) if c == '?']
k = len(q_idx)

good = 0

for choice in product(['+', '-'], repeat=k):
    temp = list(s2)
    for i, val in zip(q_idx, choice):
        temp[i] = val

    pos = temp.count('+') - temp.count('-')
    if pos == target:
        good += 1

total = 2 ** k
print(f"{good / total:.12f}")