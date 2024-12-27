# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        cur_ptrs = [i for i in lists if i]
        head = ListNode(0, None)
        cur = head

        while cur_ptrs:
            #print(cur_ptrs, cur)
            #assert isinstance(cur_ptr, ListNode)
            assert isinstance(cur, ListNode)
            cur_maxima = min(cur_ptrs, key = lambda x: x.val)
            cur.next = ListNode(cur_maxima.val, None)
            cur = cur.next
            if cur_maxima.next:
                cur_ptrs[cur_ptrs.index(cur_maxima)] = cur_maxima.next
            else:
                cur_ptrs.remove(cur_maxima)

        return head.next
        
        