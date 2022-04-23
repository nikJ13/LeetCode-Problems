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
    
    private boolean helper(TreeNode node, TreeNode subnode){
        if(node==null && subnode==null){
            return true;
        }
        if((node!=null && subnode==null)||(node==null && subnode!=null)){
            return false;
        }
        // the only case left is when the node is not null and subnode is also not null
        if(node.val!=subnode.val){
            return false;
        }
        return helper(node.left,subnode.left) && helper(node.right,subnode.right);
    }
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        if(root!=null){
            if(root.val==subRoot.val){
                if(helper(root,subRoot)){
                    return true;
                }
            }
            return isSubtree(root.left,subRoot) || isSubtree(root.right,subRoot);
        }
        return false;
    }
}