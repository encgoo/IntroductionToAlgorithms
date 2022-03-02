import sys
import time


def find_change(target, S, cur_num):

    if target == 0:
        return cur_num

    min_needed = sys.maxsize
    for s in S:
        if target >= s:
            min_needed = min(min_needed, find_change(target - s, S, cur_num + 1))

    return min_needed


def xp_find_change(target, S):

    lst = [sys.maxsize]*(target + 1)

    lst[0] = 0

    for s in S:
        for i in range(s, target + 1):
            lst[i] = min(lst[i], lst[i-s] + 1)

    return lst[target]


# Note, greedy might not work all the times.
# for example 9 for [5,3]. (5,3) will stuck. We need (3,3,3)
# assume that we have 1, this is not correct. Image target 6 for [4,3,1]. It will get (4, 1, 1) instead of (3,3)
def greedy(target, S):
    ret = 0

    remaining = target

    coins = sorted(S, reverse=True)

    for c in coins:
        while remaining - c >= 0:
            ret += 1
            remaining -= c

    return ret


if __name__ == '__main__':
    target = 6
    coins = [3,4,1]
    t1 = time.time()
    print(find_change(target, coins, 0))
    t2 = time.time()
    print(t2 - t1)
    print(xp_find_change(target, coins))
    t3 = time.time()
    print(t3 - t2)
    print(greedy(target, coins))
    t4 = time.time()
    print(t4 - t3)
