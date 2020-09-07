/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {

private:
    int sum = 0;

public:

    int sumEvenGrandparent(TreeNode* root) {
        wrapper(root);
        return this->sum;
    }

    void wrapper(TreeNode* root) {
        if (!root) {
            return;
        }
        if ((root->val & 1) == 0) {
            getSum(root);
        }
        wrapper(root->left);
        wrapper(root->right);
        return;
    }

    void getSum(TreeNode* cur) {
        if (cur->left) {
            if (cur->left->left) {
                this->sum += cur->left->left->val;
            }
            if (cur->left->right) {
                this->sum += cur->left->right->val;
            }
        }
        if (cur->right) {
            if (cur->right->left) {
                this->sum += cur->right->left->val;
            }
            if (cur->right->right) {
                this->sum += cur->right->right->val;
            }
        }
    }
};

/*
Runtime: 72 ms, faster than 41.04% of C++ online submissions for Sum of Nodes with Even-Valued Grandparent.
Memory Usage: 38.1 MB, less than 96.01% of C++ online submissions for Sum of Nodes with Even-Valued Grandparent.
*/