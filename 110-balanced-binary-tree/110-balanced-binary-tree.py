# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self,root):
        if root ==None:
            return 0
        return 1+ max(self.height(root.left), self.height(root.right))
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        lh = self.height(root.left)
        rh = self.height(root.right)
        if lh - rh >1 or rh - lh >1:
            return False
        
        isLeftBalanced = self.isBalanced(root.left)
        isRightBalanced = self.isBalanced(root.right)
        if isLeftBalanced and isRightBalanced:
            return True
        else:
            return False