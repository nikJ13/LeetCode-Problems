/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}
    
    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/

class Solution {
    public Node connect(Node root) {
        if(root==null){
            return null;
        }
        Queue<Node> que = new LinkedList<Node>();
        que.add(root);
        while(!que.isEmpty()){
            int k = que.size();
            for(int i=0;i<k;i++){
                Node node = que.remove();
                if(i==k-1){
                    node.next = null;
                }else{
                    node.next = que.peek();
                }
                if(node.left!=null){
                    que.add(node.left);
                }
                if(node.right!=null){
                    que.add(node.right);
                }
            }
        }
        return root;
    }
}