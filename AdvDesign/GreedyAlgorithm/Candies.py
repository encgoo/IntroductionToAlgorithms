#https://www.hackerrank.com/challenges/candies/problem?isFullScreen=true

# Greedy algorithm is used for optimization problems as well, especially when DP is overkill.
# Greedy algorithm makes the best choice at the moment or say local optimal choice.

# Greedy do not always give global optimal solution


def count_candies(scrs):
    candis = [0]*len(scrs)

    # start the first kid as 1 candy
    candis[0] = 1

    # forward scan
    for i in range(1, len(scrs)):
        if scrs[i] > scrs[i - 1]:
            candis[i] = candis[i-1] + 1
        else:
            candis[i] = 1

    # backward scan
    i = len(scrs) - 1
    # start the last one as 1
    candis[i] = max(candis[i], 1)
    i -= 1
    while i >= 0:
        if scrs[i] > scrs[i + 1]:
            candis[i] = max(candis[i], candis[i+1] + 1)
        else:
            candis[i] = max(candis[i], 1)
        i -= 1

    return sum(candis)


if __name__ == '__main__':
    scrs = [2,4,2,6,1,9,8,7,2,1]
    print(count_candies(scrs))
