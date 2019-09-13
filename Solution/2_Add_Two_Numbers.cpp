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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        /* Note there is a constructor defined. */
        if (!l1){
            return l2;
        }
        if (!l2){
            return l1;
        }
        int carry = 0;
        ListNode *ret = new ListNode(-1);
        ListNode *cur = ret;

        int temp_sum = 0;
        while (l1 || l2 || (carry != 0)){
            temp_sum = (l1? l1->val : 0) + (l2? l2->val : 0) + carry;
            carry = temp_sum / 10;
            temp_sum = temp_sum % 10;
            cur->next = new ListNode(temp_sum);
            cur = cur->next;
        
            if (l1){
                l1 = l1->next;
            }
            if (l2){
                l2 = l2->next;
            }
        }
        return ret->next;
    }
};