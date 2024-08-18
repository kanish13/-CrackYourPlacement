class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ss=set()
        l=0
        r=0
        ans=0
        while r<len(s) and l<=r:
            if s[r] not in ss:
                ss.add(s[r]) 
                ans= len(ss) if len(ss)>ans else ans
                r=r+1
            else: 
                ss.remove(s[l])
                l=l+1
        return ans




