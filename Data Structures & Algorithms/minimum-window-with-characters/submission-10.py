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
                


                    


                


            

            
            
                
                    
                    


        