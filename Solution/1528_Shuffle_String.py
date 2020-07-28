class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        rep = [''] * len(s)
        for idx, i in enumerate(indices):
            rep[i] = s[idx]
        return ''.join(rep)