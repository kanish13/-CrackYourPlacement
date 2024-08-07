class Solution:
    def isFascinating(self, n: int) -> bool:
        num=str(n)+str(n*2)+str(n*3)

        x=sorted([int(i) for i in num])

        return x==[1,2,3,4,5,6,7,8,9]
        
