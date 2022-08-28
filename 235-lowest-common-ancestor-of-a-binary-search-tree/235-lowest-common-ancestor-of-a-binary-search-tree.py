# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
     #If found what we want or there is nothing
        if root == None or root==p or root==q:
            return root
       
    #Recursion
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right, p, q)
       
        if left and right:
            return root
        elif left:
            return left
        elif right:
            return right
        
     #Another approach
     # right = max(p.val, q.val)
     #    left = min(p.val, q.val)
     #    if root.val < left:
     #        return self.lowestCommonAncestor(root.right, p, q)
     #    elif root.val > right:
     #        return self.lowestCommonAncestor(root.left, p, q)
     #    else:
     #        return root