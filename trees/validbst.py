def isValidBST(self, root: TreeNode) -> bool:
        return self.isBST(root, None, None)
        
def isBST(self, root, mini, maxi):
    if root is None:
        return True
        
    if mini!=None and root.val <= mini:
        return False
    if maxi!=None and root.val >= maxi:
        return False
        
    return self.isBST(root.left, mini, root.val) and self.isBST(root.right, root.val, maxi)


    def isValidBST(self, root: TreeNode) -> bool:
        prev = None
        return self.isBST(root, prev)
        
    def isBST(self, root, prev):
        if root is None:
            return True
        
        if self.isBST(root.left, prev) is False:
            return False
        if prev is not None and prev.val > root.val:
            return False
        
        prev = root
        return self.isBST(root.right, prev)
