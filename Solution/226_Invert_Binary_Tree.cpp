/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if (!root){
            return nullptr;
        }
        if ((root->left) || (root->right)) {
            TreeNode* temp;
            temp = root->left;
            root->left = root->right;
            root->right = temp;
        }
        if (root->left){
            invertTree(root->left);
        }
        if (root->right){
            invertTree(root->right);
        }
        return root;
    }
};


/*
Runtime: 0 ms, faster than 100.00% of C++ online submissions for Invert Binary Tree.
Memory Usage: 9.4 MB, less than 30.91% of C++ online submissions for Invert Binary Tree.
*/