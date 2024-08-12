# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        f=head
        while f and f.next:
            t=f.val
            f.val=f.next.val
            f.next.val=t
            f=f.next.next
        return head
       
