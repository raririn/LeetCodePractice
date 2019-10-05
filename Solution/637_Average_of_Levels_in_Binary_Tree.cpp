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
    vector<double> averageOfLevels(TreeNode* root) {
        vector<double> ret;
        queue<TreeNode*> q;
        q.push(root);
        while(!q.empty()){
            double tmp = 0;
            int size = q.size();
            for (int i = 0; i < s; i++){
                TreeNode* t = q.front();
                q.pop();
                if (t->left){
                    q.push(t->left);
                }
                if (t->right){
                    q.push(t->right);
                }
                tmp = tmp + t->val;
            }
            ret.push_back(tmp/s);
        }
        return ret;
    }
};


/*
Runtime: 20 ms, faster than 69.66% of C++ online submissions for Average of Levels in Binary Tree.
Memory Usage: 21.7 MB, less than 88.89% of C++ online submissions for Average of Levels in Binary Tree.
*/