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
    public TreeNode mergeTrees(TreeNode root1, TreeNode root2) {
        if(root1==null && root2!=null){
            return root2;
        }
        if(root1!=null && root2==null){
            return root1;
        }
        if(root1==null && root2==null){
            return root1;
        }
        TreeNode head = root1;
        TreeNode node1;
        TreeNode node2;
        LinkedList<TreeNode> que1 = new LinkedList<TreeNode>();
        LinkedList<TreeNode> que2 = new LinkedList<TreeNode>();
        que1.add(root1);
        que2.add(root2);
        int k;
        while(que1.size()!=0 && que2.size()!=0){
            k = que1.size();
            for(int i=0;i<k;i++){
                node1 = que1.poll();
                node2 = que2.poll();
                node1.val = node1.val + node2.val;
                if(node1.left==null && node2.left!=null){
                    node1.left = new TreeNode(0,null,null);
                }else if(node1.left!=null && node2.left==null){
                    node2.left = new TreeNode(0,null,null);
                }
                if(node1.left!=null){
                    que1.add(node1.left);
                }
                if(node2.left!=null){
                    que2.add(node2.left);
                }
                if(node1.right!=null && node2.right==null){
                    node2.right = new TreeNode(0,null,null);
                }else if(node1.right==null && node2.right!=null){
                    node1.right = new TreeNode(0,null,null);
                }
                if(node1.right!=null){
                    que1.add(node1.right);
                }
                if(node2.right!=null){
                    que2.add(node2.right);
                }
            }
        }
        return head;
    }
}