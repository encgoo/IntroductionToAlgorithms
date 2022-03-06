# given a list of integer, find two that can sum up to an given number

# the key point here is to use a dict
from collections import defaultdict


def def_val():
    return None


def find_two(lst, n):
    d = defaultdict(def_val)
    for i in range(len(lst)):
        d[lst[i]] = i

    for i, v in enumerate(lst) :
        if d[n-v]:
            return [i+1, d[n-v]+1]

    return None

if __name__ == '__main__':
    lst = [2,7,11,15,100,101]
    print(find_two(lst, 26))

