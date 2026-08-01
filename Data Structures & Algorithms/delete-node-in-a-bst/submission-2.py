# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
#         if root is None:
#             return root

#         if root.val > key:
#             root.left = self.deleteNode(root.left, key)

#         elif root.val < key:
#             root.right = self.deleteNode(root.right, key)

#         else: # we found key
#             if root.left is None:
#                 return root.right
#             elif root.right is None:
#                 return root.left

#             curr = root.right
#             while curr.left:
#                 curr = curr.left
#             root.val = curr.val
#             root.right = self.deleteNode(root.right, root.val)

#         return root
# # -----------------------------------------------------------------------
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root

        if root.val > key:
            root.left = self.deleteNode(root.left, key)

        elif root.val < key:
            root.right = self.deleteNode(root.right, key)

        else: # we found match 
            if root.right is None:
                return root.left
            if root.left is None:
                return root.right

            curr = root.left
            while curr.right:
                curr = curr.right  # i'll find largest on the right subtree
            root.val = curr.val
            root.left = self.deleteNode(root.left, root.val)

        return root
            






