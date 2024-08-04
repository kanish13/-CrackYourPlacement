"""
class node:
    def __init__(self,data):
        self.data = data
        self.next = None
"""

class Solution:
    def multiply_two_lists(self, first, second):
        # Code here
        n1=first
        n2=second
        num1=0
        num2=0
        mod=1000000007
        while n1:
        
            num1=(num1*10+(n1.data))%mod
            n1=n1.next 
        while n2:
     
            num2=(num2*10+(n2.data))%mod
            n2=n2.next 
        
        return (num1*num2)%mod
