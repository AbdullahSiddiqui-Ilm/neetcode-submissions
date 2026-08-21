class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_value = 0
        l = 0
        n = len(s)
        count = {}

        for r in range(n):
            window_size = (r - l) + 1
            count[s[r]] = count.get(s[r], 0) + 1
            if (window_size - max(count.values())) <= k :
                max_value = max(window_size, max_value)
            while (window_size - max(count.values())) > k:
                count[s[l]] = count.get(s[l], 0) - 1
                l += 1
                window_size = (r - l) + 1
                max_value = max(window_size, max_value)
        return max_value

