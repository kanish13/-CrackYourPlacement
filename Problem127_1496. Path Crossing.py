class Solution:
    def isPathCrossing(self, path: str) -> bool:
        s=set()
        s.add((0,0))
        x,y=0,0

        for i in path:
            if i=="N":
                y=y+1
            elif i=="S":
                y=y-1
            elif i=="E":
                x=x+1
            else:
                x=x-1
            if (x,y) in s:
                return True
            s.add((x,y))
        return False
