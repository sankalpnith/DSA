def height(self, root):O(n^2)
        if root is None:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))
def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        lheight = self.height(root.left)
        rheight = self.height(root.right)
        
        ldiameter = self.diameterOfBinaryTree(root.left)
        rdiameter = self.diameterOfBinaryTree(root.right)
        return max(lheight + rheight, max(ldiameter,rdiameter))


def diameter_height(self, root):
        if not root:
            return 0,0
        lheight, ldiameter = self.diameter_height(root.left)
        rheight, rdiameter = self.diameter_height(root.right)
        height = 1+ max(lheight, rheight)
        diameter = max(lheight+rheight,ldiameter,rdiameter)
        return height, diameter
def diameterOfBinaryTree(self, root: TreeNode) -> int:
        h,d = self.diameter_height(root)
        return d 
