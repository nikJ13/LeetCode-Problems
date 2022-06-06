/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode ptrA = headA;
        ListNode ptrB = headB;
        while(ptrA!=ptrB){
            if(ptrA!=null){
                ptrA = ptrA.next;
            }else{
                ptrA = headB;
            }
            if(ptrB!=null){
                ptrB = ptrB.next;
            }else{
                ptrB = headA;
            }
        }
        return ptrA;
    }
}