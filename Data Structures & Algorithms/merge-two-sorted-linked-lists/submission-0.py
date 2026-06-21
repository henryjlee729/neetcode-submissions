# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        dummy = ListNode(0)
        tail = dummy
        while p1 and p2:
            if p1.val > p2.val:
                tail.next = p2
                tail = p2
                p2 = p2.next
            else:
                tail.next = p1
                tail = p1
                p1 = p1.next
            
        if p1:
            tail.next = p1

        if p2:
            tail.next = p2
            
        return dummy.next    