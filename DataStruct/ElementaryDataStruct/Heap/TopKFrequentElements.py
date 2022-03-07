
from collections import defaultdict
from heapq import heappush
from heapq import heappop

def def_val():
    return 0

def top_k_frequent(lst, k):
    d = defaultdict(def_val)
    for i in lst:
        d[i] += 1

    top = []

    for item in d.items():
        heappush(top, (item[1], item[0]))
        if len(top) > k:
            heappop(top)

    return top

if __name__ == '__main__':
    lst = [1,2,9,8,3,1,1,1,5,5,2,2,2,8,8,8,8,8,2,101,1001]

    print(top_k_frequent(lst, 3))


