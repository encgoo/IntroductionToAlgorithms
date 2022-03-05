
from heapq import heappush
from heapq import heappop


def get_modified(n, upds):
    st = []
    en = []

    for u in upds:
        heappush(st, (u[0], u[2]))
        heappush(en, (u[1], u[2]))

    acc = 0
    ret = []
    for i in range(n):
        while len(st) > 0 and st[0][0] <= i:
            s = heappop(st)
            acc += s[1]

        while len(en) > 0 and en[0][0] < i:
            e = heappop(en)
            acc -= e[1]

        ret.append(acc)

    return ret

if __name__ == '__main__':
    n = 5
    uds = [
        [1, 3, 2],
        [2, 4, 3],
        [0, 2, -2]
    ]

    print(get_modified(n, uds))