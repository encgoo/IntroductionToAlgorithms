import time


def util(poss):
    max_ = 0
    i = -1
    for j in range(len(poss)):
        if len(poss[j]) > max_:
            max_ = len(poss[j])
            i = j
    return [poss[i]]

# brute force
def rec_act_sel(s, f, i, cols):

    ret = list(cols)

    if cols:
        if s[i] >= f[cols[-1]]:
            ret.append(i)
    else:
        ret.append(i)

    if i == len(s) - 1:
        return [ret]

    lst1 = rec_act_sel(s, f, i + 1, ret)
    lst2 = rec_act_sel(s, f, i + 1, cols)

    lst1.extend(lst2)
    return util(lst1)


def act_sel1(s, f):
    cols = []
    poss = rec_act_sel(s, f, 0, cols)

    ret = util(poss)
    return ret[0]


# DP
def act_sel_dp(s, f):
    # observation, the same i has been called many times.
    rec = [None]*len(s)
    cols = []
    poss = rec_act_sel_dp(s, f, 0, cols, rec)

    ret = util(poss)
    return ret[0]


def rec_act_sel_dp(s, f, i, cols, rec):

    if rec[i]:
        return rec[i]

    ret = list(cols)

    if cols:
        if s[i] >= f[cols[-1]]:
            ret.append(i)
    else:
        ret.append(i)

    if i == len(s) - 1:
        return [ret]

    lst1 = rec_act_sel_dp(s, f, i + 1, ret, rec)
    lst2 = rec_act_sel_dp(s, f, i + 1, cols, rec)

    lst1.extend(lst2)
    lst1 = util(lst1)

    rec[i] = lst1
    return lst1


# Note we want to get most activities (biggest count of activities), not max total time
# of activities.

# So it makes sense to
# 1. sort according to the ending time
# 2. pick according to end time. The sooner to end, the more to fit in
# 3. Once ended pick the next available.


def act_sel(s, f):
    i = 0

    ret = [0]
    for j in range(len(s)):
        if s[j] > f[i]:
            ret.append(j)
            i = j

    return ret

if __name__ == '__main__':
    s = [1,3,0,5,3,5, 6, 8, 8, 2,12]
    f = [4,5,6,7,8,9,10,11,12,13,14]

    t1 = time.time()
    print(act_sel(s, f))
    t2 = time.time()
    print(act_sel1(s, f))
    t3 = time.time()
    print(act_sel_dp(s, f))
    t4 = time.time()

    print(t2-t1)
    print(t3-t2)
    print(t4-t3)