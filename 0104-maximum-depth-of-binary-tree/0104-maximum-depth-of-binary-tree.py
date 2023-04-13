# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(self, root, depth):
            if not root:
                return depth
            return max(dfs(self,root.left,depth+1),dfs(self,root.right,depth+1))
            
        
        return dfs(self,root,0)
        
        