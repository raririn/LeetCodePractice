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
    int maxDepth(TreeNode* root) {
        if (!root){
            return 0;
        }
        return 1 + max(maxDepth(root ->left), maxDepth(root->right)); 
    }
};


/*
Runtime: 8 ms, faster than 87.08% of C++ online submissions for Maximum Depth of Binary Tree.
Memory Usage: 19.5 MB, less than 65.93% of C++ online submissions for Maximum Depth of Binary Tree.
*/