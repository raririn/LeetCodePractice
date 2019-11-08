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
    bool findTarget(TreeNode* root, int k) {
        unordered_set<int> d;
        return traverse(root, k, d);
    }

    bool traverse(TreeNode* root, int k, unordered_set<int>& d){
        if (!root){
            return false;
        }
        if (d.count(k - root->val)){
            return true;
        }
        d.insert(root->val);
        return traverse(root->left, k, d) || traverse(root->right, k, d);
    }
};


/*
Runtime: 48 ms, faster than 34.33% of C++ online submissions for Two Sum IV - Input is a BST.
Memory Usage: 26 MB, less than 40.00% of C++ online submissions for Two Sum IV - Input is a BST.
*/