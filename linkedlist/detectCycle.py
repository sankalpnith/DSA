def detectCycle(head):
    if head is None or head.next is None or head.next.next is None:
        return None
    slow, fast = head.next, head.next.next
    while slow != fast:
        if slow is None or fast is None or fast.next is None:
            return None
        slow = slow.next
        fast = fast.next.next
    fast = head
    while fast != slow:
        fast = fast.next
        slow = slow.next
    return fast
