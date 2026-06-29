class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        
        l = 0
        r = len(s) - 1

        while l < r:
            l_val = s[l]
            while not l_val.isalnum() and l<r:
                l += 1
                l_val = s[l]

            r_val = s[r]
            while not r_val.isalnum() and r>l:
                r -= 1
                r_val = s[r]
            print(l_val, r_val)
            print(l,r)
            if r_val != l_val:
                return False
 
            l += 1
            r -= 1
        
        return True
        