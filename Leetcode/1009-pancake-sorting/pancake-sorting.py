class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = []
        for i in range(n-1,0,-1):
            maxx = max(arr[:i+1])
            if maxx == arr[i]:
                continue
            elif maxx == arr[0]:
                res.append(i+1)
                temp = (arr[:i+1])
                temp.reverse()
                for j in range(i+1):
                    arr[j] = temp[j]
                continue
            for j in range(i):
                if arr[j] == maxx:
                    res.append(j+1)
                    res.append(i+1)
                    temp = arr[j+1:i+1]
                    a,b = i,j
                    while b >= 0:
                        arr[a] = arr[b]
                        b -= 1
                        a -= 1
                    for k in range(len(temp)):
                        arr[a] = temp[k]
                        a -= 1
                    break         
        return res
        