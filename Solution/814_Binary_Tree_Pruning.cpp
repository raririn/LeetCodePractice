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
    TreeNode* pruneTree(TreeNode* root) {
        if (!root){
            return nullptr;
        }
        
        if ((root->left) && !(containOne(root->left))){
            root->left = nullptr;
        }
        if ((root->right) && !(containOne(root->right))){
            root->right = nullptr;
        }
        pruneTree(root->left);
        pruneTree(root->right);
        return root;
    }

    bool containOne(TreeNode* root) {
        bool flag = root->val ? true : false;
    
        if (root->left){
            flag = flag & containOne(root->left);
        }
        if (root->right){
            flag = flag & containOne(root->right);
        }
        return flag;
    }
};


/*
Runtime: 0 ms, faster than 100.00% of C++ online submissions for Binary Tree Pruning.
Memory Usage: 9.8 MB, less than 78.57% of C++ online submissions for Binary Tree Pruning.
*/