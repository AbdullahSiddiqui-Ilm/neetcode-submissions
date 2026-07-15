class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count1 = {}
        char_count2 = {}

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

        if char_count1 == char_count2:
            return True
        else: return False