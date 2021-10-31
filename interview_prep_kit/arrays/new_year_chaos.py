#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimum_bribes(q):
    bribe_count = 0

    candidates = [1, 2, 3]
    for member in q:
        if member not in candidates:
            print("Too chaotic")
            return

        bribe_count += candidates.index(member)
        candidates.remove(member)
        candidates.append(max(member, candidates[-1]) + 1)

    print(bribe_count)


# Write your code here

if __name__ == '__main__':
    # t = int(input().strip())

    # for t_itr in range(t):
    #     n = int(input().strip())
    #
    #     q = list(map(int, input().rstrip().split()))

    minimum_bribes([2, 1, 5, 3, 4])
