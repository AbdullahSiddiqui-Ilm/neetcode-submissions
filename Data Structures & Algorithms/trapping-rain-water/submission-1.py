class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        max_left_array = []
        max_right_array = []
        min_val = []

        max_left = 0
        max_right = 0

        for i in height:
            if i > max_left:
                max_left_array.append(max_left)
                max_left = i
            else:
                max_left_array.append(max_left)

        for i in range(len(height) -1, -1, -1):
            if height[i] > max_right:
                max_right_array.append(max_right)
                max_right = height[i]
            else:
                max_right_array.append(max_right)
        max_right_array.reverse()

        for i in range(len(height)):
            min_val.append(min(max_left_array[i], max_right_array[i]))

        for i in range(len(height)):
            height_val = min_val[i] - height[i]
            if height_val <= 0:
                continue
            else:
                total += height_val
        return total