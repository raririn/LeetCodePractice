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
    ListNode* removeElements(ListNode* head, int val) {
        if (!head){
            return nullptr;
        }
        ListNode* cur = head;
        while (head->val == val){
            head = head->next;
            if (!head){
                return nullptr;
            }
        }
        while (cur->next){
            if (cur->next->val == val){
                cur->next = cur->next->next;
            }
            else{
                cur = cur->next;
            }
        }
        return head;
    }
};

/*
Runtime: 28 ms, faster than 66.07% of C++ online submissions for Remove Linked List Elements.
Memory Usage: 10.8 MB, less than 100.00% of C++ online submissions for Remove Linked List Elements.
*/