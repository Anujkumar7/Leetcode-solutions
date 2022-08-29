"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, node: 'Optional[Node]') -> 'Optional[Node]':
      #root as Node    
        cur , nxt = node, node.left if node else None
        
    #Performing BFS     
        while cur and nxt:
    #Connecting childs        
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left
                
       #Shifting the nodes in the same level         
            cur = cur.next
            if not cur:
                cur = nxt #Nxt level
                nxt = cur.left
                
        return node