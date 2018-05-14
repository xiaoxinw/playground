# coding: utf-8

from __future__ import division


def binary_search(arr, x):
    '''
    Search given item x in a sorted array.
    '''
    if not arr:
        return -1
    left = 0
    right = len(arr) - 1
    middle = left + (right - left) // 2   # note this line.

    while middle >= 0 and middle < len(arr):
        if arr[middle] < x:
            left = middle + 1
            middle = left + (right - middle) // 2
        elif arr[middle] > x:
            right = middle - 1
            middle = left + (right - middle) // 2
        else:
            return middle

    return -1


def test_binary_search():
    arr = []
    x = 5
    answer = binary_search(arr, x)
    assert answer == -1

    arr = range(10)
    answer = binary_search(arr, x)
    assert answer == 5

    x = -5
    answer = binary_search(arr, x)
    assert answer == -1

    x = 15
    answer = binary_search(arr, x)
    assert answer == -1


if __name__ == '__main__':
    test_binary_search()
