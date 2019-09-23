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
    ListNode* reverseList(ListNode* head) {
        if (!head){
            return nullptr;
        }
        ListNode* slow = head;
        ListNode* fast = head;

        while (head->next){
            fast = head->next;

            if (fast->next){
                head->next = fast->next;
            }
            else{
                head->next = nullptr;
            }

            fast->next = slow;
            slow = fast;
        }
        return fast;
    }
};

/*
Runtime: 8 ms, faster than 77.04% of C++ online submissions for Reverse Linked List.
Memory Usage: 9.1 MB, less than 100.00% of C++ online submissions for Reverse Linked List.
*/