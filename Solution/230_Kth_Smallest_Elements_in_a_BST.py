# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def helper_inorder(root):
            if not root:
                return []
            return helper_inorder(root.left) + [root.val] + helper_inorder(root.right)
        sortedTree = helper_inorder(root)
        return sortedTree[k-1]