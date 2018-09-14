#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    h = 'hackerrank'
    sc, hc = 0, 0
    while sc < len(s) and hc < len(h):
        if h[hc] == s[sc]:
            hc += 1
            sc += 1
        else:
            sc += 1
    return 'YES' if hc == len(h) else 'NO'
            
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
