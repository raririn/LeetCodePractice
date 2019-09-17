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
    bool hasCycle(ListNode *head) {
        if (!head){
            return 0;
        }
        ListNode* slowptr = head;
        ListNode* fastptr = head;
        while (1){
            if (slowptr ->next){
                slowptr = slowptr ->next;
            }
            else{
                return 0;
            }
            if (fastptr ->next){
                fastptr = fastptr ->next;
            }
            else{
                return 0;
            }
            if (fastptr ->next){
                fastptr = fastptr ->next;
            }
            else{
                return 0;
            }
            if (slowptr == fastptr){
                break;
            }
        }
        return 1;
    }
};

/*
Runtime: 16 ms, faster than 22.86% of C++ online submissions for Linked List Cycle.
Memory Usage: 9.7 MB, less than 100.00% of C++ online submissions for Linked List Cycle.
*/