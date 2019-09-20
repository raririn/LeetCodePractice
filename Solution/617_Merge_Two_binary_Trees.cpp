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
    TreeNode* mergeTrees(TreeNode* t1, TreeNode* t2) {
        if (!t1){
            return t2;
        }
        if (!t2){
            return t1;
        }
        TreeNode *t3 = new TreeNode(t1->val + t2->val);
        TreeNode *ret = t3;
        if (t1->right && t2->right){
            t3->right = mergeTrees(t1->right, t2->right);
        }
        else if (t1->right || t2->right){
            t3->right = (t1->right)? t1->right : t2->right;
        }
 
        if (t1->left && t2->left){
            t3->left = mergeTrees(t1->left, t2->left);
        }
        else if (t1->left || t2->left){
            t3->left = (t1->left)? t1->left : t2->left;
        }        
        return ret;

    }
};

/*
Runtime: 44 ms, faster than 23.95% of C++ online submissions for Merge Two Binary Trees.
Memory Usage: 18.9 MB, less than 33.33% of C++ online submissions for Merge Two Binary Trees.
*/