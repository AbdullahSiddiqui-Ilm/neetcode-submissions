class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1

    
        sorted_squares = []
        for i in range(len(nums)):
            if nums[left]**2 > nums[right]**2:
                sorted_squares.insert(0, nums[left]**2)
                left += 1
            else:
                sorted_squares.insert(0, nums[right]**2)
                right -= 1
        return sorted_squares

        