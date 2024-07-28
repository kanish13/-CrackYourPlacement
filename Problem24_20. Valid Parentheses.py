# 20. Valid Parentheses Link: https://leetcode.com/problems/valid-parentheses/description/

# Solution:

class Solution:
    def isValid(self, s: str) -> bool:
        h={")":"(","]":"[","}":"{"}
        x=[]
        for i in s:
            if i in h:
                if lacen(x)>0 and x[-1]==h[i]:
                    x.pop()
                else:
                    return False
            else:
                x.append(i)
        if x:
            return False
        else:
            return True
            

     
