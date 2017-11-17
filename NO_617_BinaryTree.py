class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 != None and t2 != None:
            new_tree = TreeNode(t1.val + t2.val)
            new_tree.left = self.mergeTrees(t1.left, t2.left)
            new_tree.right = self.mergeTrees(t1.right, t2.right)
        elif t1 != None:
            new_tree = TreeNode(t1.val + 0)
            new_tree.left = self.mergeTrees(t1.left, None)
            new_tree.right = self.mergeTrees(t1.right, None)
        elif t2 != None:
            new_tree = TreeNode(t2.val + 0)
            new_tree.left = self.mergeTrees(t2.left, None)
            new_tree.right = self.mergeTrees(t2.right, None)
        else:
            return None
        
        return new_tree
