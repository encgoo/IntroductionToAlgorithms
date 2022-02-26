# use partition

def partition(lst, s, e):
    p_pos = s
    p_val = lst[s]

    idx = s + 1
    while idx < e:
        if lst[idx] < p_val:
            p_pos += 1
            lst[idx], lst[p_pos] = lst[p_pos], lst[idx]
        idx += 1

    lst[p_pos], lst[s] = lst[s], lst[p_pos]

    return p_pos


def q_sort(lst, s, e):
    if s >= e:
        return

    p_pos = partition(lst, s, e)
    q_sort(lst, s, p_pos)
    q_sort(lst, p_pos + 1, e)

if __name__ == '__main__':
    lst = [4,5,3,7,2]
    q_sort(lst, 0, len(lst))
    print(lst)

