# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        od, ev = head, head.next
        even_head = ev
        
        while ev and ev.next:
            od.next = ev.next
            od = od.next
            ev.next = ev.next.next
            ev = ev.next

        od.next = even_head 
        return head