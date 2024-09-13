# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        c=0
        n1=None
        n2=None
        curr=head
        while curr:
            c=c+1
            if c==k:
                n1=curr
                n2=head
            if c>k:
                n2=n2.next
            curr=curr.next
        
        n1.val,n2.val=n2.val,n1.val
        return head
        




        
