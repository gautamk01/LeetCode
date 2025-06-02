class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


n1 = Node(5)
n2 = Node(6)
n3 = Node(8)
n4 = Node(9)
n5 = Node(1)
n6 = Node(7)

n1.left = n2
n2.left = n3
n2.right = n4
n4.left = n5
n1.right = n6


def inorder(v: Node):
    if (v):
        print(v.data, end=" ")
        inorder(v.left)
        inorder(v.right)


def bfs(v: Node):
    if v is None:
        return []
    q = [v]
    while q:
        curr = q.pop(0)
        print(curr.data, end=" ")
        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)


bfs(n1)
