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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int carry = 0,sum = 0;
        ListNode head1 = l1;
        ListNode head2 = l2;
        ListNode head = new ListNode(0,new ListNode());
        ListNode curr = head.next;
        while(head1!=null && head2!=null){
            sum = (head1.val + head2.val + carry)%10;
            carry = (head1.val + head2.val + carry)/10;
            curr.val = sum;
            if(head1.next!=null && head2.next!=null){
                curr.next = new ListNode();
                curr = curr.next;
            }
            head1 = head1.next;
            head2 = head2.next;
        }
        while(head1!=null){
            curr.next = new ListNode();
            curr = curr.next;
            curr.val = (head1.val + carry)%10;
            carry = (head1.val+carry)/10;
            if(head1.next==null){
                break;
            }
            head1 = head1.next;
        }
        while(head2!=null){
            curr.next = new ListNode();
            curr = curr.next;
            curr.val = (head2.val + carry)%10;
            carry = (head2.val+carry)/10;
            if(head2.next==null){
                break;
            }
            head2 = head2.next;
        }
        if(carry!=0){
            curr.next = new ListNode();
            curr = curr.next;
            curr.val = carry;
        }
        return head.next;
    }
}