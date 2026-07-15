class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_count1, char_count2= {}, {}

        for letter in s:
            if letter in char_count1:
                char_count1[letter] += 1
            else:
                char_count1[letter] = 1

        for letter in t:
            if letter in char_count2:
                char_count2[letter] += 1
            else:
                char_count2[letter] = 1

        return char_count1 == char_count2
            

        """countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + count.get(s[i], 0)
            countT[t[i]] = 1 + count.get(t[i], 0)
        for c in countS:
            if countS[c] != countT[c]:
                return False"""