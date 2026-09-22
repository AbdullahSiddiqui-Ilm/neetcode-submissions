class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # 1. while i < j: calculate area, by choosing min height, and 
        #    multiplying by width
        # 2. update max area
        # 3. check which height is smaller, and move that one 
        # 4. return max area
        i = 0
        j = len(heights) - 1
        max_area = 0
        while i < j:
            area = min(heights[i], heights[j]) * (j - i)
            if area > max_area:
                max_area = area
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1
        return max_area
    
            
            

