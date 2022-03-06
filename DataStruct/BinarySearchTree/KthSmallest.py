class TNode:
    def __init__(self, v=0, l=None, r=None):
        self.v = v
        self.l = l
        self.r = r


class Rec:
    def __init__(self, v):
        self.v = v
        self.count = 0
        self.ret = None


def dfs_rec(n, rec):
    ret = False
    if n.l:
        ret = dfs_rec(n.l, rec)
    if ret:
        return True

    if rec.count == rec.v - 1:
        rec.ret = n.v
        return True
    else:
        rec.count += 1

    if n.r:
        ret = dfs_rec(n.r, rec)

    return ret


def kth_smallest(root, k):
    rec = Rec(k)
    dfs_rec(root, rec)
    return rec.ret


def dfs(node, lst):
    if node.l:
        dfs(node.l, lst)
    lst.append(node.v)
    if node.r:
        dfs(node.r, lst)


if __name__=='__main__':
    root = TNode(10)
    root.l = TNode(2)
    root.l.l = TNode(1)
    root.l.r = TNode(3)
    root.l.r.r = TNode(5)

    root.r = TNode(60)
    root.r.l = TNode(15)

    lst = []
    dfs(root, lst)
    print(lst)

    print(kth_smallest(root, 8))