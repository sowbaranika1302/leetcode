# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(p,q):
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            elif p.val == q.val:
                return True
            else:
                return False
        deq = deque([(p,q)])
        while deq:
            
            p,q = deq.popleft()
            if not check(p,q):
                return False
            if p:
                deq.append((p.left,q.left))
                deq.append((p.right,q.right))
        return True
            
