# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)     # a dummy node to start out linked list from 
        curr = dummy            # Points to the last node in the merged list.

        while list1 and list2:            # if both list exist
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
                curr = curr.next

            else:                      # list2.val < list1.val
                curr.next = list2
                list2 = list2.next
                curr = curr.next

        if list1 is None:   #if only one of the list exist
            curr.next = list2
        else:
            curr.next = list1
            
        return dummy.next      # Return the head of the merged list.