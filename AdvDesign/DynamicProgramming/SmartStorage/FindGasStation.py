# stations in a loop. Each can get a_i gas. Cost between them is bi
# find _a_ station that a car can start with and finish the loop

# brute force approach is just to try to start from each station, until find one. Theoretically this is O(n^2)
# this approach stores total. Whenever total goes to negative, we stop.

# DP stores information smartly to do it in O(n). It continues even if total is already negative. It uses
# an other accumulator sum_r. When this goes to negative, it will reset itself to 0 and the start station


def find_station(g, c):
    # start from 0
    s = 0
    total = sum(g) - sum(c)
    sum_r = 0

    for i in range(len(g)):
        remaining = g[i] - c[i]

        if sum_r >= 0:
            # still good
            sum_r += remaining
        else:
            sum_r = remaining
            s = i

    if total >= 0:
        return s
    else:
        return -1

if __name__ == '__main__':
    g = [1, 2, 3]
    c = [2,2,2]
    print(find_station(g, c))
