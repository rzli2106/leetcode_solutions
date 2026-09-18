#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    maximum = max(arr)
    minimum = min(arr)
    arrsum = 0
    for num in arr:
        arrsum += num
    minSum = arrsum - maximum
    maxSum = arrsum - minimum
    print(f'{minSum} {maxSum}')
    
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
