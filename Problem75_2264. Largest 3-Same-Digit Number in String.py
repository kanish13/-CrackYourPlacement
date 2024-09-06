class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res=-1
        l=0
        r=2
        while r<len(num):
            if num[l]==num[r] and num[l+1]==num[r] and int(num[l])>res:
                res=int(num[r])
            l=l+1
            r=r+1
        if res==-1:
            return ""
        return str(res)*3
       

