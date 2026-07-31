# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.inorder_list = []
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return self.inorder_list

        if root.left:
            self.inorderTraversal(root.left)

        self.inorder_list.append(root.val)

        if root.right:
            self.inorderTraversal(root.right)

        return self.inorder_list