class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1

        sorted_squares = [0] * len(nums)
        indexer = len(sorted_squares) - 1
    
        for i in range(len(sorted_squares)):
            if nums[left]**2 > nums[right]**2:
                sorted_squares[indexer] = nums[left] ** 2
                left += 1
                indexer -= 1
            else:
                sorted_squares[indexer] = nums[right] ** 2
                right -= 1
                indexer -= 1
        return sorted_squares

        