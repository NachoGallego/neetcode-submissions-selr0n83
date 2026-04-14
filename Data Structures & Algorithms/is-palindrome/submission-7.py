class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        res = True
        s2 = []
        for i in s:
            if i.isalnum() == True:
                s2.append(i.lower())

        l,r = 0, len(s2)-1
        while l < r:

            if s2[l] != s2[r]:
                return False
            else:
                l = l+1
                r = r-1
        return res

                
            