# MergeKsorted shows how to merge k sorted linked lists.

# This shows how to merge k arrays. It is about the trick to use heap in python

from heapq import heappush
from heapq import heappop


def merge_k(lsts):
    num_lst = len(lsts)

    hp = []
    # init with the first element
    for i in range(num_lst):
        if len(lsts[i]) > 0:
            heappush(hp, (lsts[i][0], i, 0))
    ret = []
    while len(hp) > 0:
        p = heappop(hp)
        ret.append(p[0])
        i = p[1]
        idx = p[2]

        # check if we have more from the same list
        if idx + 1 < len(lsts[i]):
            heappush(hp, (lsts[i][idx + 1], i, idx + 1))

    return ret


if __name__ == '__main__':
    lsts = [
        [0, 3, 6, 9, 12, 15],
        [1, 4, 7, 10, 13, 16],
        [2, 5, 8, 11, 14, 17]
    ]
    print(merge_k(lsts))