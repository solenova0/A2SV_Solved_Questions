class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index= {v: i for i, v in enumerate(list1)}
        
        min_sum = float('inf')
        res = []
        
        for j, v in enumerate(list2):
            if v in index:
                total = j + index[v]
                
                if total < min_sum:
                    min_sum = total
                    res = [v]
                elif total == min_sum:
                    res.append(v)
                    
        return res

            

            