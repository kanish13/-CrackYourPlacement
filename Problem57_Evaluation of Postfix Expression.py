class Solution:
    
    #Function to evaluate a postfix expression.
    def evaluatePostfix(self, S):
        #code here
        s=[]
        for i in S:
            if i.isnumeric():
                s.append(int(i))
            else:
                if len(s)>=2:
                    s1=s.pop()
                    s2=s.pop()
                    if i=="+":sum=s2+s1
                    if i=="-":sum=s2-s1
                    if i=="*":sum=s2*s1
                    if i=="/":sum=s2//s1
                    s.append(sum)
        return s[-1]
