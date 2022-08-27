# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid_bst(root, minval, maxval):
            if root == None:
                return True
            
            elif root.val>= maxval or root.val<= minval:
                return False
            
            return valid_bst(root.left, minval, root.val) and valid_bst(root.right, root.val, maxval)
        
        return valid_bst(root, -math.inf, math.inf)