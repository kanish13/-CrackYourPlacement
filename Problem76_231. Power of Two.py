class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        c=0
        x=n
        while n>1:
            c=c+1
            if n%2==0:
                n=n//2
            else:
                break
        return (2**c)==x
