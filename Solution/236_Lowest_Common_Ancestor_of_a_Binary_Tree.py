# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root == p or root == q:
            return root
        
        left_subtree_LCA = self.lowestCommonAncestor(root.left, p, q)
        right_subtree_LCA = self.lowestCommonAncestor(root.right, p, q)

        # If both are non-null, it means root is a CA
        if left_subtree_LCA and right_subtree_LCA:
            return root
        # If one is null and the other isn't, it means p OR Q is in this subtree, so passing the value upwards
        return left_subtree_LCA or right_subtree_LCA # One of them is null, or both are null
            