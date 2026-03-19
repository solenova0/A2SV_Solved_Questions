from collections import defaultdict

n , k = map(int,input().split())
nums = list(map(int,input().split()))
l = 0
maxx = 0
freq = defaultdict(int)
n = len(nums)

for r in range(n):
    freq[nums[r]] += 1
    while len(freq) > k:
        freq[nums[l]] -= 1
        if  freq[nums[l]] == 0:
            del  freq[nums[l]]
        l += 1

    maxx += r - l + 1
    
print(maxx)