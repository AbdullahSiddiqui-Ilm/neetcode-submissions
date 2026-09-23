class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        max_left_array = []
        max_right_array= []
        min_val_arr = []
        max_left = max_right = 0

        for i in height:
            if i > max_left:
                max_left_array.append(max_left)
                max_left = i
            else:
                max_left_array.append(max_left)
        
        for i in range(len(height) - 1, - 1, -1):
            if height[i] > max_right:
                max_right_array.append(max_right)
                max_right = height[i]
            else:
                max_right_array.append(max_right)
        max_right_array.reverse()
        
        for i in range(len(height)):
            min_val = min(max_left_array[i], max_right_array[i])
            min_val_arr.append(min_val)

        for i in range(len(height)):
            water_height = min_val_arr[i] - height[i]
            if water_height <= 0:
                continue
            else:
                total += water_height
        return total

"""
Pattern:

- When looking at the question, we understand that the amount of trapped
water is determined by the space between the bars. we need a way to determine 
the max of both sides for each bar which will determine how many blocks we can fit 
in this position.
- We use two arrays, to determine the max on the left and the max on the right 
for each index. we also need max variables to hold the current max_left
/max_right. This is as we have to check is the current index/block greater
than the max. If so, we append the current max_left/right and then update the 
variable after appending to be the new max.
- we have to iterate through height twice. once from the beginning from the left,
and once from the end for the max_right_array.
- we then iterate through height again, but this time this is to take the
minimum height from both the max_left_array and the max_right_array. We need the
minimum as thats the maximum amount of water we can have in this space. 
- Now finally, we calculate the amount of water at each index. This is done by
taking the min_value from the 3rd array, and sutracting the height of the current
index/block. This is straightforward to understand. We then add the result to
the total, and return total. edge case: if current water value is less or equal to
0, then comtinue, as no water can be stored here

"""

