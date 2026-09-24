#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    for i in range(n):
        line = ''
        spaces = ' ' * (n - (i + 1))
        hashes = '#' * (i+1)
        line += spaces + hashes
        print(line)

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
