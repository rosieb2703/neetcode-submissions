class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_size = 0
        l, r = 0, 0

        while r < len(s):
            sub_string = s[l:r+1]
            if len(set(sub_string)) == len(sub_string):
                r += 1
                max_size = max(max_size, len(sub_string))
            else:
                l += 1
            
        return max_size
            