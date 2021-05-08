# Python3 program to check if two trees are mirror of each other

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def areMirror(a, b):
    if a is None and b is None:
        return True

    if a is None or b is None:
        return False

    return (a.data == b.data and
            areMirror(a.left, b.right) and
            areMirror(a.right, b.left))
