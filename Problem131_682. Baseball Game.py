class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s=[]
        for i in operations:
            if i.isdigit() or (i[0]=="-" and i[-1].isdigit()):
                
                s.append(int(i))
            elif i=="C":
                if s:
                    s.pop()
            elif i=="D":
                if s:
                   s.append(2*s[-1])
            else:
                if len(s)>1:
                   s.append(s[-1]+s[-2])
        return sum(s)
