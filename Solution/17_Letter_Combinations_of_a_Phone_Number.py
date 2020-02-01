class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], \
        '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], \
        '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']
        }

        def directProduct(list1, list2):
            ret = []
            for i in list1:
                for j in list2:
                    ret.append(i+j)
            return ret
        
        if len(digits) == 0:
            return []
        ret = d[digits[0]]
        for digit in digits[1:]:
            ret = directProduct(ret, d[digit])
        return ret


'''
Runtime: 20 ms, faster than 99.99% of Python3 online submissions for Letter Combinations of a Phone Number.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Letter Combinations of a Phone Number.
'''