class LNode:
    def __init__(self, v=0, n=None):
        self.v = v
        self.n = n


def print_link_list(lst):
    n = lst
    while n:
        print(n.v, end='')
        n = n.n
    print('')


def add(llst, rlst):
    carry = False

    ln = llst
    rn = rlst
    ret = None
    cur = None
    while ln or rn:
        val = 0
        if ln:
            val += ln.v
        if rn:
            val += rn.v

        if carry:
            val += 1

        if val//10 > 0:
            carry = True
        else:
            carry = False

        nn = LNode(val%10)

        if not ret:
            ret = nn
        else:
            cur.n = nn

        cur = nn

        if ln:
            ln = ln.n
        if rn:
            rn = rn.n

    if carry:
        nn = LNode(1)
        cur.n = nn

    return ret


if __name__ == '__main__':
    lst = LNode(2)
    lst.n = LNode(4)
    lst.n.n = LNode(5)

    rlst = LNode(5)
    rlst.n = LNode(6)
    rlst.n.n = LNode(4)
    rlst.n.n.n = LNode(9)
    rlst.n.n.n.n = LNode(9)

    ret = add(lst, rlst)
    print_link_list(ret)
