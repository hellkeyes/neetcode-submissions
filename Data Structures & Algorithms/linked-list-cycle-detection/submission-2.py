# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        i = 0
        current = head

        while current:
            if current.next == None:
                return False

            else:
                if current in seen:
                    return True
                seen.add(current)

            i += 1
            current = current.next

        return False

