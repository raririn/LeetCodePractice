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
    bool isUnivalTree(TreeNode* root) {
        if (!root){
            return true;
        }
        int val = root->val;
        return isEqualVal(root->left, val) && isEqualVal(root->right, val);
    }
    bool isEqualVal(TreeNode* node, int val){
        if (!node){
            return true;
        }
        if (!(node->val == val)){
            return false;
        }
        else{
            return isEqualVal(node->left, val) && isEqualVal(node->right, val);
        }
    }
};

/*
Runtime: 4 ms, faster than 67.00% of C++ online submissions for Univalued Binary Tree.
Memory Usage: 10.5 MB, less than 100.00% of C++ online submissions for Univalued Binary Tree.
*/