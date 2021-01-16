# print sum of ll for both reversed order and forward order
# 6->7-1 + 1->2 == 176+21=197 ==> 7->9->1
# 6->7->1 + 1->2 == 671 + 12 ==> 683


class LinkedList:
    def __init__(self, value, next):
        self.value = value
        self.next = next


def calculate_sum(node1, node2):
    carry = 0
    output = final = LinkedList(0, None)
    while node1 is not None or node2 is not None:
        val1 = node1.value if node1 else 0
        val2 = node2.value if node2 else 0
        sum = val1 + val2 + carry
        carry = sum//10
        val = sum % 10
        final.next = LinkedList(val, None)
        final = final.next
        if node1 is not None:
            node1 = node1.next
        if node2 is not None:
            node2 = node2.next

    if carry > 0:
        final.next = LinkedList(carry, None)
    return output.next

def reverse(node):
    prev_node = None
    while node is not None:
        next_node = node.next
        node.next = prev_node
        prev_node = node
        node = next_node
    return prev_node

if __name__=="__main__":
    node1 = LinkedList(6,None)
    node1.next = LinkedList(7, None)
    node1.next.next = LinkedList(1, None)
    node2 = LinkedList(2, LinkedList(1,LinkedList(2,None)))
    final_ll = calculate_sum(node2,node1)
    while final_ll is not None:
        print(final_ll.value)
        final_ll = final_ll.next

    # reversal
    node1 = reverse(node1)
    node2 = reverse(node2)
    final_ll = calculate_sum(node1, node2)
    final_ll = reverse(final_ll)
    while final_ll is not None:
        print(final_ll.value)
        final_ll = final_ll.next