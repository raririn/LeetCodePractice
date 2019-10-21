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
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        if ((!headA) || (!headB)){
            return nullptr;
        }
        ListNode* p1 = headA;
        ListNode* p2 = headB;
        while (p1 != p2){
            if ((!p1->next) && (!p2->next)){
                return nullptr;
            }
            if (p1->next){
                p1 = p1->next;
            }
            else{
                p1 = headB;
            }
            if (p2->next){
                p2 = p2->next;
            }
            else{
                p2 = headA;
            }
        }
        return p1;
    }
};

/*
Runtime: 60 ms, faster than 22.29% of C++ online submissions for Intersection of Two Linked Lists.
Memory Usage: 16.8 MB, less than 74.07% of C++ online submissions for Intersection of Two Linked Lists.
*/