/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public int getDecimalValue(ListNode head) {
        int ret = 0;
        while (head != null){
            ret = (ret << 1) | head.val;
            head = head.next;
        }
        return ret;
    }
}

/*
Runtime: 0 ms, faster than 100.00% of Java online submissions for Convert Binary Number in a Linked List to Integer.
Memory Usage: 37.3 MB, less than 100.00% of Java online submissions for Convert Binary Number in a Linked List to Integer.
*/