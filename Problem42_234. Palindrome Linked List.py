# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            f=f.next.next

        prev=None
        while slow:
            n=slow.next
            slow.next=prev
            prev=slow
            slow=n
        l=head
        r=prev
        while r:
            if l.val!=r.val:
                return False
            l=l.next
            r=r.next
        return True
