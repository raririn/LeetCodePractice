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

#include <cstdlib>

class Solution {
public:
    /** @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node. */
    Solution(ListNode* head) {
        this->head = head;
    }
    
    /** Returns a random node's value. */
    int getRandom() {
        int count = 1;
        int ret = this->head->val;
        ListNode* cur = this->head;
        while (cur->next) {
            cur = cur->next;
            count += 1;
            if (rand() % count == 0) {
                ret = cur->val;
            }
        }
        return ret;
    }
private:
    ListNode* head;
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(head);
 * int param_1 = obj->getRandom();
 */

/*
Runtime: 96 ms, faster than 8.94% of C++ online submissions for Linked List Random Node.
Memory Usage: 16.5 MB, less than 93.84% of C++ online submissions for Linked List Random Node.
*/