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
    int rangeSumBST(TreeNode* root, int L, int R) {
        int sum = 0;

        if ((root->val >= L) && (root->val <= R)){
            sum = sum + root->val;
        }
        if (root->left){
            sum = sum + rangeSumBST(root->left, L, R);
        }
        if (root->right){
            sum = sum + rangeSumBST(root->right, L, R);
        }
        return sum;
    }
};

/*
Runtime: 152 ms, faster than 51.15% of C++ online submissions for Range Sum of BST.
Memory Usage: 40.9 MB, less than 100.00% of C++ online submissions for Range Sum of BST.
*/