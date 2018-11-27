# -*- coding=utf-8 -*-
from random import randint

"""
二分查找算法
"""

def binary_search(list, item):
    low = 0
    high = len(list)-1
    count = 0
    while low<=high:
        mid = int((low+high)/2)
        count = count+1
        guess = list[mid]

        # print(mid,guess)
        if guess == item:
            print('find %d times,get item %d' % (count,item))
            return mid
        if item>guess:
            low=mid+1
        else:
            high=mid-1    
    print("Can't find this item in list.")
    return None

# list = [1,3,5,7,9,10,15] 
# binary_search(list,3)
# binary_search(list,0)


def exercises_1():
    pass

