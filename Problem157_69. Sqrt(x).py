class Solution:
    def mySqrt(self, x: int) -> int:
        l=0
        h=x
        res=0
        while l<=h:
            mid=(l+h)//2

            if mid**2==x:
                return mid
            elif mid**2>x:
                h=mid-1
            else:
                l=mid+1
                res=mid
        return res
