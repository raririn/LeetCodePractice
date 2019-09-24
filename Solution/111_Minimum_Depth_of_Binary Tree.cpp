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
    int minDepth(TreeNode* root) {
        if (!root){
            return 0;
        }
        if (!root->left){
            return 1 + minDepth(root->right);
        }
        if (!root->right){
            return 1 + minDepth(root->left);
        }
        return 1 + min(minDepth(root ->left), minDepth(root->right));         
    }
};

/*
Runtime: 16 ms, faster than 41.07% of C++ online submissions for Minimum Depth of Binary Tree.
Memory Usage: 20 MB, less than 59.52% of C++ online submissions for Minimum Depth of Binary Tree.
*/