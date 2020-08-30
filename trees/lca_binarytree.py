def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        ppath = []
        qpath = []
        
        self.get_path(root, p, ppath)
        self.get_path(root, q, qpath)
        for path in ppath:
            if path in qpath:
                return path
        
    def get_path(self, root, node, path):
        if not root:
            return False
        if root.val == node.val:
            path.append(root)
            return True
        
        left = self.get_path(root.left, node, path)
        if left:
            path.append(root)
            return True
        right = self.get_path(root.right, node, path)
        if right:
            path.append(root)
            return True


def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # if both nodes are present
        if root is None:
            return None

        if root.val == p.val or root.val == q.val:
            return root
        
        left_lca = self.lowestCommonAncestor(root.left, p, q)
        right_lca = self.lowestCommonAncestor(root.right, p, q)
            
        if left_lca and right_lca:
            return root
        
        return left_lca if left_lca else right_lca




	# if nodes are not present then check if the nodes exist or not before returni
def lowestCommonAncestorUtil(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None

        if root.val == p.val or root.val == q.val:
            return root
        
        left_lca = self.lowestCommonAncestor(root.left, p, q)
        right_lca = self.lowestCommonAncestor(root.right, p, q)
            
        if left_lca and right_lca:
            return root
        
        return left_lca if left_lca else right_lca
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # if both nodes are present
	lca = self.lowestCommonAncestorUtil(root,p,q)

	if find(lca,p) and find(lca,q):
		return lca
	else:
           return None

def find(root, p):
    if not root:
	return False
   if root.data == p.data or find(root.left, p) or find(root.right,q)
	return True
