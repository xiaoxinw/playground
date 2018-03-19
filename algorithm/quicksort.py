# coding: utf-8

import random


def partition(arr, left, right):
    privot_pos = left
    privot = arr[privot_pos]

    for i in range(left + 1, right + 1):
        if arr[i] < privot:
            privot_pos += 1
            if i != privot_pos:
                arr[privot_pos], arr[i] = arr[i], arr[privot_pos]

    arr[privot_pos], arr[left] = arr[left], arr[privot_pos]
    print(arr)
    return privot_pos


def quick_sort(arr, left, right):
    if left < right:
        position = partition(arr, left, right)
        quick_sort(arr, left, position - 1)
        quick_sort(arr, position + 1, right)


def run():
    arr = random.sample(range(1, 15), 10)
    print('Before sort...')
    print(arr)
    quick_sort(arr, 0, len(arr) - 1)
    print('After sort...')
    print(arr)


if __name__ == '__main__':
    run()
