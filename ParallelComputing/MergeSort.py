import time
import random
import threading

# This is a good candidate for parallel computing.

th_ret = []
def merge(llst, rlst):
    lptr = 0
    rptr = 0
    ret = []
    while lptr < len(llst) and rptr < len(rlst):
        if llst[lptr] < rlst[rptr]:
            ret.append(llst[lptr])
            lptr += 1
        else:
            ret.append(rlst[rptr])
            rptr += 1

    ret.extend(llst[lptr:])
    ret.extend(rlst[rptr:])
    return ret

# normal merge sort
def merge_sort(lst):
    if len(lst) == 1:
        return lst

    mid = int(len(lst)/2)
    return merge(merge_sort(lst[:mid]), merge_sort(lst[mid:]))


# need to wrap to return to a global variable.
def wrapper(lst):
    global th_ret
    th_ret = merge_sort(lst)


# do it in parallel
def merge_par(lst):
    mid = int(len(lst)/2)
    llst = merge_sort(lst[:mid])

    t = threading.Thread(target=wrapper, args=(lst[mid:],))
    t.start()
    t.join()

    return merge(llst, th_ret)


def gen_lst():
    lst = []
    for i in range(10000):
        lst.append(int(random.random()*1000))
    return lst


if __name__ == '__main__':
    t1 = time.time()
    lst = gen_lst()
    print(merge_sort(lst))
    t2 = time.time()
    # when sz = 10000, the parallel computing is 10% faster
    print(merge_par(lst))
    t3 = time.time()
    print(t2-t1)
    print(t3-t2)


