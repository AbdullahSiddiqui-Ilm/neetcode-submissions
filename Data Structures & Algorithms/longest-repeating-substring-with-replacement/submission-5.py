class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        l = 0
        n = len(s)
        count = {}

        for r in range(n):
            window_size = (r - l) + 1
            count[s[r]] = count.get(s[r], 0) + 1
            if (window_size - max(count.values())) <= k:
                max_length = max(window_size, max_length)

            while (window_size - max(count.values())) > k:
                count[s[l]] -= 1
                l += 1
                window_size = (r - l) + 1

        return max_length

"""
- For each substring/window, we replace the less frequent characters with    the more frequent characters. E.g. “AAAB” -> “AAAA”. 

- We want to find the number of replacements in each window, using the equation replacements needed = (window size -  most frequent character frequency) <= k'.  

- If this equation is true, we expand the window, however if the equation is false, we shrink the window. Note: When the window moves right and expands, add the current index to hash table and add 1 to its frequency. if the window is invalid and shrinks, we decrease the frequency of the current left index by 1 and then shrink the window 

- We compare the max value to the current window length, and choose the maximum from the two values on each iteration to be stored in max value. 

- Return max value.  
"""

