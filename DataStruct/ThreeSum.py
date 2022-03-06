from collections import defaultdict


def def_val():
    return 0


def three_sum(lst, n):
    d = defaultdict(def_val)

    for v in lst:
        d[v] += 1
    ret = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            a = lst[i]
            b = lst[j]
            needed = n - a - b
            if a == needed and b == needed:
                if d[needed] >= 3:
                    l = [a,a,a]
                    if not l in ret:
                        ret.append([a, a, a])
            elif a == needed or b == needed:
                if d[needed] >= 2:
                    l = sorted([a, b, needed])
                    if not l in ret:
                        ret.append(sorted([a, b, needed]))
            elif d[needed] >=1:
                l = sorted([a, b, needed])
                if not l in ret:
                    ret.append(sorted([a, b, needed]))

    return ret


if __name__ == '__main__':
    lst = [-1, 0, 1, 2, -1, -4]
    print(three_sum(lst, 0))

