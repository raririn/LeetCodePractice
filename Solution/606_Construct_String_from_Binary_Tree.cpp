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
    string tree2str(TreeNode* t) {
        string ret = "";
        preorder(t, ret);
        return ret;
    }

    void preorder(TreeNode* node, string& ret){
        if (node){
            ret += to_string(node->val);
            if ((!node->left) && node->right){
                ret += "()";
            }
            if (node->left){
                ret += "(";
                preorder(node->left, ret);
                ret += ")";
            }
            if (node->right){
                ret += "(";
                preorder(node->right, ret);
                ret += ")";
            }                  
        }
    }
};

/*
Runtime: 16 ms, faster than 93.01% of C++ online submissions for Construct String from Binary Tree.
Memory Usage: 20.8 MB, less than 100.00% of C++ online submissions for Construct String from Binary Tree.
*/