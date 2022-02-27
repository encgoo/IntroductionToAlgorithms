def bubble_sort(lst):

    n = len(lst)
    e = n - 1
    # don't need e = 0 because the last one must be automatically sorted
    while e > 0:
        j = 0
        # need e - 1 because we need to sway
        while j <= e - 1:
            if lst[j] > lst[j + 1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
            j += 1
        e -= 1

if __name__ == '__main__':
    lst = [1, 10,2,9, 3, 8, 4, 6, 5, 7]

    bubble_sort(lst)
    print(lst)
