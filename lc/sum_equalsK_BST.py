# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

def findTarget(self, root, k) -> bool:
    order = {}
    queue = []
    queue.append(root)
    while queue:
        node = queue.pop(0)
        if k - node.val in order:
            return True
        order[node.val] = 1
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


def calculate_pairs(root, target):

    it1, it2 = [], []
    pointer = root
    pairs = []
    while pointer is not None:
        it1.append(pointer)
        pointer = pointer.left
    pointer = root

    while pointer is not None:
        it2.append(pointer)
        pointer = pointer.right

    while it1[-1] != it2[-1]:
        value1 = it1[-1].data
        value2 = it2[-1].data

        if value1 + value2 == target:
            pairs.append((value1, value2))
        elif value1 + value2 < target:
            pointer = it1.pop().right

            while pointer is not None:
                it1.append(pointer)
                pointer = pointer.left
        else:
            pointer = it2.pop().left

            while pointer is not None:
                it2.append(pointer)
                pointer = pointer.right
    return pairs






# Approaches
# 1. Create InOrder traversal of a bst -> sorted order then use two pointer technique
# Time -> O(n)
# Space -> O(n)
#
# 2. Traversing the bst create level order traversal and check while creating level order traversal
# Time -> O(n)
# Space -> O(n)
#
# 3. Create two pointer arrays -> one array containing left pointers and second array containing right pointers
# Time -> O(n)
# Space -> O(log(N)) height of tree
