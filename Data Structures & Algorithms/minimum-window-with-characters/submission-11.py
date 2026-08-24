class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window_hash = {}
        t_hash = {}
        for char in t:
            t_hash[char] = t_hash.get(char, 0) + 1
        
        l = 0
        min_window_length = len(s) + 1
        need = len(t_hash)
        have = 0

        for r in range(len(s)):
            window_hash[s[r]] = window_hash.get(s[r], 0) + 1
            if s[r] in t_hash:
                if window_hash[s[r]] == t_hash[s[r]]:
                    have += 1
            while have == need:
                current_window = (r - l) + 1
                if min_window_length > current_window:
                    min_left = l
                    min_right = r
                    min_window_length = current_window
                window_hash[s[l]] -= 1
                if s[l] in t_hash:
                    if window_hash[s[l]] < t_hash[s[l]]:
                        have -= 1
                l += 1

        if min_window_length == len(s) + 1:
            return ""
        else:    
            min_window_string = "".join(s[min_left:min_right + 1])
            return min_window_string
                

"""
1. Build t hash table and window hash table.

2. set min_window_length to a value larger than the string itself (ie. something impossible to reach), so
that we can use it as a placeholder to check at the end if we ever reached a valid window. If the min_window_length 
is equal to the impossible value we set, it means a valid window was never achieved.

3. we will use 'need' and 'have' to check if we have met the requirements of the t_hashtable. This saves us 
from a brute force approach that would require us to loop through the t_hashtable every iteration to check whether the window has the requirements. instead we use the have and need as running values, which allow
us to check the validity of the window rather than looping through the whole t_hashmap to check if the current
window is valid. Instead, each time we add s[r] to the window, we check two things:
  1. Is it in the t_hashmap
  2. If true, have we met the requirement? for example:
    t_hash = {A: 2, B: 1} // we check if the current window_hash[s[r]] has the same values as stored in
    the t_hashtable, so for example, we would be looking for window_hash[A] = 2. If this is true, then we 
    increase 'have' by 1. Then after we check if have == need, which saves us from constantly looping
    through t_hash to check if our window is valid.

4. if the window is valid, and have == need, then we take the l + r indices of the valid substring/window, and
record the min_window_length.

5. As our window is still currently valid, we now want to shrink the window to check if we still have a 
valid window which is smaller than the current window. Every time we shrink the window, we remove the current
l from the window, and then check if the window is still valid. This is done by checking if the left char
that we have removed is in t_hash. If it is still in t_hash, we want to see if after removing the current
s[l] and decrementing its window_hash count, has the count fallen below the required count in t_hash. ie, A: 2. if A is now 1, we have no longer met the requirement, and we
subtract one from our 'have' value to indicate that the window is no longer valid. l += 1 shrinks the window.

6. The end result: We check if the min_window_length is still the impossivle value we set at the beginning to check if there was no valid window, and so we return "". If not, and there was a valid window, we use the indices we recorded to slice the string and return the minimum valid window.


"""
                    


                


            

            
            
                
                    
                    


        