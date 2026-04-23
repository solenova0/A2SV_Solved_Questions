s = input()
stack = [-1]
maxlen = 0
for i , v in enumerate(s):
    if v == "(":
        stack.append(i)
    else:
        stack.pop()
        if not stack:
            stack.append(i)
        else:
            if i - stack[-1] > maxlen:
                maxlen = i - stack[-1]
                count = 1
            elif i - stack[-1] == maxlen:
                count += 1
if maxlen == 0:
    count = 1
print(maxlen , count)

# t = int(input())
# for _ in range(t):
#     x = int(input())
#     val = x % 10  # Get the digit (since x consists of the same digit)
#     ans = 10 * (val - 1)  # Count keypresses for previous digits
#     sz = len(str(x))  # Get the number of digits in x
#     ans += sum(range(1, sz + 1))  # Add keypresses for the current digit
#     print(ans)




# t = int(input()) 
# for _ in range(t):
#     n, s = [int(i) for i in input().split()]
#     left, right = 0, s + 1
#     while left <= right:
#         M = (left + right) // 2  
#         m = n // 2 + 1 
        
#         if m * M <= s:
#             left = M + 1
#             answer = M

#         else:
#             right = M - 1 
    
#     print(answer) 






# def solve():
#     # Read input values: number of spaceships (s) and number of bases (b)
#     s, b = map(int, input().split())
    
#     # Read the attacking power of each spaceship
#     ships = list(map(int, input().split()))
    
#     # Read the defensive power and gold of each base
#     bases = [list(map(int, input().split())) for _ in range(b)]
    
#     # Step 1: Sort bases by defensive power to process them efficiently
#     bases.sort()
    
#     # Step 2: Sort spaceships by attacking power while keeping track of original indices
#     ships = sorted((ships[i], i) for i in range(s))
    
#     # Array to store the maximum gold each spaceship can steal
#     ans = [0] * s
    
#     # Two-pointer approach to efficiently determine how much gold each spaceship can steal
#     l, max_gold = 0, 0
    
#     # Step 3: Process each spaceship in increasing order of attacking power
#     for i in range(s):
#         # Move the pointer 'l' to include all bases that the spaceship can attack
#         while l < b and bases[l][0] <= ships[i][0]:
#             max_gold += bases[l][1]  # Add the gold from the base
#             l += 1  # Move to the next base
        
#         # Store the total gold that this spaceship can steal
#         ans[ships[i][1]] = max_gold  # Store result at original index
    
#     # Step 4: Print the results in the original order of spaceships
#     print(*ans)

# if __name__ == "__main__":
#     solve()


# import sys

# def solve():
#     n, k = map(int, sys.stdin.readline().strip().split())
#     s = sys.stdin.readline().strip()
#     prefix = [0]
    
#     # Compute prefix sum for counting free rooms quickly
#     for val in s:
#         prefix.append(prefix[-1] + (1 if val == '0' else 0))
    
#     def max_cows_in_range(d):
#         """Given max distance d, calculate the maximum number of cows that can be placed"""
#         max_cows = 0
#         for i in range(n):
#             if s[i] == '0':  # Consider only unoccupied rooms
#                 left = max(0, i - d)
#                 right = min(n, i + d + 1)
#                 max_cows = max(max_cows, prefix[right] - prefix[left])
#         return max_cows
    
#     # Binary search for the minimum possible maximum distance
#     l, r = 0, n
#     while l < r:
#         mid = (l + r) // 2
#         if max_cows_in_range(mid) >= k + 1:
#             r = mid  # Try a smaller maximum distance
#         else:
#             l = mid + 1
    
#     print(l)

# if __name__ == "__main__":
#     solve()
