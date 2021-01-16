# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pt1 = pt2 = head
        for i in range(n):
            pt1 = pt1.next
        if not pt1:
            return head.next
        while pt1.next:
            pt1 = pt1.next
            pt2 = pt2.next
        pt2.next = pt2.next.next
        return head