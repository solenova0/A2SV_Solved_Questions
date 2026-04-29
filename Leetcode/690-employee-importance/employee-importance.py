"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        from collections import deque
        emp_map = {e.id: e for e in employees}
        queue = deque([id])
        total = 0

        while queue:
            curr_id = queue.popleft()
            emp = emp_map[curr_id]

            total += emp.importance 

            for sub in emp.subordinates:
                queue.append(sub)

        return total