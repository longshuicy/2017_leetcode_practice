/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public int maxDepth(TreeNode root) {
        
        int depth = 1;
        
        if (root != null){
            
            depth += Math.max(maxDepth(root.left),maxDepth(root.right));
            return depth;
        }
        else{
            return 0;
        }
    }
}



if __name__ != '__main__':
    test = Solution()
    root = [2,null,1]
    print(test.maxDepth(root))

