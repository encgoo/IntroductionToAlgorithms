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


def candies(n, arr):
    if n == 0:
        return 0

    candy_kid = [0] * n
    # at least one candy for each kid
    num_candies_to_give = 1
    candy_kid[0] = num_candies_to_give

    for index in range(1, len(arr)):
        if arr[index] > arr[index - 1]:
            # need to give more candy
            num_candies_to_give += 1
        else:
            num_candies_to_give = 1
        candy_kid[index] = num_candies_to_give

    # reset
    num_candies_to_give = 1
    # init
    total_candies = candy_kid[-1]
    for index in range(len(arr) - 2, -1, -1):
        if arr[index] > arr[index + 1]:
            num_candies_to_give += 1
        else:
            num_candies_to_give = 1

        total_candies += max(candy_kid[index], num_candies_to_give)

    return total_candies

if __name__ == '__main__':
    #scrs = [2,4,2,6,1,9,8,7,2,1]
    scrs = [51,36,36,53,25,80]
    print(count_candies(scrs))
    print(candies(len(scrs), scrs))