# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        info = []
        
        def dfs(node,depth):
            if node:
                if len(info) <= depth:
                    info.append([0,0])
                    
                info[depth][0] += node.val
                info[depth][1] += 1
                
                dfs(node.left, depth + 1)
                dfs(node.right, depth + 1)
                
        dfs(root, 0 )
        
        return [ sum/float(count) for sum,count in info]
