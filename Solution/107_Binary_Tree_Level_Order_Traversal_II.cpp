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
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        vector<vector<int>> ret;
        if (!root){
            return ret;
        }
        queue<TreeNode*> q;
        q.push(root);
        while (!q.empty()){
            vector<int> cur;
            int size = q.size();
            for (int i = 0; i < size; i++){
                TreeNode* tmp = q.front();
                q.pop();
                cur.push_back(tmp->val);
                if (tmp->left){
                    q.push(tmp->left);
                }
                if (tmp->right){
                    q.push(tmp->right);
                }
            }
            ret.insert(ret.begin(), cur);
        }
        return ret;
    }        
};

/*
Runtime: 12 ms, faster than 21.96% of C++ online submissions for Binary Tree Level Order Traversal II.
Memory Usage: 13.8 MB, less than 86.49% of C++ online submissions for Binary Tree Level Order Traversal II.
*/