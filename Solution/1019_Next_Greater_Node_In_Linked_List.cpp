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
    vector<int> nextLargerNodes(ListNode* head) {
        vector<int> ret;
        if (!head){
            return ret;
        }
        ListNode* slow = head;
        ListNode* fast = head;
        bool flag = false;
        while (slow){
            std::cout << "slow" << slow->val <<std::endl;
            flag = false;
            while (fast->next){
                fast = fast->next;
                std::cout << fast->val <<std::endl;
                if (fast->val > slow->val){
                    ret.push_back(fast->val);
                    flag = true;
                    break;
                }
            }
            if (!flag){
                ret.push_back(0);
            }
            slow = slow->next;
        }
        return ret;
    }
};

/*
Runtime: 1500 ms, faster than 13.96% of C++ online submissions for Next Greater Node In Linked List.
Memory Usage: 24.4 MB, less than 88.24% of C++ online submissions for Next Greater Node In Linked List.
*/