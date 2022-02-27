# To get uniform random permutation, we need an uniform random function

# Random(0,1) generate 0 or 1 according to a uniform distribution.
# Use Random(0, 1) to generate Random(a, b). Here a and b are two integers and b > a. Random(a, b) needs to generate
# all the integers between a and b according to a uniform distribution

import math
import random


def random_between(a, b):
    bits = math.ceil(math.log2(b - a + 1))

    ret = 0
    while True:
        number = random_bits(bits)

        if a + number <= b:
            ret = a + number
            break

    return ret


def random_bits(bits):
    n = 0

    for i in range(bits):
        n = n*2 + random.randint(0, 1)

    return n


if __name__ == '__main__':
    total = 2000
    a = 10
    b = 15
    acc = [0]*(b-a+1)

    for i in range(total):
        n = random_between(a, b)
        acc[n-a] += 1

    prob = list(map(lambda x:x/float(total), acc))
    print(prob)





