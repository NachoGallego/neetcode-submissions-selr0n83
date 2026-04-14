class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        t = sorted(t, key=str.casefold) 
        s = sorted(s, key=str.casefold) 
        print(s)
        print(t)       
        res = False
        if(s==t):
            res = True

        return res

        