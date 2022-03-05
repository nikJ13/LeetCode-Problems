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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if(list1==null && list2==null){
            return null;
        }
        if(list1==null){
            return list2;
        }
        if(list2==null){return list1;}
        ListNode head1 = list1;
        ListNode head2 = list2;
        ListNode head = new ListNode(0,null);
        ListNode curr = head;
        while(head1!=null && head2!=null){
            if(head1.val<=head2.val){
                curr.next = head1; 
                head1 = head1.next; 
            }
            else{
                curr.next = head2; 
                head2 = head2.next;  
            }
            curr = curr.next;
        }
        curr.next = head1==null?head2 : head1;
        return head.next;
    }
}