from collections import defaultdict
import time

def defValue():
    return None

# brute force approach has timeout failures as expected.
def finalWin(lst):
    count = 0
    adj = False
    lastBin = False

    for c in lst:
        if c == 'I':
            count += 1
            if lastBin:
                adj = True
            lastBin = True
        else:
            lastBin = False

    if count == 1 or (count == 2 and adj):
        return True
    elif count == 2:
        return False
    else:
        return False

def isWinning(lst, playing):
    # When there are less than 2 pins, it is determined
    if lst.count('I') <= 2:
        return playing == finalWin(lst)

    if playing:
        ret = False
    else:
        ret = True
    for i in range(len(lst)):
        # knock down a pin
        if lst[i] == 'I':
            nlst = lst[:i] + 'X' + lst[i+1:]
            if playing:
                ret = ret or isWinning(nlst, not playing)
            else:
                ret = ret and isWinning(nlst, not playing)
        if i < len(lst) - 1 and lst[i+1] == 'I':
            # knock down two adjacent pins
            nlst = lst[:i] + 'XX' + lst[i+2:]
            if playing:
                ret = ret or isWinning(nlst, not playing)
            else:
                ret = ret and isWinning(nlst, not playing)

    return ret


# DP with memorization. Performance improved by memorization, but not enough to pass all tests.

# some configs are the same, so we simplify it.
# for example XXXIXXXIXXXX is the same as IXI
def simplify(config):
    # remove leading and trailing X's
    ret = ''
    first_I = False
    last_X = False
    s = 0
    while s < len(config):
        # no more I, then break
        rest = config[s:]
        if rest.count('I') == 0:
            break
        if config[s] == 'I':
            # always copy I
            ret += 'I'
            first_I = True
            last_X = False
        else:
            # for X, depends
            if first_I and not last_X:
                ret += 'X'
            last_X = True

        s += 1

    return ret

def isWinning2(lst, playing, d):
    # When there are less than 2 pins, it is determined
    if lst.count('I') <= 2:
        return playing == finalWin(lst)

    slst = simplify(lst)

    if d[slst] is not None:
        return playing == d[slst]

    if playing:
        ret = False
    else:
        ret = True
    for i in range(len(slst)):
        # knock down a pin
        if slst[i] == 'I':
            nlst = slst[:i] + 'X' + slst[i+1:]
            if playing:
                ret = ret or isWinning2(nlst, not playing, d)
            else:
                ret = ret and isWinning2(nlst, not playing, d)
        if i < len(slst) - 1 and slst[i+1] == 'I':
            # knock down two adjacent pins
            nlst = slst[:i] + 'X' + slst[i+2:]
            if playing:
                ret = ret or isWinning2(nlst, not playing, d)
            else:
                ret = ret and isWinning2(nlst, not playing, d)
    d[slst] = ret
    if not playing:
        d[lst] = not ret
    return ret


if __name__ == '__main__':
    lst = 'XXXXIIXIXIXIIXXIIIIXXXX'
    t1 = time.time()
    d = defaultdict(defValue)
    print(isWinning2(lst, True, d))
    t2 = time.time()
    print(t2-t1)
    print(isWinning(lst, True))
    t3 = time.time()
    print(t3-t2)
