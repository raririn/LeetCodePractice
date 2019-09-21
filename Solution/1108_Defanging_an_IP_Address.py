class Solution:
    def defangIPaddr(self, address: str) -> str:
        import re
        return re.sub('\.', '[.]', address)


'''
Runtime: 36 ms, faster than 64.46% of Python3 online submissions for Defanging an IP Address.
Memory Usage: 13.5 MB, less than 100.00% of Python3 online submissions for Defanging an IP Address.
'''