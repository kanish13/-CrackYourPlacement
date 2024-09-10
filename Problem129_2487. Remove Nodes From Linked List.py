# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
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
        maxi=head.val
        curr=head
        while curr.next:
            if curr.next.val<maxi:
                curr.next=curr.next.next
            else:
                maxi=curr.next.val
                curr=curr.next
        return rev(head)
            
