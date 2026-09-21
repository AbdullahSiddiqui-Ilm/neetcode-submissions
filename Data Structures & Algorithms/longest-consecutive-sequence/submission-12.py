class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        hashset_nums = set(nums)
        longest_count = 1

        for n in hashset_nums:
            if n - 1 not in hashset_nums:
                count = 1
                while n + 1 in hashset_nums:
                    count += 1
                    n += 1
                if count > longest_count:
                    longest_count = count
        return longest_count

"""
return 0 if nums doesnt exists
- make a hashset of nums as we dont need duplicates
- make longest_count = 1 as we have at least 1 value in nums
- loop through hashset, if n - 1 doestn exist, set count to 1 as its start of sequence
- while n + 1 in hashet, increase the count and also move n forward by one, as we have a valid sequence
- check the current count against the longest count, if current is longer, set longest_count to count
- return longest count
"""
            

        