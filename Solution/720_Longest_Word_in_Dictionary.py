class Solution:
    def longestWord(self, words: List[str]) -> str:
        words = sorted(words, key = len)
        trie = {}
        maxlen = 0
        ret = []
        for word in words:
            flag = True
            if len(word) == 1:
                trie[word[0]] = {}
                ret.append(word)
            else:
                cur = trie
                for char in word[:-1]:
                    if char in cur:
                        cur = cur[char]
                    # If the word is not in trie, break
                    else:
                        flag = False
                        break
                if flag:
                    cur[word[-1]] = {}
                    if len(word) > maxlen:
                        maxlen = len(word)
                        ret = [word]
                    elif len(word) == maxlen:
                        ret.append(word)
        return sorted(ret)[0]

'''
Runtime: 112 ms, faster than 53.16% of Python3 online submissions for Longest Word in Dictionary.
Memory Usage: 14.1 MB, less than 50.00% of Python3 online submissions for Longest Word in Dictionary.
'''