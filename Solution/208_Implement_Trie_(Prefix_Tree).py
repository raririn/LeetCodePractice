class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.trie
        for char in word:
            if char not in cur:
                cur[char] = {}
            cur = cur[char]
        cur['!'] = 1
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.trie
        for char in word:
            if char not in cur:
                return False
            cur = cur[char]
        return '!' in cur
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.trie
        for char in prefix:
            if char not in cur:
                return False
            cur = cur[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


'''
Runtime: 144 ms, faster than 88.94% of Python3 online submissions for Implement Trie (Prefix Tree).
Memory Usage: 27.2 MB, less than 66.67% of Python3 online submissions for Implement Trie (Prefix Tree).
'''