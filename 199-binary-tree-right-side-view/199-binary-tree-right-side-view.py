# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def helper(node, level):
            if node:
                if level == len(res):
                    res.append(node.val)
                helper(node.right, level+1)
                helper(node.left, level+1)
        res = []
        helper(root, 0)
        return res
