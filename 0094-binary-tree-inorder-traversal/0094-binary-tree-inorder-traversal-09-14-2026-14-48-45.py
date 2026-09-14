# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        white ,gray = 0, 1
        stack = [(white, root)]
        ret = []
        while stack:
            color, node = stack.pop()
            if node == None:
                continue
            if white == color:
                stack.append((white, node.right))
                stack.append((gray, node))
                stack.append((white, node.left))
            else:
                ret.append(node.val)
        return ret