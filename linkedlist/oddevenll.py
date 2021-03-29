# https://leetcode.com/problems/odd-even-linked-list/
# Given a singly linked list, group all odd nodes together followed by the even nodes.
# Please note here we are talking about the node number and not the value in the nodes.
#
# You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.
#
# Example 1:
#
# Input: 1->2->3->4->5->NULL
# Output: 1->3->5->2->4->NULL


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next or not head.next.next:
            return head

        t1 = head1 = head
        t2 = head2 = head.next
        while t1.next is not None:
            t1.next = t1.next.next
            if t1.next is not None:
                t1 = t1.next
            if t2.next is not None:
                t2.next = t2.next.next
                if t2.next is not None:
                    t2 = t2.next
        t1.next = head2
        return head1