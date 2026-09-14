class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashtable = {}
        for i in range(len(nums)):
            hashtable[nums[i]] = hashtable.get(nums[i], 0) + 1
            if hashtable[nums[i]] > 1:
                return nums[i]