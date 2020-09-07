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
public:
    TreeNode* trimBST(TreeNode* root, int L, int R) {
        return trim(root, L, R);
    }

    TreeNode* trim(TreeNode* root, int L, int R) {
        if (!root) {
            return nullptr;
        }
        if (root->val > R) {
            return trim(root->left, L, R);
        }
        else if (root->val < L) {
            return trim(root->right, L, R);
        }
        else {
            root->left = trim(root->left, L, R);
            root->right = trim(root->right, L, R);
        }
        return root;
    }
};

/*
Runtime: 28 ms, faster than 61.11% of C++ online submissions for Trim a Binary Search Tree.
Memory Usage: 24.2 MB, less than 5.05% of C++ online submissions for Trim a Binary Search Tree.
*/