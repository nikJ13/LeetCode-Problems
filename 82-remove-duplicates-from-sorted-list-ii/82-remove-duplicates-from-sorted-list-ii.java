/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        ListNode temp = new ListNode(0,head);
        ListNode curr = temp;
        while(head!=null){
            if(head.next!=null && head.next.val==head.val){
                while(head.next!=null && head.next.val==head.val){
                    head = head.next;
                }
                curr.next = head.next;
            }else{
                curr = curr.next;
            }
            head = head.next;
        }
        return temp.next;
    }
}