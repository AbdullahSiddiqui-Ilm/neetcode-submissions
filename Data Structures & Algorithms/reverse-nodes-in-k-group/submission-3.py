# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        previous_group = None
        while curr:
            check = curr
            count = 0
            while check and count < k:
                check = check.next
                count += 1
            if count < k:
                break
            prev = None
            group_tail = curr
            while count > 0:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                count -= 1

            # prev = new head of reversed group; 1 - 2 - 3 --> prev -> 3 - 2 - 1
            # group_tail = new tail of reversed group 
            # curr = start of next group

            # set the group's tail next to the start of next group, ie curr
            # if we have a previous group, set its next to reversed groups head, prev
            # set previous group to the new reversed groups tail
            # return head to return the reverse of the linked list

            group_tail.next = curr

            if previous_group:
                previous_group.next = prev
            else:
                head = prev
            previous_group = group_tail
        return head

            

            
            

"""

- Check whether at least k nodes are available starting from curr.
- If fewer than k, stop and leave those nodes unchanged.
- If at least k, reverse exactly those k nodes.
- Reconnect the reversed group to the previous group and the remaining list.
- Move curr to the first node of the next group.
- Repeat.

- previous_group
- group_start
- group_end
- next_group

"""