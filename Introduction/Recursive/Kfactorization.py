# This is classified as Recursion problem in hackerRank. Shall it be DP?
# https://www.hackerrank.com/challenges/k-factorization/problem?isFullScreen=true

# straightforward recursive approach. As expected, about half tests failed because of timeout.
import time
from collections import defaultdict

def kfact(lst, tgt, clst, cprd, cbest):
    bst = cbest
    for i in lst:
        if i * cprd == tgt:
            if len(bst) > len(clst) + 1 or len(bst) == 0:
                bst = list(clst)
                bst.append(i)
        elif i * cprd < tgt:
            clst1 = list(clst)
            clst1.append(i)
            bst = kfact(lst, tgt, clst1, cprd * i, bst)

    return bst


def kFactorization(n, A):
    clst = []
    cprd = 1
    cbest = []
    A.sort()
    bst = kfact(A, n, clst, cprd, cbest)

    if len(bst) == 0:
        return -1

    ret = [1]
    for i in bst:
        ret.append(ret[-1] * i)
    return ret

# DP approach
def find_less(lst1, lst2):
    ret = []
    if len(lst1) < len(lst2):
        ret = lst1
    elif len(lst2) < len(lst1):
        ret = lst2
    else:
        ind = 0
        while lst1[ind] == lst2[ind] and ind < len(lst1):
            ind += 1

        if ind == len(lst1):
            # same? Doesn't matter than
            ret = lst1
        else:
            if lst1[ind] < lst2[ind]:
                ret = lst1
            else:
                ret = lst2

    return ret


def kFact(n, A):
    rec = [None]*(n + 1)
    rec[1] = [1]
    first_ele = True
    for i in A:
        ind = 1
        while ind*i <= n:
            if rec[ind] is not None:
                # ind is reachable
                # then ind * i is reachable
                nxt = ind * i
                new_lst = list(rec[ind])
                new_lst.append(rec[ind][-1]*i)
                if rec[nxt] is None:
                    rec[nxt] = new_lst
                else:
                    # check which one to keep
                    rec[nxt] = find_less(rec[nxt], new_lst)
            if first_ele:
                ind *= i
            else:
                ind += 1
        first_ele = False

    return rec[-1]


# greedy algorithm
# greedy is good for getting optimized. DP and Recursion is for
# counting total of different choices.
def greedy_alg(lst, trgt):
    # use the largest first. Sort the lst
    lst.sort(reverse=True)
    ret = [trgt]

    res = trgt
    for i in lst:
        while res%i == 0:
            res = int(res/i)
            ret.append(res)

        if res == 1:
            return list(reversed(ret))

    return [-1]


if __name__ == '__main__':
    lst = [2,3,5,7,11,13,17,19]
    n = 231000000
    s1 = time.time()

    s2 = time.time()
    print(greedy_alg(lst,n))
    s3 = time.time()

    print(s2-s1)
    print(s3-s2)