# "the sky is blue" -> "blue is sky the"


def reverse(lst, st, ed):
    i = st
    j = ed
    while j > i:
        lst[i], lst[j] = lst[j], lst[i]
        i += 1
        j -= 1


def reverse_word(str_):
    lst = list(str_)

    # first reverse everything
    reverse(lst, 0, len(lst) - 1)

    # scan words and reverse
    first_char = False
    s = 0
    for i in range(len(lst)):
        if not first_char and lst[i] != ' ':
            s = i
            first_char = True
        if first_char and lst[i] == ' ':
            first_char = False
            reverse(lst, s, i - 1)

    if lst[-1] != ' ':
        # reverse the last word
        reverse(lst, s, len(lst)-1)

    return ''.join(lst)


if __name__ == '__main__':
    str_ = "Don't ask what the country can do for you"
    print(reverse_word(str_))

