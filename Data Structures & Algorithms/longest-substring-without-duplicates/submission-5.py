class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_size = 0
        l, r = 0, 0
        n = len(s)

        while r < n:
            sub_string = s[l:r+1]  # include character at r
            if len(set(sub_string)) == len(sub_string):  # all unique characters
                max_size = max(max_size, len(sub_string))
                r += 1
            else:
                l += 1  # shrink window from left
        
        return max_size