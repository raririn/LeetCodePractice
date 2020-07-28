/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {
        if (!head) {
            return nullptr;
        }

        ListNode* even_head = new ListNode(-1);
        ListNode* even_cur = new ListNode(-1);
        even_head->next = even_cur;
        ListNode* cur = head;


        while (cur->next) {
            even_cur->next = cur->next;
            even_cur = even_cur->next;

            if (cur->next->next) {
                cur->next = cur->next->next;
            }
            else {
                break;
            }
            cur = cur->next;
        }
        cur->next = even_head->next->next;
        even_cur->next = nullptr;
        return head;
    }
};


/*
Runtime: 8 ms, faster than 99.41% of C++ online submissions for Odd Even Linked List.
Memory Usage: 10 MB, less than 5.94% of C++ online submissions for Odd Even Linked List.
*/