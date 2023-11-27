import math
import os
import random
import re
import sys
def solve(s):
    lst = s.split()
    for i in range(len(lst)):
        if lst[i].isalpha():
            k = s.replace(lst[i], lst[i].capitalize())
            s = k
        else:
            pass
    return s
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()