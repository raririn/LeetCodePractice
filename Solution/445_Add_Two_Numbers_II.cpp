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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int c1 = 0;
        int c2 = 0;
        ListNode* cur = l1;
        while (cur){
            cur = cur->next;
            c1++;
        }
        cur = l2;
        while (cur){
            cur = cur->next;
            c2++;
        }

        if (c1 > c2){
            cur = helper(l1, l2, c1, c2);
        }
        else if (c1 == c2){
            cur = add(l1, l2);
        }
        else{
            cur = helper(l2, l1, c2, c1);
        }
        
        
        bool flag = true;
        while (flag){
            flag = false;
            if (cur->val >= 10){
                ListNode* a = new ListNode(1);
                a->next = cur;
                cur->val -= 10;
                cur = a;
            }
            ListNode* tmp1 = cur;
            ListNode* tmp2 = cur;
            while (tmp1->next){
                tmp1 = tmp1->next;
                if (tmp1->val >= 10){
                    tmp1->val -= 10;
                    tmp2->val += 1;
                    if (tmp2->val >= 10){
                        flag = true;
                    }
                }
                tmp2 = tmp1;
            }
        }
        return cur;
    }

    ListNode* helper(ListNode* l1, ListNode* l2, int c1, int c2){
        ListNode* tmp = l1;
        for (int i = 1; i < c1 - c2; i++){
            l1 = l1->next;
        }
        l1->next = add(l1->next, l2);
        return tmp;
    }

    ListNode* add(ListNode* l1, ListNode* l2){
        ListNode* tmp = l1;
        while (l1){
            l1->val += l2->val;
            l1 = l1->next;
            l2 = l2->next;
        }
        return tmp;
    }
};

/*
Runtime: 20 ms, faster than 91.41% of C++ online submissions for Add Two Numbers II.
Memory Usage: 9.7 MB, less than 100.00% of C++ online submissions for Add Two Numbers II.
*/