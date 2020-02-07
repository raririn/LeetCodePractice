class Solution:
    def validIPAddress(self, IP: str) -> str:
        def validIpv4(IP: str) -> str:
            if ".." in IP or "-" in IP:
                return "Neither"
            IP = IP.split('.')
            if len(IP) != 4:
                return "Neither"
            for i in IP:
                if len(i) == 0 or len(i) > 3:
                    return "Neither"
                if i[0] == "0" and len(i) > 1:
                    return "Neither"
                try:
                    j = int(i)
                    if j < 0 or j >= 256:
                        return "Neither"
                except:
                    return "Neither"
            return "IPv4"
        
        def validIpv6(IP: str) -> str:
            if "::" in IP or "-" in IP:
                return "Neither"
            IP = IP.split(':')
            if len(IP) != 8:
                return "Neither"
            for i in IP:
                if len(i) == 0 or len(i) > 4:
                    return "Neither"
                try:
                    j = int(i, 16)
                    if j < 0 or j >= 65536:
                        return "Neither"
                except:
                    return "Neither"
            return "IPv6"            

        
        if "." in IP:
            return validIpv4(IP)
        else:
            return validIpv6(IP)

'''
Runtime: 28 ms, faster than 61.98% of Python3 online submissions for Validate IP Address.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Validate IP Address.
'''