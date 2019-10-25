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
    int sumRootToLeaf(TreeNode* root) {
        int val = 0;
        return helper(root, val);
        
    }

    int helper(TreeNode* node, int val){
        if (!node){
            return 0;
        }
        val = val * 2 + node->val;
        if ((!node->left) && (!node->right)){
            return val;
        }
        return helper(node->left, val) + helper(node->right, val);
    }
};

/*
Runtime: 8 ms, faster than 65.58% of C++ online submissions for Sum of Root To Leaf Binary Numbers.
Memory Usage: 16.8 MB, less than 100.00% of C++ online submissions for Sum of Root To Leaf Binary Numbers.
*/