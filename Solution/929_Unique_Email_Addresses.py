class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        import re
        emails = [i.split('@') for i in emails]
        emails = set([(re.sub('\+.*', '', re.sub('\.', '', i[0])) + '@' + i[1]) for i in emails])
        return len(emails)

'''
Runtime: 68 ms, faster than 29.23% of Python3 online submissions for Unique Email Addresses.
Memory Usage: 13.6 MB, less than 6.25% of Python3 online submissions for Unique Email Addresses.
'''