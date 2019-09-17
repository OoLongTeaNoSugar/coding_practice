# -*- coding: utf-8 -*-
"""
堆排序
"""
def heapSort(array):
   if len(array) < 2:
       return
   for i in range(len(array)):
       heapInsert(array, i)

   heapsize = len(array) - 1
   swap(array, 0, heapsize)
   while heapsize > 0:
       heapify(array, 0, heapsize)
       heapsize -= 1
       swap(array, 0, heapsize)

def heapify(arr, index, size):
    left = index * 2 + 1
    while left < size:
        lagest = left + 1 if (left + 1 < size and arr[left+1] > arr[left]) else left
        lagest = lagest if arr[lagest] > arr[index] else index
        if lagest == index:
            break
        swap(arr, lagest, index)
        index = lagest
        left = index * 2 + 1

def heapInsert(arr, index):
    while arr[index] > arr[(index-1) >> 1]:
        swap(arr, index, (index-1) >> 1)
        index = (index-1) >> 1

def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

"""
内置heapSort
"""
import heapq
def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]

def walk(grid):
    n = len(grid)
    m = len(grid[0])
    for i in range(1, n):
        grid[i][0] += grid[i - 1][0]
    for j in range(1, m):
        grid[0][j] += grid[0][j - 1]
    for i in range(1, n):
        for j in range(1, m):
            grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

    return grid[n - 1][m - 1]



if __name__ == "__main__":
    # arr2 = [[1,3,1],
    #         [1,5,1],
    #         [4,2,1]]
    # print(walk(arr2))
    test = [2,3,4,1,7,9,6,8]
    heapSort(test)
    print(test)