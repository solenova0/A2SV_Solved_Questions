T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    s = input()

    offsets = ["RGB", "GBR", "BRG"]
    ans = float('inf')

    for offset in offsets:
        matches = 0

        # Count matches in the first window of size K
        for right in range(K):
            if offset[right % 3] == s[right]:
                matches += 1

        max_matches = matches

        # Sliding window
        for right in range(K, N):
            left = right - K

            if offset[right % 3] == s[right]:
                matches += 1
            if offset[left % 3] == s[left]:
                matches -= 1

            max_matches = max(max_matches, matches)

        ans = min(ans, K - max_matches)

    print(ans)