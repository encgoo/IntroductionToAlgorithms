
from collections import deque

class TNode:
    def __init__(self, v=0, l=None, r=None):
        self.v = v
        self.l = l
        self.r = r


def symmetric_nodes(ln, rn):
    if not ln and not rn:
        return True
    if (ln and not rn) or (rn and not ln):
        return False

    if ln.v != rn.v:
        return False

    ret = symmetric_nodes(ln.l, rn.r)
    ret = ret and symmetric_nodes(ln.r, rn.l)

    return ret


def is_symmetric(root):
    if not root.l and not root.r:
        return True

    if (root.l and not root.r) or (root.r and not root.l):
        return False

    return symmetric_nodes(root.l, root.r)


if __name__ == '__main__':
    root = TNode(1)
    root.l = TNode(2)
    root.r = TNode(2)
    #root.l.l = TNode(3)
    root.l.r = TNode(3)
    #root.r.l = TNode(4)
    root.r.r = TNode(3)

    print(is_symmetric(root))


