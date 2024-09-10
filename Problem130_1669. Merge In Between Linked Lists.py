# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        n1=list1
        n3=list2
        dum=ListNode(0)
        n2=dum
        c1=0
        while n1:
            if c1==a:
                n2.next=n3
                while c1<=b:
                    n1=n1.next
                    c1=c1+1
                while n2.next:
                    n2=n2.next
            else:
                n2.next=n1
                n1=n1.next
                n2=n2.next
                c1=c1+1
        return dum.next


