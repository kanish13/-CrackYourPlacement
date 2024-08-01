# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        n1=list1
        n2=list2
        new=ListNode(0)
        x=new
        while n1 and n2:
            if n1.val<n2.val:
                x.next=n1
                n1=n1.next
            else:
                x.next=n2
                n2=n2.next
            x=x.next
        while n1:
            x.next=n1
            n1=n1.next
            x=x.next
        while n2:
            x.next=n2
            n2=n2.next
            x=x.next
        return new.next
