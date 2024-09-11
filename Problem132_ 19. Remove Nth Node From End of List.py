# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def rev(head):
            prev=None
            curr=head
            while curr:
                t=curr.next
                curr.next=prev
                prev=curr
                curr=t
            return prev
        head=rev(head)

        c=0
        dum=ListNode(-1)
        x=dum
        while head:
            if c!=n-1:     
                x.next=ListNode(head.val)
                x=x.next
            c=c+1
            head=head.next
        return rev(dum.next)
