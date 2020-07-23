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
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        if (!root) {
            return new TreeNode(val);
        }
        if (root->val > val) {
            if (root->left) {
                insertIntoBST(root->left, val);
            }
            else {
                root->left = new TreeNode(val);
            }
        }
        else {
            if (root->right) {
                insertIntoBST(root->right, val);
            }
            else {
                root->right = new TreeNode(val);
            }
        }
        return root;
    }
};

/*
Runtime: 100 ms, faster than 48.23% of C++ online submissions for Insert into a Binary Search Tree.
Memory Usage: 38.4 MB, less than 84.47% of C++ online submissions for Insert into a Binary Search Tree.
*/