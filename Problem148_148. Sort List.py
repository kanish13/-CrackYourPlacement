# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n=head
        x=[]
        while n:
            x.append(n.val)
            n=n.next
        x=sorted(x)

        dum=ListNode(-1)
        y=dum
        i=0
        while i<len(x):
            y.next=ListNode(x[i])
            y=y.next
            i=i+1
        return dum.next
        
