# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    #Intialise array
        res = []
        
    #Initializing queue    
        q = collections.deque()
        q.append(root)
        
        while q:
    # For ensuring we are going one level at a time        
            qlen = len(q)
            level = []
            for i in range(qlen):
                
             #FIFO   
                node = q.popleft()
                if node:
                    level.append(node.val)
         #Adding children           
                    q.append(node.left)
                    q.append(node.right)
                
#Technically our list can have null nodes , we are not adding null nodes in res
            if level:
                res.append(level)
        return res