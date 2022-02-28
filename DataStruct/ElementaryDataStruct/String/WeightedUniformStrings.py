import time


def wus(lst, arr):
    m = {}
    for i in range(26):
        m[chr(i + 97)] = i + 1

    # use a set instead of an array
    sw = set()
    sw.add(m[lst[0]])
    cnt = 1
    ind = 1
    n = len(lst)
    while ind < n:
        if lst[ind] != lst[ind - 1]:
            # new char
            sw.add(m[lst[ind]])
            cnt = 1
        else:
            cnt += 1
            sw.add((m[lst[ind]]) * cnt)

        ind += 1

    ret = []

    for i in arr:
        if i in sw:
            ret.append('Yes')
        else:
            ret.append('No')

    return ret


if __name__=='__main__':

    lst = 'abbcccddddd'
    q = [1,7,5,4,15,2,6,9,7,8,10,11,101,102, 1,1,1,1,1,1,1,1,1,11,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,22,2,2,2,2,2,22,2]

    t1 = time.time()
    print(wus(lst, q))
    t2 = time.time()
    print(t2 - t1)
