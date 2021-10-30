#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):

    arr_length = len(arr)

    if arr_length == 0:
        print("0.000000\n0.000000\n0.000000")
        return

    positive_counter = 0
    negative_counter = 0
    zero_counter = 0

    for member in arr:
        if member == 0:
            zero_counter += 1
        elif member > 0:
            positive_counter += 1
        elif member < 0:
            negative_counter += 1

    print("%.6f" % (positive_counter/arr_length))
    print("%.6f" % (negative_counter/arr_length))
    print("%.6f" % (zero_counter/arr_length))



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
