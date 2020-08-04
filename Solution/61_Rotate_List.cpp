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
    ListNode* rotateRight(ListNode* head, int k) {
        if (!head) {
            return nullptr;
        }
        if (!k) {
            return head;
        }

        int len = 1;
        ListNode* cur = head;
        while (cur->next) {
            len++;
            cur = cur->next;
        }

        if (len==1) {
            return head;
        }

        k = len - k % len - 1;


        cout << len << endl;        
        cur = head;
        while (k) {
            cur = cur->next;
            k--;
        }

        ListNode* newtail = cur;
        cur = cur->next;

        if (!cur) {
            return head;
        }

        newtail->next = nullptr;
        ListNode* newhead = cur;

        while (cur->next) {
            cur = cur->next;
        }
        cur->next = head;
        return newhead;
    }
};

/*
Runtime: 4 ms, faster than 97.59% of C++ online submissions for Rotate List.
Memory Usage: 11.3 MB, less than 53.71% of C++ online submissions for Rotate List.
*/