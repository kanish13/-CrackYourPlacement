# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sum=0
        dum=ListNode(0)
        x=dum
        n=head
        while n:
            if n.val==0:
                x.next=ListNode(sum)
                x=x.next
                sum=0
            else:
                sum=sum+n.val
            n=n.next
        return dum.next.next
                
