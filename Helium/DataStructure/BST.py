class Node:
    def __init__(self, key, Node):
        self.key = key
        self.right = None
        self.left = None
        self.parent = Node


def insert(root, key):
    if root is None:
        root = Node(key, None)
    else:
        if root.key < key:
            if root.right is None:
                root.right = Node(key, root)
            else:
                insert(root.right, key)
        else:
            if root.left is None:
                root.left = Node(key, root)
            else:
                insert(root.left, key)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)


def successor(node):
    if(node.right):
        return minvalue(node.right)
#     print('if not met')
    parent = node.parent
    while(parent.left != node):
        node = parent
        parent = node.parent

    return parent


def minvalue(node):
    current = node
    while current.left is not None:
        current = current.left

    return current


def find(root, key):
    if(root.key == key):
        return root
    elif (root.key > key):
        if root.left is None:
            return None
        else:
            node = find(root.left, key)
    else:
        if(root.right is None):
            return None
        else:
            node = find(root.right, key)
    return node


def delete(root1, key):
    global root

    node = find(root1, key)

    if(node.left is None or node.right is None):
        if(node.parent is None):
            pseudoroot = Node(0, None)
            pseudoroot.left = node
            node.parent = pseudoroot
            deleted = delete(root, key)
            root = node.parent.left
            if root is not None:
                root.parent = None
            return deleted
        if node is node.parent.left:
            node.parent.left = node.right or node.left
            if node.parent.left is not None:
                node.parent.left.parent = node.parent
        else:
            node.parent.right = node.right or node.left
            if node.parent.right is not None:
                node.parent.right.parent = node.parent
        return node
    else:
        suc_node = successor(node)
        node.key, suc_node.key = suc_node.key, node.key
        return delete(suc_node, key)


root = Node(20, None)
insert(root, 8)
insert(root, 22)
insert(root, 4)
insert(root, 12)
insert(root, 10)
insert(root, 14)

# inorder(r)
inorder(root)
print('delete 4')
# print(r.left.parent.key)
# print(minvalue(r).key)
# node = find(r, 14)
# print(successor(node).key)
# print(node.parent.key)
# print(successor(r).key)
# print "\nDelete 20"
delete(root, 4)
inorder(root)
print('delete 10')
print('deleted key', delete(root, 10).key)
inorder(root)
print('delete 12')
delete(root, 12)
inorder(root)
print('delete 20')
delete(root, 20)
inorder(root)
print('delete 22')
delete(root, 22)
inorder(root)
print('delete 8')
delete(root, 8)
inorder(root)
print('delete 14')
delete(root, 14)
inorder(root)
print('phirse')
inorder(root)
