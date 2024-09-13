# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def rev(head):
            prev=None
            curr=head
            while curr:
                t=curr.next
                curr.next=prev
                prev=curr
                curr=t
            return prev
        
        s=head
        f=head
        while f and f.next:
            s=s.next
            f=f.next.next
        
        n1=head
        n2=rev(s)
        maxi=0

        while n1 and n2:
            if (n1.val+n2.val)>maxi:
                maxi=n1.val+n2.val
            n1=n1.next
            n2=n2.next
        
        return maxi

