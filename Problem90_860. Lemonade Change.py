class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills[0]!=5:
            return False
        f=0
        t=0

        for i in bills:
            if i==5:
                f=f+1
            elif i==10:
                if f>0:
                  f=f-1
                  t=t+1
                else:
                    return False
            else:
                if f>0 and t>0:
                    f=f-1
                    t=t-1 
                elif f>2:
                    f=f-3  
                else:
                    return False
        return True
