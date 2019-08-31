# -*- coding:utf-8 -*-
"""
Q: 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下4 X 4矩阵： [[1 2 3 4], [5 6 7 8], [9 10 11 12], [13 14 15 16]]
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.

A: 首先判断每一圈开始时的坐标点，是否小于行数的一半且小于列数的一半。
打印的时候从左到右打印，从上到下打印(至少两行)，从右到左打印(至少两行两列)，
从下到上打印四种情况(至少三行两列)。除了从左到右打印一定发生，其他三种情况都要判断发生条件。
"""


class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        if not matrix:
            return []

        rows = len(matrix)
        columns = len(matrix[0])
        start = 0
        result = []
        while rows > start * 2 and columns > start * 2:
            self.PrintMatrixInCircle(matrix, columns, rows, start, result)
            start += 1
        return result

    def PrintMatrixInCircle(self, matrix, columns, rows, start, result):
        endX = columns - 1 - start
        endY = rows - 1 - start

        # 从左到右打印一行
        for i in range(start, endX + 1):
            # number = matrix[start][i]
            result.append(matrix[start][i])

        # 从上到下打印一行
        if start < endY:
            for i in range(start + 1, endY + 1):
                # number = matrix[i][endX]
                result.append(matrix[i][endX])

        # 从右到左打印一行
        if start < endX and start < endY:
            for i in range(endX - 1, start - 1, -1):
                # number = matrix[endY][i]
                result.append(matrix[endY][i])

        # 从下到上打印一行
        if start < endX and start < endY - 1:
            for i in range(endY - 1, start, -1):
                # number = matrix[i][start]
                result.append(matrix[i][start])


def printMatrix(matrix):
    if not matrix:
        return []

    rows = len(matrix)
    columns = len(matrix[0])
    start = 0
    result = []
    while rows > start * 2 and columns > start * 2:
        PrintMatrixInCircle(matrix, columns, rows, start, result)
        start += 1
    return result

def PrintMatrixInCircle(matrix, columns, rows, start, result):
    endX = columns - 1 - start
    endY = rows - 1 - start

    # 从左到右打印一行
    for i in range(start, endX + 1):
        # number = matrix[start][i]
        result.append(matrix[start][i])

        # 从上到下打印一行
    if start < endY:
        for i in range(start + 1, endY + 1):
                # number = matrix[i][endX]
            result.append(matrix[i][endX])

        # 从右到左打印一行
    if start < endX and start < endY:
        for i in range(endX - 1, start - 1, -1):
                # number = matrix[endY][i]
            result.append(matrix[endY][i])

        # 从下到上打印一行
    if start < endX and start < endY - 1:
        for i in range(endY - 1, start, -1):
                # number = matrix[i][start]
            result.append(matrix[i][start])

if __name__ == "__main__":
    import sys
    m, n = map(int, sys.stdin.readline().strip().split())
    while m != -1 and n != -1:
        matrix = []
        i = 0
        while i < m:
            line = sys.stdin.readline().strip().split(' ')
            line = list(line)
            matrix.append(line)
            i += 1
        res = printMatrix(matrix)
        print(','.join(res))
        m, n = map(int, sys.stdin.readline().strip().split())
