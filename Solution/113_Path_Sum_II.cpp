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
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        vector<int> path;
        vector<vector<int>> paths;
        dfs(root, sum, path, paths);
        return paths; 
    }

    void dfs(TreeNode* node, int sum, vector<int>& path, vector<vector<int>>& paths){
        if (!node){
            return;
        }
        path.push_back(node->val);
        if (!(node->left) && !(node->right) && sum == node->val){
            paths.push_back(path);
        }
        dfs(node->left, sum - node->val, path, paths);
        dfs(node->right, sum - node->val, path, paths);
        path.pop_back();
    }
};

/*
Runtime: 12 ms, faster than 86.01% of C++ online submissions for Path Sum II.
Memory Usage: 19.8 MB, less than 92.11% of C++ online submissions for Path Sum II.
*/