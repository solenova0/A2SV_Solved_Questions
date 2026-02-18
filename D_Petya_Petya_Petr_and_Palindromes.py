from collections import Counter

def max_distinct_split(s):
    right_counter = Counter(s)  # Tracks characters in the right part
    left_counter = Counter()    # Tracks characters in the left part
    max_distinct_sum = 0

    for char in s:
        left_counter[char] += 1
        right_counter[char] -= 1
        if right_counter[char] == 0:
            del right_counter[char]
        max_distinct_sum = max(max_distinct_sum, len(left_counter) + len(right_counter))
    return max_distinct_sum

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(max_distinct_split(s))
