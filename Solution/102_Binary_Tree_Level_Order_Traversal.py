# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [(0, 0, root)]
        ret = []
        count = 1
        while queue:
            depth, _, cur = heapq.heappop(queue)
            if cur.left:
                count += 1
                heapq.heappush(queue, (depth+1, count, cur.left))
            if cur.right:
                count += 1
                heapq.heappush(queue, (depth+1, count, cur.right))
            if len(ret) <= depth:
                ret.append([])
            ret[depth].append(cur.val)
        return ret


'''
Runtime: 48 ms, faster than 33.99% of Python3 online submissions for Binary Tree Level Order Traversal.
Memory Usage: 14 MB, less than 78.81% of Python3 online submissions for Binary Tree Level Order Traversal.
'''