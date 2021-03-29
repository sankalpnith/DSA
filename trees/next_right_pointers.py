#https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/submissions/

#Input: root = [1,2,3,4,5,null,7]
#Output: [1,#,2,3,#,4,5,7,#]
#Explanation: Given the above binary tree (Figure A),
# your function should populate each next pointer to point to its next right node, just like in Figure B.
# The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

# level order traversal
# printing each level separate

def connect(self, root: 'Node') -> 'Node':
    if not root:
        return root
    queue = []
    queue.append(root)
    output = []
    while queue:
        level = []
        size = len(queue)
        while size != 0:
            node = queue.pop(0)
            level.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            size -= 1
        for index, node in enumerate(level[:-1]):
            node.next = level[index + 1]
        output.extend(level)
    return output[0]
