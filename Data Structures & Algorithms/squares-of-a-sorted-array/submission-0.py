class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1

        squares =[]
        for val in nums:
            squares.append(val ** 2)


        sorted_squares = []
        for i in range(len(squares)):
            if squares[left] > squares[right]:
                sorted_squares.append(squares[left])
                left += 1
            else:
                sorted_squares.append(squares[right])
                right -= 1
        sorted_squares.reverse()
        return sorted_squares

        