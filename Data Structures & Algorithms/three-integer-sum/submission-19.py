class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

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
                    if [nums[i], nums[l], nums[r]] in result:
                        l += 1
                        r -= 1
                    else:
                        result.append([nums[i], nums[l], nums[r]])
                        l += 1
                        r -= 1
        return result



"""
- Sort nums using .sort()
- Two pointers. Use two pointer aswell as loop i value to determine whether 
  the current three values add to 0.
- Make sure when adding to result array that the triplets are always added in the same order,
  and that they are checked in the same order aswell, while checking duplicates. 
- the desired result is space complexity of n^2, meaning for each loop, there will be
  another loop checking whether the current answer adds to 0, and if it does, a 2nd check to
  confirm whether this triplet already exists.
- Each triplet that succeeds all checks will be appended to the list as a list. The numbers will be appended, not the indicies
"""

