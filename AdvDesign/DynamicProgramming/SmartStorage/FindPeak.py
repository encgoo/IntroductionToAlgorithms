def find_peak(lst):
    if len(lst) == 0:
        return -1

    j = 1
    while j < len(lst) and lst[j-1] <= lst[j]:
        j += 1

    return j - 1

if __name__ == '__main__':
    print(find_peak([1,2,3,1,8, 2]))