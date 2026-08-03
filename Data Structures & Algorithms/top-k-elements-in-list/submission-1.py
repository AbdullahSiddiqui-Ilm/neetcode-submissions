class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        output = []

        for i in range(len(nums)):
            hashmap[nums[i]] = hashmap.get(nums[i], 0) + 1
        
        sorted_hashmap = sorted(hashmap.items(),key=lambda x: x[1] , reverse=True)

        for tup in sorted_hashmap:
            if k > 0:
                output.append(tup[0])
                k -= 1
        return output

        
        