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

        
        