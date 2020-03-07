#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    binary=bin(n).replace("0b","")
    result=re.findall('[1]{1,100}',str(binary))
    result.sort()
    num=0
    for i in result[-1]:
        num+=int(i)
    print(num)