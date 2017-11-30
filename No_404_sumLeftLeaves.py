# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        # this is how you use stack
        if not root: return 0

        stack = [root]
        res = 0
        while stack:
            tmp = stack.pop()
            if tmp.left:
                stack.append(tmp.left)
                if not tmp.left.left and not tmp.left.right:
                    res += tmp.left.val
            if tmp.right:
                stack.append(tmp.right)
        return res
