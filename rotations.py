#!/bin/python3

import math
import os
import random
import re
import sys

from collections import deque

# Complete the rotLeft function below.
def rotLeft(a, d):
    
    q = deque()
    for i in a:
        q.append(i)
        
    while d > 0:
        temp = q.popleft()
        q.append(temp)
        d-=1
    
    a = list(q)
         
    return a
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
