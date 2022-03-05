
from collections import defaultdict


def default_val():
    return None


def check(pattstr, str_):
    patts = list(pattstr)
    ws = str_.split(' ')
    assert len(patts) == len(ws)

    dict_ = defaultdict(default_val)

    ret = True
    for i in range(len(ws)):
        patt = patts[i]
        if dict_[patt] is None:
            dict_[patt] = ws[i]
        else:
            if dict_[patt] != ws[i]:
                ret = False
                break

    return ret


if __name__ == '__main__':
    print(check('ababbcbc', 'cat dog cat dog dog fish dog fish'))
