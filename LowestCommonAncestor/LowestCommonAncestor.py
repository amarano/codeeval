__author__ = 'angelo'


class Node:
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.value = val


def binaryInsert(root, node):
    if root is None:
        root = node
    else:
        if node.value < root.value:
            if root.l_child is None:
                root.l_child = node
            else:
                binaryInsert(root.l_child, node)
        if node.value > root.value:
            if root.r_child is None:
                root.r_child = node
            else:
                binaryInsert(root.r_child, node)

def main():
    root = None
    for i in [30, 8, 52, 3, 20, 10, 29]:
        newNode = Node(i)
        binaryInsert(root, newNode)
        root = newNode

main()
