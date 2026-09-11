# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Fast and slow pointers to calculate mid point of linked list
        slow, fast = head, head.next # look at comments below: 1) 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = slow.next # 2)
        slow.next = None 
        prev = None     

        while curr != None:  # Reverse 2nd half of linked list
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        list1 = head
        list2 = prev

        while list2:
            temp = list1.next # reorder the list. 3)
            temp2 = list2.next
            list1.next = list2
            list2.next = temp
            list1 = temp
            list2 = temp2
"""
1)we can start the fast pointer at either head or head.next. head.next is cleaner
as the list seperation is not affected by the lin ked list being even or odd length, however
started fast at head will create an uneven list when list length is even. e.g: 
{ 1 -> 2 -> 3 -> 4 -> None } after 2 iterations, fast will point at None(technically), and slow
will point at 3. This gives us a seperation of { 1 -> 2 -> 3 } and { 4 }. This still gives us the 
result wanted when we reorder the list, however it may seem unconsistent to some, therefore 
setting to fast to head.next creates a consistent split accross the linked list when even and odd.

2)whether our linked list has an even or odd length, we stop at the same 
value, therefore to identity the part of the linked list thats going to
be reversed, we set 'curr' to the value after slow. to seperate both lists, we set slow.next to 
null/None.

3) temp values are to preserve the next values from being out of bounds, as we are rearranging
the current next values of both linked lists.

"""

