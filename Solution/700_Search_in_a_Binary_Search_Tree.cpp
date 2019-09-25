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
    TreeNode* searchBST(TreeNode* root, int val) {
        if (!root){
            return nullptr;
        }
        if (root->val == val){
            return root;
        }
        if (root->val > val){
            return searchBST(root->left, val);
        }
        else{
            return searchBST(root->right, val);
        }
    }
};



/*
Runtime: 64 ms, faster than 13.77% of C++ online submissions for Search in a Binary Search Tree.
Memory Usage: 28.8 MB, less than 100.00% of C++ online submissions for Search in a Binary Search Tree.
*/