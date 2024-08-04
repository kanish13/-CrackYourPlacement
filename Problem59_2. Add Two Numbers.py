# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dum=ListNode(0)
        x=dum
        n1=l1
        n2=l2
        c=0
        while n1 or n2 or c!=0:
            d1=n1.val if n1 else 0
            d2=n2.val if n2 else 0
            sum=d1+d2+c
            digit=sum%10
            c=sum//10
            x.next=ListNode(digit)
            x=x.next
            n1=n1.next if n1 is not None else None
            n2=n2.next if n2 is not None else None
        return dum.next

