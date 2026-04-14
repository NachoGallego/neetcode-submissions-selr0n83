class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        sset = set()
        n = len(s)
        lng = 0

        for r in range(n):
            while s[r] in sset:

                sset.remove(s[l])
                l +=1
            w = (r-l)+1
            sset.add(s[r])
            lng = max(lng,w)
        return lng


