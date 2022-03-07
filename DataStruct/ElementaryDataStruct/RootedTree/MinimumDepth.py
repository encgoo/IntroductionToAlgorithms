
from collections import deque


class TNode:
    def __init__(self, v=None, l=None, r=None):
        self.v = v
        self.l = l
        self.r = r


def min_depth(root):
    q = deque()
    q.append(root)
    # append a separator
    q.append(TNode())
    lvl = 0
    while q:
        p = q.popleft()
        if p.v is None:
            # a separator
            lvl += 1
            if q:
                # append ONLY if q is not empty
                q.append(TNode())
            p = q.popleft()
        if not p.l and not p.r:
            # found a end node
            break
        else:
            if p.l:
                q.append(p.l)
            if p.r:
                q.append(p.r)

    return lvl

if __name__ == '__main__':
    rt = TNode(1)
    rt.l = TNode(2)
    rt.r = TNode(3)

    rt.l.l = TNode(4)
    rt.l.r = TNode(5)
    rt.l.r.l = TNode(9)
    rt.l.l.l = TNode(7)

    rt.r.r = TNode(6)
    rt.r.r.l = TNode(8)

    print(min_depth(rt))