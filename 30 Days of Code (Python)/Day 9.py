#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)

if __name__ == '__main__':
    n = int(input())
    if n>=2 and n<=12:
        result = factorial(n)
        print(str(result) + '\n')
