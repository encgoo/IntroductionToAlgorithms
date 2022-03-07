class TNode:
    def __init__(self, v=0, l=None, r=None):
        self.v = v
        self.l = l
        self.r = r


def morris_traversal(root):
    cur = root

    while cur:
        if cur.l is None:
            # for an extreme case, no left child at all. Just a linked list then
            print(cur.v, end=' ')
            cur = cur.r
        else:
            pre = cur.l

            while pre.r is not None and pre.r is not cur:
                pre = pre.r

            if pre.r is cur:
                pre.r = None
                cur = cur.r
            else:
                print(cur.v, end=' ')
                pre.r = cur
                cur = cur.l


def pre_order(node):
    if node:
        print(node.v, end=' ')
        pre_order(node.l)
        pre_order(node.r)


if __name__ == '__main__':
    root = TNode(1)
    root.l = TNode(2)
    root.r = TNode(3)

    root.l.l = TNode(4)
    root.l.r = TNode(5)

    root.r.l = TNode(6)
    root.r.r = TNode(7)

    pre_order(root)

    morris_traversal(root)

