# This is listed as Recurssion
# https://www.hackerrank.com/challenges/arithmetic-expressions/problem?isFullScreen=true
from collections import defaultdict


# brute force approach using recursive causes timeout and system error (memory or recursive limit)
def check_result(lst, idx, cur, clst):
    if cur != 0 and cur%101 == 0:
        # current is already multiple of 101. Multiply the rest
        str_lst = map(lambda x: str(x), lst[idx:])
        st = '*'.join(str_lst)
        return clst + '*' + st
    if lst[idx]%101 == 0:
        lst1 = map(lambda x: str(x), lst[:idx])
        lst2 = map(lambda x: str(x), lst[idx:])
        return '+'.join(lst1) + '*' + '*'.join(lst2)

    if idx == len(lst) - 1:
        # last one
        if (lst[idx] + cur)%101 == 0 and (lst[idx] + cur) != 0:
            return clst + '+' + str(lst[idx])
        elif (cur - lst[idx])%101 == 0 and (cur - lst[idx]) != 0:
            return clst + '-' + str(lst[idx])
        else:
            return ''

    ret = check_result(lst, idx + 1, cur + lst[idx], clst + '+' + str(lst[idx]))
    if not ret:
        ret = check_result(lst, idx + 1, cur - lst[idx], clst + '-' + str(lst[idx]))
        if not ret:
            ret = check_result(lst, idx + 1, cur * lst[idx], clst + '*' + str(lst[idx]))

    return ret


def check(lst):
    ret = check_result(lst, 1, lst[0], str(lst[0]))
    return ret


# The trick here is that we just need to keep track of the remainder.

def check1(lst):
    d = defaultdict(list)

    d[lst[0]%101] = str(lst[0])

    for i in lst[1:]:
        t = defaultdict(list)
        for e in d:
            t[(e + i)%101] = d[e] + '+' + str(i)
            t[(e - i)%101] = d[e] + '-' + str(i)
            t[(e * i)%101] = d[e] + '*' + str(i)

        d = t

    return d[0]

if __name__ == '__main__':
    # lst = [1]*100
    # lst.append(2)
    # lst.extend([1]*100)
    # lst.append(2)
    # lst.extend([1] * 50)
    lst = [22, 79, 21]

    print(check1(lst))



