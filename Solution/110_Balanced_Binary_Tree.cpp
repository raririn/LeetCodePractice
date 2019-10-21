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
    bool isBalanced(TreeNode* root) {
        int height = 0;
        return helper(root, height);
    }
    bool helper(TreeNode* root, int& height){
        if (!root){
            height = -1;
            return true;
        }
        int left_h, right_h;
        if (helper(root->left, left_h) && helper(root->right, right_h) && abs(left_h-right_h) < 2){
            height = max(left_h, right_h) + 1;
            return true;
        }
        return false;
    }
};

/*
Runtime: 12 ms, faster than 84.33% of C++ online submissions for Balanced Binary Tree.
Memory Usage: 17.5 MB, less than 54.24% of C++ online submissions for Balanced Binary Tree.
*/