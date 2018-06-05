#!/bin/python3

import sys

def miniMaxSum(arr):
    arr.sort()
    max1=sum(arr[1:len(arr)])
    min1=sum(arr[0:len(arr)-1])
    print(min1,max1)

if __name__ == "__main__":
    arr = list(map(int, input().strip().split(' ')))
    miniMaxSum(arr)

