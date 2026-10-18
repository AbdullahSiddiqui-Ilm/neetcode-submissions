class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            wanted = target - nums[i]
            if wanted in hashmap:
                return [hashmap[wanted], i]
            hashmap[nums[i]] = i
            
        