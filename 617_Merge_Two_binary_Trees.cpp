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
        TreeNode T3 = TreeNode(0);
        TreeNode *t3 = &T3;
        (*t3).val = (*t1).val + (*t2).val;
        // Right case
        if (t1->right && t2->right){  /* If there are both children, merge them */
            t3->right = mergeTrees(t1->right, t2->right);
        }
        if (t1->right&& !(t2->right)){  /* If there is a single child, copy it */
            cout<<"right added"<<endl;
            t3->right = t1->right;
        }
        if ((!t1->right)&& t2->right){  /* If there is a single child, copy it */
            cout<<"right added"<<endl;
            t3->right = t2->right;
        } 
        
        // Left case
        if (t1->left&& t2->left){  /* If there are both children, merge them */
            t3->left = mergeTrees(t1->left, t2->left);
        }
        if (t1->left&& !t2->left){  /* If there is a single child, copy it */
            t3->left = t1->left;
        }
        if (!t1->left&& t2->left){  /* If there is a single child, copy it */
            t3->left = t2->left;
        }        
       
        return t3;
    }
};