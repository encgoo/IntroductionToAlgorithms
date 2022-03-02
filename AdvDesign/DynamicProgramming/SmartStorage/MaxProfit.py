
import sys
# brutal approach is O(n^2)
def max_profit(prs):
    max_ = 0
    for i in range(len(prs) - 1):
        for j in range(i+1, len(prs)):
            max_ = max(max_, prs[j] - prs[i])

    return max_


# DP stores min_ as well
def profit_max(prs):
    max_ = 0
    min_ = sys.maxsize

    for i in range(1, len(prs)):
        min_ = min(min_, prs[i])
        max_ = max(max_, prs[i] - min_)

    return max_

if __name__ == '__main__':
    prs = [10, 7, 5, 8, 11, 9]
    print(max_profit(prs))
    print(profit_max(prs))



