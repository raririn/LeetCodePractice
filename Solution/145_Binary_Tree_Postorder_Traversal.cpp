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
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> ret;
        stack<TreeNode*> stack;
        stack.push(root);
        if (!root){
            return ret;
        }
        while (!stack.empty()){
            /* This is a reverse version of node->right->left ! */
            TreeNode* cur = stack.top();
            ret.insert(ret.begin(), cur->val);
            stack.pop();
            if (cur->left){
                stack.push(cur->left);
            }
            if (cur->right){
                stack.push(cur->right);
            }

        }
        return ret;
    }        
};