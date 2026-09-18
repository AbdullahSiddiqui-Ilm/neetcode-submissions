class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        
        for i in range(len(strs)):
            key = ''.join(sorted(strs[i]))
            if key not in hashmap:
                hashmap[key] = [strs[i]]
            else:
                hashmap[key].append(strs[i])
        group = list(hashmap.values())
        return group

""" 
Pattern: Canonical Key + HashMap

When different inputs are considered equivalent, find a canonical representation (key) that is identical for all equivalent inputs, then use a HashMap to group them.

Example: Anagrams → same character composition → sorted string/frequency count becomes the key → HashMap<key, [group]>.
"""