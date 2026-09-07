class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split()
        res = len(arr[-1])
        return res
        