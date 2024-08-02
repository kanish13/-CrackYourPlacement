'''
	Your task is to segregate the list of 
	0s,1s and 2s.
	
	Function Arguments: head of the original list.
	Return Type: head of the new list formed.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

'''
class Solution:
    #Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        #code here
        l=[]
        n=head
        while n:
            l.append(n.data)
            n=n.next
        l.sort()
        dum=Node(0)
        x=dum
        for i in range(len(l)):
            x.next=Node(l[i])
            x=x.next
        return dum.next
    
