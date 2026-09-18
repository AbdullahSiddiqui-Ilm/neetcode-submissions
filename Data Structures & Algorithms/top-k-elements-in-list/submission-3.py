class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        output = []

        for val in nums:
            hashmap[val] = hashmap.get(val, 0) + 1

        sorted_hashmap = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)

        i = 0
        while k > 0:
            output.append(sorted_hashmap[i][0])
            i += 1
            k -= 1
        return output

""" 
Pattern: Frequency Counting

When a problem requires recording how frequently each value appears, use a key → value structure:

number → frequency

This naturally maps to a HashMap / HashTable.

Ask: "Do I need to keep track of how many times each value occurs?"
→ Frequency map / HashMap
"""

        
        