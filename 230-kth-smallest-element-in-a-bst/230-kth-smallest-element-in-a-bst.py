# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count= 0
        res = []
        cur = root
        
        while cur or res:
            
#We are just keep going left because thats how inorder traversal works  
            while cur:     
                res.append(cur)
                cur = cur.left
            cur = res.pop()
            count+=1
            
            if count==k:
                return cur.val
      #We can go to right subtree also      
            cur = cur.right