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
    bool isSymmetric(TreeNode* root) {
        if (!root){
            return true;
        }
        if ((!root->left) && (root->right)){
            return false;
        }     
        else if ((!root->right) && (root->left)){
            return false;
        }
        else if ((!root->left) &&(!root->right)){
            return true;
        }
        return isSame(root->left, root->right);
    }

    bool isSame(TreeNode* l, TreeNode* r){
        if (l->val != r->val){
            return false;
        }
        if ((!l->left) && (!l->right) && (!r->left) && (!r->right)){
            return true;
        }
        bool flag = true;
        if ((l->left) && (r->right)){
            flag = flag && isSame(l->left, r->right);
        }
        else if (!((!l->left) && (!r->right))){
            return false;
        }

        if ((r->left) && (l->right)){
            flag = flag && isSame(l->right, r->left);
        }

        else if (!((!r->left) && (!l->right))){
            return false;
        }
        return flag;
    }
};


/*
Runtime: 8 ms, faster than 47.17% of C++ online submissions for Symmetric Tree.
Memory Usage: 14.8 MB, less than 77.97% of C++ online submissions for Symmetric Tree.
*/