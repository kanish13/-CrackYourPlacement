class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum1=0
        sum2=0
        k=1
        for i in a[::-1]:
            if int(i) ==1:
                sum1=sum1+k
            k=k*2
        k=1
        for i in b[::-1]:
            if int(i)==1:
                sum2=sum2+k
            k=k*2
        t=sum1+sum2
        ans=""
        while t!=0:
            ans=ans+str((t%2))
            t=t//2
        if ans=="":
            return "0"
        return ans[::-1]
