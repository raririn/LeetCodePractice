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
    int findBottomLeftValue(TreeNode* root) {
        if (!root){
            return 0;
        }
        int m = 0;
        int val = root->val;
        helper(root, m, val, 0);
        return val;
    }

    void helper(TreeNode* root, int& maxDepth, int& val, int depth){
        if (!root){
            return;
        }
        helper(root->left, maxDepth, val, depth + 1);
        helper(root->right, maxDepth, val, depth + 1);

        if (depth > maxDepth){
            maxDepth = depth;
            val = root->val;
        }
    }
};

/*
Runtime: 16 ms, faster than 63.14% of C++ online submissions for Find Bottom Left Tree Value.
Memory Usage: 20.5 MB, less than 100.00% of C++ online submissions for Find Bottom Left Tree Value.
*/