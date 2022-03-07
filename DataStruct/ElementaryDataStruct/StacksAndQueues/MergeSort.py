# Use merge sort to sort a linked list


class LNode:
    def __init__(self, v=0, n=None):
        self.v = v
        self.n = n


def make_lst(arr):
    head = LNode(arr[0])
    p = head
    for i in arr[1:]:
        p.n = LNode(i)
        p = p.n
    return head


def print_lst(lst):
    nd = lst
    while nd:
        print(nd.v, end=', ')
        nd = nd.n


def split(lst):
    if lst.n and not lst.n.n:
        # only two
        ret = lst.n
        lst.n = None
        return ret

    fast = lst
    slow = lst
    slow_parent = None
    while fast.n and fast.n.n:
        fast = fast.n.n
        slow_parent = slow
        slow = slow.n
    if slow_parent:
        slow_parent.n = None

    return slow


def merge(lst1, lst2):
    dummy = LNode(0)
    w_nd = dummy
    r_nd1 = lst1
    r_nd2 = lst2

    while r_nd1 and r_nd2:
        if r_nd1.v < r_nd2.v:
            w_nd.n = r_nd1
            w_nd = r_nd1
            r_nd1 = r_nd1.n
        else:
            w_nd.n = r_nd2
            w_nd = r_nd2
            r_nd2 = r_nd2.n

    if r_nd1:
        w_nd.n = r_nd1

    if r_nd2:
        w_nd.n = r_nd2

    return dummy.n


def merge_sort(lst):
    if not lst.n:
        return lst

    lst2 = split(lst)

    return merge(merge_sort(lst), merge_sort(lst2))


if __name__ == '__main__':
    lst = make_lst([1,9,2,8,3,7,4,6,5])
    print_lst(lst)
    print('')
    ret = merge_sort(lst)
    print_lst(ret)
