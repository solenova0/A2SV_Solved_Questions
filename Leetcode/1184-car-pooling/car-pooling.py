class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        time = [0] * 1001
        
        for pas, i, j in trips:
            time[i] += pas
            time[j] -= pas
        
        curr = 0
        for k in time:
            curr += k
            if curr > capacity:
                return False
                
        return True
       