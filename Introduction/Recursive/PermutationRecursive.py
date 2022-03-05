def pick_one(lst):
    if len(lst) == 1:
        print(lst[0])
        return

    for i in lst:
        lst1 = list(lst)
        print(i, end=',')
        lst1.remove(i)
        pick_one(lst1)

if __name__ == '__main__':
    pick_one([1,2,3,45])