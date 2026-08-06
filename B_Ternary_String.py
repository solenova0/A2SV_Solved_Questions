t = int(input())
for _ in range(t):
    s = input()

    # count = [0] * 4
    # l = 0
    # ans = 10**9

    # for r in range(len(s)):
    #     count[int(s[r])] += 1

    #     while count[1] and count[2] and count[3]:
    #         ans = min(ans, r - l + 1)
    #         count[int(s[l])] -= 1
    #         l += 1

    # print(0 if ans == 10**9 else ans)

    from collections import defaultdict

    count = defaultdict(int)
    left = 0
    ans = float('inf')

    for right in range(len(s)):
        count[s[right]] += 1

        while count['1'] > 0 and count['2'] > 0 and count['3'] > 0:
            ans = min(ans, right - left + 1)

            count[s[left]] -= 1
            left += 1

    if ans == float('inf'):
        print(0)
    else:
        print(ans)