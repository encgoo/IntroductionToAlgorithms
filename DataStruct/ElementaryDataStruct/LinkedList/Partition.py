# https://www.programcreek.com/2013/02/leetcode-partition-list-java/
# Note the above question has different definition of partition from the one used in quick sort

# here we do a partition like the one used in Quick sort.

class LNode:
    def __init__(self, v=0, n=None):
        self.v = v
        self.n = n

def create_lst(arr):
    ret = LNode(arr[0])
    p = ret
    for i in arr[1:]:
        n = LNode(i)
        p.n = n
        p = p.n

    return ret


def print_lst(lst, sep=','):
    n = lst
    while n:
        print(n.v, end=sep)
        n = n.n

def partition(lst, pv):
    lhead = LNode(0)
    rhead = LNode(0)

    l = lhead
    r = rhead

    rptr = lst
    pnode = None
    while rptr:
        if rptr.v > pv:
            r.n = rptr
            r = r.n
        elif rptr.v < pv:
            l.n = rptr
            l = l.n
        else:
            pnode = rptr

        rptr = rptr.n

    ret = lhead.n
    if not ret:
        ret = pnode
        ret.n = rhead.n
        r.n = None
    else:
        l.n = pnode
        pnode.n = rhead.n
        r.n = None

    return ret


if __name__ == '__main__':
    lst = create_lst([1,4,3,2,5,2])
    lst = partition(lst, 3)
    print_lst(lst)
