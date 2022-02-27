# give a sorted list find the closest element

# a typical binary search


def get_closest(lst, s, e, m):
    if s + 1 == e and lst[e] >= m >= lst[s]:
        if lst[e] - m > m - lst[s]:
            return lst[s]
        return lst[e]

    mid = (s+e)//2

    if m > lst[mid]:
        return get_closest(lst, mid, e, m)

    return get_closest(lst, s, mid, m)


def find_closest(lst, m):
    n = len(lst)

    if m > lst[n-1]:
        return lst[n-1]
    elif m < lst[0]:
        return lst[0]

    return get_closest(lst, 0, n-1, m)

if __name__ == '__main__':
    lst = [1,3,5,7,10,11]
    print(find_closest(lst, 8))