
def swap_case(s):
    result = []
    for ch in s:
        if ch.islower():
            result.append(ch.upper())
        elif ch.isupper():
            result.append(ch.lower())
        else:
            result.append(ch)
    return ''.join(result)


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)