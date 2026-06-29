class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        mp = {}
        l, r = 0, 0
        max_window = 0

        while r < len(s):
            print(s[r])
            if s[r] in mp:
                del mp[s[l]]
                l+=1
            else:
                mp[s[r]] = "T"
                r+=1
            max_window = max(max_window, r-l)

        return max_window    