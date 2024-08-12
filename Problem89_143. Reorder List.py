# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # middle element
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        sec=slow.next
        slow.next=None
        # reverse the second half
        prev=None
        curr=sec
        while curr:
            t=curr.next
            curr.next=prev
            prev=curr
            curr=t
        #merge
        f=head
        s=prev
        while f and s:
            t1=f.next
            t2=s.next
            f.next=s
            s.next=t1
            f=t1
            s=t2








        
