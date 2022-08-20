# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self,s: TreeNode,t: TreeNode) -> bool:
        if not t: return True
        if not s: return False
        
 # If both of the trees are same return true       
        if self.sameTree(s,t):
            return True
        
# Checking if t is the left subtree of s OR t is the right subtree of s        
        return(self.isSubtree(s.left,t)or
              self.isSubtree(s.right, t))
    
# Helper func sameTree 
    def sameTree(self, s,t):
        
#If both empty return True
        if not s and not t:
            return True
        
##If both of them are not empty
        if s and t and s.val== t.val:
            return (self.sameTree(s.left, t.left)and
                    self.sameTree(s.right, t.right))
# If neither of this condition works that means one of the tree is empty hence return False
        return False