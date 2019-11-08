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
    ListNode *detectCycle(ListNode *head) {
        if ((!head) || (!head->next) || (!head->next->next)){
            return nullptr;
        }
        ListNode* slow = head->next;
        ListNode* fast = head->next->next;
        while (slow != fast){
            if (!(slow->next)){
                return nullptr;
            }
            slow = slow->next;
            if (!(fast->next)){
                return nullptr;
            }
            fast = fast->next;
            if (!(fast->next)){
                return nullptr;
            }
            fast = fast->next;
        }
        fast = head;
        while (slow != fast){
            slow = slow->next;
            fast = fast->next;            
        }
        return slow;
    }
};


/*
Runtime: 12 ms, faster than 75.80% of C++ online submissions for Linked List Cycle II.
Memory Usage: 9.8 MB, less than 69.05% of C++ online submissions for Linked List Cycle II.
*/