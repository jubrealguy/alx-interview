#!/usr/bin/python3

def pascal_triangle(n):
    arr = [1, 2, 1]
    for i in range(n):
        newArr = []
        newArr.append(1)
        for j in range(len(arr) - 1):
            newArr[j + 1] = arr[j] + arr[j + 1]
        newArr.insert(-1, 1)
        newArr = arr
        return newArr
