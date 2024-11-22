import math

from math import inf

def divide(first, second):
    if int(second) == 0:
        return inf
    else:
        res = int(first) / int(second)
        return res