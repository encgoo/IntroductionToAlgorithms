
def print_lst(lst):
    print(' '.join(map(lambda x:str(x), lst)))


def insert_last(lst, e):
    i_val = lst[e]

    ind = e - 1
    while ind >=0 and lst[ind] > i_val:
        lst[ind + 1] = lst[ind]
        ind -= 1

    lst[ind + 1] = i_val
    print_lst(lst)


def insert_sort(lst):
    n = len(lst)
    idx = 1
    while idx < n:
        insert_last(lst, idx)
        idx += 1


if __name__ == '__main__':
    lst = [3,2,1,5,6,9, 8]
    insert_sort(lst)
    print(lst)
