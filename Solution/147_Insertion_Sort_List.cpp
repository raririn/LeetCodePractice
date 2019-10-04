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
    ListNode* insertionSortList(ListNode* head) {
        if (!head){
            return nullptr;
        }
        if (!head->next){
            return head;
        }
        ListNode* cur = head->next;
        ListNode* tmp;
        ListNode* tra;
        head->next = nullptr;
        while (cur){
            tmp = cur->next;
            if (!tmp){
            }
            if (cur->val <= head->val){
                cur->next = head;
                head = cur;
            }
            else{
                tra = head;
                if (!head->next){
                    std::cout << "b1" << std::endl;
                    head->next = cur;
                    cur->next = nullptr;
                }
                else{
                    std::cout << "b2" << std::endl;
                     while (tra->next){
                        if ((cur->val > tra->val) && (cur->val <= (tra->next)->val)){
                            insertAfter(cur, tra);
                            break;
                        }
                        tra = tra->next;
                    }
                    if (!tra->next){
                        tra->next = cur;
                        cur->next = nullptr;
                    }
                }
            }
            cur = tmp;
        }
        tra = head;
        return head;
    }

    void insertAfter(ListNode* cur, ListNode* node) {
        ListNode* tmp;
        tmp = node->next;
        node->next = cur;
        cur->next = tmp;
    }
};

/*
Runtime: 60 ms, faster than 13.17% of C++ online submissions for Insertion Sort List.
Memory Usage: 9.5 MB, less than 88.89% of C++ online submissions for Insertion Sort List.
*/