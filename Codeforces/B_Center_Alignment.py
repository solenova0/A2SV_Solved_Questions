import sys
lines = [line.rstrip('\n') for line in sys.stdin]
max_len = max(len(line) for line in lines)
print('*' * (max_len + 2))
Flag = False

for line in lines:
    diff = max_len - len(line)
    left = diff // 2
    right = diff // 2

    if diff % 2 == 1:
        if not Flag:
            right += 1
        else:
            left += 1
        Flag = not Flag

    print('*' + ' ' * left + line + ' ' * right + '*')
print('*' * (max_len + 2))