
class TNode:
    def __init__(self, v=0, l=None, r=None):
        self.v = v
        self.l = l
        self.r = r


def is_balanced(node):
    if not node.l and not node.r:
        return True, 1

    ret = True
    lnum = 0
    if node.l:
        isGood, lnum = is_balanced(node.l)
        ret = ret and isGood

    rnum = 0
    if node.r:
        isGood, rnum = is_balanced(node.r)

    ret = ret and isGood and abs(lnum - rnum) <= 1

    return ret, lnum + rnum + 1


if __name__ == '__main__':
    root = TNode(0)
    root.l = TNode(1)
    root.r = TNode(2)
    root.r.r = TNode(3)
    root.r.l = TNode(4)

    ret, _ = is_balanced(root)
    print(ret)


