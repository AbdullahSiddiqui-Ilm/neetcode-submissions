class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_countS, char_countT= {}, {}

        for i in range(len(s)):
            char_countS[s[i]] = char_countS.get(s[i], 0) + 1
            char_countT[t[i]] = char_countT.get(t[i], 0) + 1

        return char_countS == char_countT