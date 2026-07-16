class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for i in range(len(strs)):
            key = ''.join(sorted(strs[i]))
            if key not in hashmap:
                hashmap[key] = [strs[i]]
            else:
                hashmap[key].append(strs[i])
        groups = list(hashmap.values())
        return groups
            

            





            

        