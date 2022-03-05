from collections import deque


def simplify(path):

    flds = path.split('/')
    q = deque()
    for fld in flds:
        if fld != '..':
            if fld != '.' and fld != '':
                q.append(fld)
        else:
            if q:
                q.pop()

    if q:
        ret = ''
        while q:
            ret += '/'
            f = q.popleft()
            ret += f

        return ret
    else:
        return '/'

if __name__ == '__main__':
    print(simplify('/home/'))
    print(simplify('/a///./b/../../c/'))
    print(simplify('/../'))
    print(simplify('/home//foo/'))