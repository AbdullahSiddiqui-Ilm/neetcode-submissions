class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        substring = set()

        n = len(s)

        for r in range(n):
            while s[r] in substring:
                substring.remove(s[l])
                l += 1
            substring.add(s[r])
            w = (r - l) + 1
            longest = max(w, longest)
        return longest
