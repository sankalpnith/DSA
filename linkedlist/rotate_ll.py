# https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None or k == 0:
            return head
        slow_ptr = fast_ptr = head
        count = 0
        for _ in range(k):
            if slow_ptr is None:
                break
            count += 1
            slow_ptr = slow_ptr.next
        if slow_ptr is None:
            k %= count
            if k and count != 1:
                slow_ptr = head
                for _ in range(k):
                    slow_ptr = slow_ptr.next
            else:
                return head
        while slow_ptr.next is not None:
            fast_ptr = fast_ptr.next
            slow_ptr = slow_ptr.next
        new_head = fast_ptr.next
        fast_ptr.next = None
        slow_ptr.next = head
        return new_head
