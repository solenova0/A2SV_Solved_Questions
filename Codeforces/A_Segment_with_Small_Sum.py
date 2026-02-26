n , s = map(int, input().split())
nums = list(map(int, input().split()))   
n=len(nums)
ans=0
Window = 0
left=0 
for right in range(n):
    Window += nums[right]
    while Window > s:
        Window -= nums[left]        
        left += 1  
               
    ans = max(ans, right - left + 1)  # update the answer 
print(ans)