# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Fast and slow pointers to calculate mid point of linked list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = slow.next # whether our linked list has an even or odd length, 
        slow.next = None
        prev = None

        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        l = head
        r = prev

        while r:
            temp = l.next
            temp2 = r.next
            l.next = r
            r.next = temp
            l = temp
            r = temp2
        

