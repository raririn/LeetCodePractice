class Solution:
    def entityParser(self, text: str) -> str:
        d = {
            "&quot;": "\"",
            "&apos;": "\'",
            "&gt;": ">",
            "&lt;": "<",
            "&frasl;": "/",
        }

        for k, v in d.items():
            text = text.replace(k, v)
        return text.replace("&amp;", "&")

'''
Runtime: 60 ms, faster than 80.12% of Python3 online submissions for HTML Entity Parser.
Memory Usage: 14.5 MB, less than 48.00% of Python3 online submissions for HTML Entity Parser.
'''