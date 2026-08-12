class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        hashset = set(nums)
        longest_count = 1

        for n in hashset:
            if n - 1 not in hashset:
                count = 1
                while n + 1 in hashset:
                    if n in hashset:
                        count += 1
                        n += 1
                        if count > longest_count:
                            longest_count = count
        return longest_count
            

        