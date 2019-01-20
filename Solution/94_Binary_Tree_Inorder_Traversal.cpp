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
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> ret;
        stack<TreeNode*> stack;
        stack.push(root);
        if (!root){
            return ret;
        }
        while (!stack.empty()){
            TreeNode* cur = stack.top();
            if (cur->left){
                stack.push(cur->left);
                cur->left = NULL;
            }
            else{
                ret.push_back(cur->val);
                stack.pop();
                if (cur->right){
                    stack.push(cur->right);
                }
            }
        }
        return ret;
    }
};