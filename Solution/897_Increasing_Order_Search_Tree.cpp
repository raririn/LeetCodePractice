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
    TreeNode* increasingBST(TreeNode* root) {
        if (!root){
            return nullptr;
        }
        return rotateTree(root, nullptr);
    }
    TreeNode* rotateTree(TreeNode* root, TreeNode* next) {
        if (!root){
            return next;
        }
        TreeNode* ret = root->left? rotateTree(root->left, root) : root;
        root->left = nullptr;
        root->right = root->right? rotateTree(root->right, next) : next;
        return ret;
    }
};

/*
Runtime: 36 ms, faster than 75.69% of C++ online submissions for Increasing Order Search Tree.
Memory Usage: 14.9 MB, less than 100.00% of C++ online submissions for Increasing Order Search Tree.
*/