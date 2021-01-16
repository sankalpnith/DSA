def inorderSuccessor(root, x):
    # Code here
    if x.right is not None:
        x = x.right
        while x.left is not None:
            x = x.left
        return x
    else:
        output = None
        while root is not None:
            if x.data < root.data:
                output = root
                root = root.left
            elif x.data > root.data:
                root = root.right
            else:
                break;
        return output
