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
    TreeNode* ret = nullptr;
    TreeNode* getTargetCopy(TreeNode* original, TreeNode* cloned, TreeNode* target) {
        if (!original || !cloned) {
            return nullptr;
        }
        if (original->val == target->val) {
            ret = cloned;
        }
        else {
            getTargetCopy(original->left, cloned->left, target);
            getTargetCopy(original->right, cloned->right, target);            
        }

        return ret;
    }
};

/*
Runtime: 1036 ms, faster than 33.86% of C++ online submissions for Find a Corresponding Node of a Binary Tree in a Clone of That Tree.
Memory Usage: 164.5 MB, less than 34.21% of C++ online submissions for Find a Corresponding Node of a Binary Tree in a Clone of That Tree.
*/