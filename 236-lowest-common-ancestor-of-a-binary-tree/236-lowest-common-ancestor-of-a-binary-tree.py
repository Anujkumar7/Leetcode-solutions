# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    # BaseCase: if root is reached at null return root or if p or q found return that root
        if root == None or root== p or root==q:
            return root
        
  #After that we move to left and right      
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right, p ,q)
        
# While coming back if the left node is null return the right one or vice versa
        if left== None:
            return right
        elif right== None:
            return left
 # If above both condition are not true that means we have found that root under which both p and q lies       
        else:
            return root