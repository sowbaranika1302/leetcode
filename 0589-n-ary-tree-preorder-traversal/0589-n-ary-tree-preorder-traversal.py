"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
#add the children of the temp into the stack in reverse order.
            # children of 1 = [3,2,4], if not reveresed then 4 will be popped out first from the stack.
            # if reversed then stack = [4,2,3]. Here 3 will pop out first.
            # This continues till the stack is empty.
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:               
        if not root:
            return None
        stack = [root]
        output = []
        while stack:
            temp = stack.pop()
            output.append(temp.val)
            stack.extend(temp.children[::-1])
        return output