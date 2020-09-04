/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
private:
    int maxDepth;
    int sum;

public:
    int deepestLeavesSum(TreeNode* root) {
        traverse(root, 0);
        return this->sum;
    }
    
    void traverse(TreeNode* cur, int curDepth) {
        if (this->maxDepth < curDepth) {
            this->maxDepth = curDepth;
            this->sum = cur->val;
        }
        else if (this->maxDepth == curDepth) {
            this->sum += cur->val;
        }

        if (cur->left) {
            traverse(cur->left, curDepth+1);
        }
        if (cur->right) {
            traverse(cur->right, curDepth+1);
        }

        return;
    }
};

/*
Runtime: 60 ms, faster than 86.46% of C++ online submissions for Deepest Leaves Sum.
Memory Usage: 38.3 MB, less than 70.09% of C++ online submissions for Deepest Leaves Sum.
*/