# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head  
        previous = None
        next_node = 0

        while current:

            next_node = current.next # here we get the next node first

            current.next = previous  # we update the current address pointer
             
            previous = current  # here we send current to previous
            
            current = next_node  # this is my counter to move forward
            
        return previous
        