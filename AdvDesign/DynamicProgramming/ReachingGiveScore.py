# stairs problem
# changes problem
# game scores problem

# when we are looking for how many ways, need to use DP. When we find the minimum count, we use Greedy(?)

# Coin change problem. Assume 3, 5, 10


def find_ways(amt, coins):
    ways = [0]*(amt+1)

    ways[0] = 1

    c = coins[0]

    for i in range(c, amt + 1, c):
        ways[i] += ways[i - c]

    for j in range(1, len(coins)):
        c = coins[j]
        for i in range(c, amt + 1):
            ways[i] += ways[i-c]

    return ways[amt]

if __name__ == '__main__':
    print(find_ways(10, [2,3,5]))