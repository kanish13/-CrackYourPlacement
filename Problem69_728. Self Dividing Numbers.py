class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        x=[]
        for i in range(left,right+1):
            n=i
            f=0
            while i>0:
                d=i%10
                if d==0 or (n%d)!=0:
                    f=1
                    break
                i=i//10
            if f==0:
                x.append(n)
        return x



