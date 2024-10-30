class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        x=[]
        for i in intervals:
            if x:
                if i[0]<=x[-1][1]:
                    if i[1]>x[-1][1]:
                        x[-1][1]=i[1]

                else:
                    x.append(i)
            else:
                x.append(i)
        return x

