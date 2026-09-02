class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        from math import ceil
        l, r = 1, max(piles)
        min_speed = 0
        while l <= r:
            hours = 0
            m = (r + l) // 2
            for pile in piles:
                hours += ceil(pile / m)

            if hours <= h:
                min_speed = m
                r = m - 1
            else:
                l = m + 1
        return min_speed


             
