# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p, fast, slow =None,  head, head
        while fast and fast.next:
            p = slow
            slow = slow.next
            fast = fast.next.next
        p.next = None
        left_sorted = self.sortList(head)
        right_sorted = self.sortList(slow)
        return self.merge(left_sorted, right_sorted)

    def merge(self, l1, l2):
        out = ListNode()
        dummy = out
        while l1 and l2:
            if l1.val < l2.val:
                dummy.next, l1 = l1, l1.next
            else:
                dummy.next, l2 = l2, l2.next

            dummy = dummy.next

        if l1:
            dummy.next = l1
        if l2:
            dummy.next = l2
        return out.next