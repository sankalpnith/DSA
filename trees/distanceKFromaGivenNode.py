# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def __init__(self):
        self.parent = {}

    def calculate_parent(self, root):
        queue = []
        queue.append(root)

        while queue:
            node = queue.pop()
            if node == root:
                self.parent[node] = None
            if node.left:
                self.parent[node.left] = node
                queue.append(node.left)
            if node.right:
                self.parent[node.right] = node
                queue.append(node.right)

    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:

        self.calculate_parent(root)
        visited = set()
        queue = []
        queue.append(target)
        visited.add(target)
        dist = 0
        output = []
        while queue:

            if dist == K:
                output = [node.val for node in queue]
                return output

            level_size = len(queue)
            # print(dist, queue, level_size)
            while level_size:
                node = queue.pop(0)

                if node.left and node.left not in visited:
                    queue.append(node.left)
                    visited.add(node.left)
                if node.right and node.right not in visited:
                    queue.append(node.right)
                    visited.add(node.right)
                if self.parent[node] and self.parent[node] not in visited:
                    queue.append(self.parent[node])
                    visited.add(self.parent[node])
                level_size -= 1
            dist += 1
        return output