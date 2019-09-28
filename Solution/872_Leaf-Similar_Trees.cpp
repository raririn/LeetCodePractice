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
    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        int hash1 = 0;
        int hash2 = 0;
        getLeafHash(root1, hash1);
        getLeafHash(root2, hash2);
        return hash1 == hash2;
    }

    void getLeafHash(TreeNode* root, int& hash) {
        if (!root){
            return;
        }
        if ((!root->left) && (!root->right)){
            hash = (hash*2 + root->val) % 100;
        }
        if ((root->left) || (root->right)){
            getLeafHash(root->left, hash);
            getLeafHash(root->right, hash);            
        }

        return;
    }
};

/*
Runtime: 0 ms, faster than 100.00% of C++ online submissions for Leaf-Similar Trees.
Memory Usage: 13.1 MB, less than 88.89% of C++ online submissions for Leaf-Similar Trees.
*/