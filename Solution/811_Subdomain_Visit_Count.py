class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = {}
        for i in cpdomains:
            sp = i.split(" ")
            num = int(sp[0])
            domainsplit = sp[1].split(".")
            # ["discuss", "leetcode", "com"]
            for i in range(len(domainsplit)-1, -1, -1):
                d[".".join(domainsplit[i:])] = d.get(".".join(domainsplit[i:]), 0) + num
        return [str(v) + " " + str(k) for k, v in d.items()]


'''
Runtime: 64 ms, faster than 64.52% of Python3 online submissions for Subdomain Visit Count.
Memory Usage: 13.8 MB, less than 8.33% of Python3 online submissions for Subdomain Visit Count.
'''