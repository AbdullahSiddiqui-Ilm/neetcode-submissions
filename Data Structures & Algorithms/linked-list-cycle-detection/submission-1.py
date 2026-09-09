# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        
        fast_p = head.next
        slow_p = head

        while fast_p != slow_p:
            if fast_p == None or fast_p.next == None:
                return False
            else:
                fast_p = fast_p.next.next
                slow_p = slow_p.next
        return True
            
        
