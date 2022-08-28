# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
   #If root is null then create a node which is the val     
        if root == None:
            return TreeNode(val)
        
   #Else iterate through recursion to left and right subtree     
        if (root.val > val):
            root.left = self.insertIntoBST(root.left, val)
        
        if (root.val < val):
            root.right =  self.insertIntoBST(root.right, val)
            
        return root