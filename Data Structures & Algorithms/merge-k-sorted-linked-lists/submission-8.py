# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if not lists[0] and len(lists) == 1:
            return None
        
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                mergedLists.append(self.mergeTwoLists(l1, l2))
            lists = mergedLists

        return lists[0]

    def mergeTwoLists(self, list1, list2) -> Optional[ListNode]:
        if not list2:
            return list1
        
        dummy = ListNode()
        curr = dummy

        p1 = list1
        p2 = list2

        while p1 and p2:
            if p1.val > p2.val:
                curr.next = p2
                p2 = p2.next
                curr = curr.next
            else:
                curr.next = p1
                p1 = p1.next
                curr = curr.next
        if p1:
            curr.next = p1
            curr = curr.next
        else:
            curr.next = p2
            curr = curr.next
        return dummy.next


"""
    - define function mergeTwoLists
    - do a merge sort on lists[i - 1] and lists[i]
    - keep merging neighbouring lists until we have 1 list remaining
    - using 'while len(lists) > 1'
    - replace lists with merged lists every iteration (inside the while loop)
    - once we have 1 list remaining, return head
"""
