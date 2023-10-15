from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""
        target_count = Counter(t)
        
        left, right = 0, 0
        min_len = float('inf')
        min_window = ""
        current_count = Counter()
        required_chars = len(target_count)
        formed_chars = 0
        
        while right < len(s):
            current_char = s[right]
            current_count[current_char] += 1
            
            if current_char in target_count and current_count[current_char] == target_count[current_char]:
                formed_chars += 1
            
            while left <= right and formed_chars == required_chars:
                window_len = right - left + 1
                if window_len < min_len:
                    min_len = window_len
                    min_window = s[left:right+1]
                
                left_char = s[left]
                current_count[left_char] -= 1
                
                if left_char in target_count and current_count[left_char] < target_count[left_char]:
                    formed_chars -= 1
                
                left += 1
            
            right += 1
        
        return min_window
