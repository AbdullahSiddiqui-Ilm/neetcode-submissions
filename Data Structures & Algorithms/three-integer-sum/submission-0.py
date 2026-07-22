class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        array = []
        nums.sort()


        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0 and [nums[i], nums[left], nums[right]] not in array:
                    array.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1
        return array
            

            
        