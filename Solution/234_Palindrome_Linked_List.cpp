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
    bool isPalindrome(ListNode* head) {
        /*
        Very bad attempt. Use modern hash instead.
        */
        if (!head){
            return true;
        }
        ListNode* fast = head;
        int count = 1;
        float hash = 0;
        while (fast->next){
            count++;
            fast = fast->next;
        }
        fast = head;
        if (!(count & 1)){
            for (int i = 0; i < count/2; i++){
                hash += (fast->val  );
                hash *= 7;
                fast = fast->next;
            }
            for (int i = 0; i < count/2; i++){
                hash /= 7;
                hash -= (fast->val  );
                fast = fast->next;
            }
            return hash < 0.01 && hash > -0.01;
        }
        else{
            for (int i = 0; i < (count-1)/2; i++){
                hash += (fast->val  );
                hash *= 7;
                fast = fast->next;
            }
            fast = fast->next;
            for (int i = 0; i < (count-1)/2; i++){
                hash /= 7;
                hash -= (fast->val  );
                fast = fast->next;
            }
            return hash < 0.01 && hash > -0.01;            
        }
    }
};

/*
Runtime: 20 ms, faster than 91.60% of C++ online submissions for Palindrome Linked List.
Memory Usage: 12.9 MB, less than 39.66% of C++ online submissions for Palindrome Linked List.
*/