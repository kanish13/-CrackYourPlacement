# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dum=ListNode(0)
        dum.next=head
        n=head
        x=dum
        while n:
            if n.val==val:
                x.next=n.next
            else:
                x=n
            n=n.next
        return dum.next
