# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#First intialise a diameter counter from 0
        self.diameter = 0
    
# Function of height    
        def height(node):
            if node== None:
                return 0
            l = height(node.left)
            r = height(node.right)
            self.diameter = max(self.diameter, l + r)
            return max(l, r) + 1
        height(root)
        return self.diameter

    