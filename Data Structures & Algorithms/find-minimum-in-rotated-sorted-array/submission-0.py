class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (r + l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid
        return nums[r]




#if nums[mid] > nums[right]:
    # minimum is strictly to the right
#else:
    # minimum is at mid or to the left
