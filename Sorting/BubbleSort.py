def bubble_sort(lst):

    n = len(lst)
    # when i = 0, it bubbles the max to the end
    # when i = 1, it bubbles the second max to the second last pos
    for i in range(n-1):
        for j in range(n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                print(lst)

if __name__ == '__main__':
    lst = [1,8,9,2]

    bubble_sort(lst)
    print(lst)
