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
    ListNode* deleteDuplicates(ListNode* head) {
        if (!head){
            return nullptr;
        }
        ListNode* cur = head;
        while (cur->next){
            if (cur->next->val == cur->val){
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
Runtime: 12 ms, faster than 72.55% of C++ online submissions for Remove Duplicates from Sorted List.
Memory Usage: 9.2 MB, less than 98.11% of C++ online submissions for Remove Duplicates from Sorted List.
*/