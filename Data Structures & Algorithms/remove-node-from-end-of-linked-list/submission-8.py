# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        
        point1 = head
        steps = 0

        while steps < n:
            point1 = point1.next
            steps += 1

        dummy = ListNode()
        point2 = dummy
        point2.next = head

        if point1 == None:
            head = head.next
            return head
        else:
            while point1:
                point1 = point1.next
                point2 = point2.next
            point2.next = point2.next.next
            return head
        
           