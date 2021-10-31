#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
from typing import List


def hourglass_sum(arr: List[List[int]]) -> int:

    sum = -math.inf
    print("initial sum: %s" % sum)
    for rowIndex in range(0, 4):
        for colIndex in range(0, 4):
            local_sum = arr[rowIndex][colIndex] + arr[rowIndex][colIndex+1] + arr[rowIndex][colIndex+2] + \
            arr[rowIndex+1][colIndex+1] + \
            arr[rowIndex+2][colIndex] + arr[rowIndex+2][colIndex+1] + arr[rowIndex+2][colIndex+2]
            print("localsum: %s" % local_sum)
            sum = max(local_sum, sum)

    return sum


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglass_sum(arr)

    print(result)