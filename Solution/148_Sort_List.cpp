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
    ListNode* sortList(ListNode* head) {
        if (!head){
            return nullptr;
        }
        ListNode* cur = head->next;
        ListNode* it;
        ListNode* dummy;
        head->next = nullptr;
        while (cur){
            dummy = cur->next;
            if (cur->val <= head->val){
                cur->next = head;
                head = cur;
            }
            else{
                for (it = head; it->next; it = it->next){
                    if (it->next->val > cur->val){
                        break;
                    }
                }
                cur->next = it->next;
                it->next = cur;
            }
            cur = dummy;
        }
        return head;
    }
};

/*
Runtime: 1144 ms, faster than 5.13% of C++ online submissions for Sort List.
Memory Usage: 11.6 MB, less than 100.00% of C++ online submissions for Sort List.
*/