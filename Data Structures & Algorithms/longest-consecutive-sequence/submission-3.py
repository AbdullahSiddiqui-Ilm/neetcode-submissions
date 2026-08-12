class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        sorted_nums = sorted(nums)
        count = 1
        longest_count = 1
        for i in range(1, len(nums)):
            if sorted_nums[i] -1  == sorted_nums[i - 1]:
                count += 1
                if count > longest_count:
                    longest_count = count
            elif sorted_nums[i] == sorted_nums[i-1]:
                continue
            else:
                count = 1
                continue
        
        return longest_count 
            

        