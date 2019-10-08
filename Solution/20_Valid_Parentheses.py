class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in s:
            if i == "(" or i == "{" or i == "[":
                st.append(i)
            elif i == ")" or i == "}" or i == "]":
                if len(st) == 0:
                    return 0
                j = st.pop()
                if i == ")" and (not j == "("):
                    return 0
                elif i == "]" and (not j == "["):
                    return 0
                elif i == "}" and (not j == "{"):
                    return 0
        if len(st) == 0:
            return 1
        else:
            return 0

'''
Runtime: 52 ms, faster than 10.08% of Python3 online submissions for Valid Parentheses.
Memory Usage: 13.8 MB, less than 5.22% of Python3 online submissions for Valid Parentheses.
'''