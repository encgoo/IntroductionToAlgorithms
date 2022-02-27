# https://www.hackerrank.com/challenges/lilys-homework/problem?isFullScreen=true
#
# Observations:
# 1. A beautiful array is just a sorted array.
# 2. When swapping two elements, the position of the rest don't change.
# 3. If an element is already in a good position, we don't need to touch it.
# 4. If an element is not in a good location, we swap it with the one in its location. Then it becomes a good one
#    and _stays_
# 5. We need to do the swap one by one to count

# Note this is a good example for parallel computing. The increment order and decrement order are
# basically independent, and can be done in separated threads.
def count(lst, slst):
    d = dict()
    for i in range(len(slst)):
        d[slst[i]] = i

    swap = 0
    i = 0
    while i < len(lst):
        if lst[i] == slst[i]:
            i += 1
        else:
            # need one swap
            swap += 1
            tmp = d[lst[i]]
            lst[i], lst[tmp] = lst[tmp], lst[i]
            # don't increment i, the newly lst[i] might not be final. keep the same i until it is final

    return swap


def count_swap(lst):
    slst = sorted(lst)
    # Note, need to make a copy of lst.
    swaps = count(list(lst), slst)
    slst.reverse()
    swaps = min(swaps, count(lst, slst))

    return swaps


if __name__ == '__main__':
    lst = [3,4,2,5,1, 9, 8]
    print(count_swap(lst))
