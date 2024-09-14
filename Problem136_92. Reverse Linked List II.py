# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        for i in range(1, left):
            prev = prev.next
        curr = prev.next
        after = curr.next
        for i in range(right - left):
            curr.next = after.next
            after.next = prev.next
            prev.next = after
            after = curr.next
        
        return dummy.next
