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
    ListNode* middleNode(ListNode* head) {
        if (!head){
            return nullptr; 
        }
        ListNode* slowptr = head;
        ListNode* fastptr = head;
        while (1){
            if (fastptr ->next){
            slowptr = slowptr ->next;
            fastptr = fastptr ->next;
            }
            else{
                break;
            }
            if (fastptr ->next){
                fastptr = fastptr->next;
            }
            else{
                break;
            }
        }
        return slowptr;
    }
};

/*
Runtime: 0 ms, faster than 100.00% of C++ online submissions for Middle of the Linked List.
Memory Usage: 8.5 MB, less than 69.49% of C++ online submissions for Middle of the Linked List.
*/