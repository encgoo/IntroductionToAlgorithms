

def find_w(mtx, i, j, wrd, l, visited):
    num_r = len(mtx)
    num_c = len(mtx[0])

    if i < 0 or j < 0 or i >= num_r or j >= num_c or visited[i][j]:
        return False
    if mtx[i][j] != wrd[l]:
        return False

    if l == len(wrd) - 1:
        # last char
        return True

    visited[i][j] = True

    ret = find_w(mtx, i + 1, j, wrd, l + 1, visited)
    ret = ret or find_w(mtx, i - 1, j, wrd, l + 1, visited)
    ret = ret or find_w(mtx, i, j + 1, wrd, l + 1, visited)
    ret = ret or find_w(mtx, i, j - 1, wrd, l + 1, visited)

    return ret


def find_word(mtx, wrd):
    num_r = len(mtx)
    num_c = len(mtx[0])

    found = False
    for i in range(num_r):
        for j in range(num_c):
            visited = [[False] * num_c for _ in range(num_r)]
            found = find_w(mtx, i, j, wrd, 0, visited)
            if found:
                break
        if found:
            break

    return found


if __name__ == '__main__':
    mtx = ['ABCE',
           'SFCS',
           'ADEE']
    print(find_word(mtx, 'ABCCED'))
    print(find_word(mtx, 'SEE'))
    print(find_word(mtx, 'ABCB'))