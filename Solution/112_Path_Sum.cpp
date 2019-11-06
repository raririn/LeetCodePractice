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
    bool hasPathSum(TreeNode* root, int sum) {
        if (!root){
            return false;
        }
        if (sum == root->val){
            if ((!root->left) && (!root->right)){
                return true;
            }
        }
        bool flag = false;
        if (root->left){
            flag = flag || hasPathSum(root->left, sum - root->val);
        }
        if (root->right){
            flag = flag || hasPathSum(root->right, sum - root->val);
        }
        return flag;
    }
};


/*
Runtime: 16 ms, faster than 40.97% of C++ online submissions for Path Sum.
Memory Usage: 19.9 MB, less than 75.00% of C++ online submissions for Path Sum.
*/