from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        right = 0
        best_left = 0
        best_right = 0
        best_length = float("inf")

        formed = 0
        required = len(set(t))

        s_counter = Counter()
        t_counter = Counter(t)
        for right in range(len(s)):
            r_c = s[right]
            s_counter[r_c] += 1
            if r_c in t_counter and s_counter[r_c] == t_counter[r_c]:
                formed += 1
            
            while formed == required:
                if right - left + 1 < best_length:
                    best_length = right - left + 1
                    best_left = left
                    best_right = right
                
                l_c = s[left]
                s_counter[l_c] -= 1
                if l_c in t_counter and s_counter[l_c] < t_counter[l_c]:
                    formed -= 1

                left += 1
        
        if best_length == float("inf"):
            return ""
        
        return s[best_left : best_right + 1]