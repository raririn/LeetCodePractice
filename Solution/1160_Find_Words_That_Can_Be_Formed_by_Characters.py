class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ret = 0
        for word in words:
            tempchar  = [char for char in chars]
            flag = 1
            for i in word:
                if i in tempchar:
                    tempchar.remove(i)
                else:
                    flag = 0
                    break
            if flag:
                ret = ret + len(word)
        return ret

'''
Runtime: 204 ms, faster than 58.39% of Python3 online submissions for Find Words That Can Be Formed by Characters.
Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Find Words That Can Be Formed by Characters.
'''