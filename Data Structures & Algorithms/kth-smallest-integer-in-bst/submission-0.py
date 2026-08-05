# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.i = 0
        self.answer = None

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return
            
        if root.left:
            self.kthSmallest(root.left, k)

        self.i += 1
        if self.i == k:
            self.answer = root.val
            
        if root.right:
            self.kthSmallest(root.right, k)

        return self.answer


        

        

        