/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    
    private boolean helper(TreeNode root1, TreeNode root2){
        if(root1==null && root2==null){
            return true;
        }
        if((root1!=null && root2==null)||(root1==null && root2!=null)){
            return false;
        }
        if(root1!=null){
            if(root1.val!=root2.val){
                return false;
            }
            return helper(root1.left,root2.left) && helper(root1.right,root2.right);
        }
        return true;
    }
    public boolean isSameTree(TreeNode p, TreeNode q) {
        TreeNode root1 = p;
        TreeNode root2 = q;
        return helper(root1,root2);
    }
}