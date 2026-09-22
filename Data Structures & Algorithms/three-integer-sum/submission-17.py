class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i >= 1 and nums[i - 1] == nums[i]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                summ = nums[i] + nums[l] + nums[r]
                if summ < 0:
                    l += 1
                elif summ > 0:
                    r -= 1
                else:
                    if [nums[i], nums[l], nums[r]] in res:
                        l += 1
                        r -= 1
                        continue
                    else:
                        res.append([nums[i], nums[l], nums[r]])
                        l += 1
                        r -= 1

            
        return res

