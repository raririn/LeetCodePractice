# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        ret = []
        def addToList(root):
            if root:
                addToList(root.left)
                ret.append(root.val)
                addToList(root.right)
        
        addToList(root1)
        addToList(root2)
        # You can write a mergesort yourself, but I don't see it necessary.
        return sorted(ret)

'''
Runtime: 340 ms, faster than 96.49% of Python3 online submissions for All Elements in Two Binary Search Trees.
Memory Usage: 21.5 MB, less than 38.11% of Python3 online submissions for All Elements in Two Binary Search Trees.
'''