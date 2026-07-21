class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1

    
        sorted_squares = []
        for i in range(len(nums)):
            if nums[left]**2 > nums[right]**2:
                sorted_squares.append(nums[left]**2)
                left += 1
            else:
                sorted_squares.append(nums[right]**2)
                right -= 1
        sorted_squares.reverse()
        return sorted_squares

        