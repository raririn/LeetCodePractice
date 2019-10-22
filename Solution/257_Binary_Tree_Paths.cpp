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
    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> ret;
        if (!root){
            return ret;
        }
        helper(root, to_string(root->val), ret);
        return ret;
    }

    void helper(TreeNode* node, string s, vector<string>& ret){
        if (!node->left && !node->right){
            ret.push_back(s);
            return;
        }
        if (node->left){
            helper(node->left, s + "->" + to_string(node->left->val), ret);
        }
        if (node->right){
            helper(node->right, s + "->" + to_string(node->right->val), ret);
        }
    }
};

/*
Runtime: 0 ms, faster than 100.00% of C++ online submissions for Binary Tree Paths.
Memory Usage: 11.7 MB, less than 73.68% of C++ online submissions for Binary Tree Paths.
*/