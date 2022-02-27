
# The quick sort algorithm offers a quick way to find the nth element


def partition(lst, s, e):
    p_val = lst[s]
    p_pos = s

    ind = s
    while ind < e:
        if lst[ind] < p_val:
            p_pos += 1
            lst[ind], lst[p_pos] = lst[p_pos], lst[ind]
        ind += 1

    lst[s], lst[p_pos] = lst[p_pos], lst[s]

    return p_pos


def find_median(lst):
    # len is odd
    mid = int(len(lst)/2)

    s = 0
    e = len(lst)
    p = partition(lst, s, e)
    while p != mid:
        if p > mid:
            p = partition(lst, s, p)
        else:
            p = partition(lst, p + 1, e)

    return lst[p]

# Note that the built-in sorted function might be implemented in C++
# so it is faster than what implemeted in python
def find_median_built_in(lst):
    arr = sorted(lst)
    return arr[len(arr)//2]

if __name__ == '__main__':
    lst = [5,3,6, 1,2,4,7]
    print(find_median(lst))

