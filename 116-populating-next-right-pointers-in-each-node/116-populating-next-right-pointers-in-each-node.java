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
        LinkedList<Node> que = new LinkedList<Node>();
        Node head = root;
        que.add(root);
        Node node;
        //Node temp = new Node(null,null,null,null);
        while(que.size()!=0){
            int k = que.size();
            for(int i=0;i<k;i++){
                node = que.poll();
                if(i!=k-1){
                    node.next = que.peek();
                }else{
                    node.next = null;
                }
                if(node.left!=null){
                    que.add(node.left);
                }
                if(node.right!=null){
                    que.add(node.right);
                }
            }
       }
        return head;
    }
}