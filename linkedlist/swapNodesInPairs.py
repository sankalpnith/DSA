def swapPairs(head):
    if head is None or head.next is None:
        return head
    tmp = head
    head = head.next
    next_set = head.next
    tmp, tmp.next = tmp.next, tmp
    tmp.next.next = next_set
    tmp = tmp.next
    while tmp.next is not None and tmp.next.next is not None:
        prev = tmp
        curr = tmp.next
        remaining = curr.next.next
        curr, curr.next = curr.next, curr
        curr.next.next = remaining
        tmp = curr.next
        prev.next = curr
    return head