/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if (!l1){
            return l2;
        }
        if (!l2){
            return l1;
        }
        ListNode* ret = new ListNode(-1);
        ListNode* temp = ret;
        while (l1 && l2){
            if ((l1 ->val) >= (l2 ->val)){
                temp ->next = l2;
                /* Note it's not the opposite: we point temp to its next (which was l2) */
                temp = temp ->next;
                l2 = l2 ->next;
            }
            else{
                temp ->next = l1;
                temp = (temp ->next);
                l1 = l1 ->next;
            }
        }

        while (l1){
            temp ->next = l1;
            temp = (temp ->next);
            l1 = l1 ->next;
        }
        while (l2){
            temp ->next = l2;
            temp = (temp ->next);
            l2 = l2 ->next;
        }
        return ret ->next;
    }
};

/*
Runtime: 12 ms, faster than 10.52% of C++ online submissions for Merge Two Sorted Lists.
Memory Usage: 8.9 MB, less than 86.07% of C++ online submissions for Merge Two Sorted Lists.
*/