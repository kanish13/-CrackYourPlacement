# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1=0
        l2=0
        n1=headA
        n2=headB
        while n1:
            l1=l1+1
            n1=n1.next
        while n2:
            l2=l2+1
            n2=n2.next
        while l1>l2:
            l1=l1-1
            headA=headA.next
        while l2>l1:
            l2=l2-1
            headB=headB.next
        while headA!=headB:
            headA=headA.next
            headB=headB.next
        return headA
