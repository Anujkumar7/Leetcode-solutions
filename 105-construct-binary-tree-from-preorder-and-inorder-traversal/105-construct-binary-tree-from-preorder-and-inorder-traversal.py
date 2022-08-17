# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
#If preorder or inorder is null
        if not preorder or not inorder:
            return None

#Starts from preorder index 0        
        
        root = TreeNode(preorder[0])
        
# Finding that index in inorder         
        mid=inorder.index(preorder[0])
    
 # Building Subtree:  in preorder from 1th index(because 0th index is the root) to mid+1 ele   and in inorder from start to mid but not including mid 
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
    
#For building right subtree we need values after the above root.left
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root