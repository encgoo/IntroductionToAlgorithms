
def app_del(lst1, lst2, k):
    idx = 0
    while idx < len(lst1) and idx < len(lst2) and lst1[idx] == lst2[idx]:
        idx += 1

    dl = len(lst1) - idx
    ap = len(lst2) - idx

    if dl + ap > k:
        return 'No'
    elif ((dl+ap) - k)%2 == 0:
        return 'Yes'
    elif k > len(lst1) + len(lst2):
        # delete whole lst1 and rebuild lst2
        return 'Yes'
    return 'No'

if __name__ == '__main__':
    print(app_del('abc', 'def', 6))
    print(app_del('hackerhappy', 'hackerrank', 9))
