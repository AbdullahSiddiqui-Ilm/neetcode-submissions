class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_hash = {}
        l = 0

        for char in s1:
            s1_hash[char] = s1_hash.get(char, 0) + 1
        
        for r in range(len(s1) - 1, len(s2)):
            s2_hash = {}
            for char in range(l, r + 1):
                s2_hash[s2[char]] = s2_hash.get(s2[char], 0) + 1
            if s1_hash == s2_hash:
                return True
            else:
                l += 1
        return False

        

