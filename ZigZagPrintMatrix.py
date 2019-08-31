# -*- coding:utf-8 -*-
##############
# zigzag 打印矩阵

def printlevel(m, tr, tc, dr, dc, flag):
    if flag:
        while tr != (dr + 1):
            print(m[tr][tc])
            tr += 1
            tc -= 1
    else:
        while dr != tr - 1:
            print(m[dr][dc])
            dr -= 1
            dc += 1

def printMatrixZigZag(matrix):
    tr = 0
    dr = 0
    tc = 0
    dc = 0
    endR = len(matrix) - 1
    endC = len(matrix[0]) - 1
    fromup = False
    while tr != endR + 1:
        printlevel(matrix, tr, tc, dr, dc, fromup)
        tr = tr + 1 if tc == endC else tr
        tc = tc if tc == endC else tc + 1
        dc = dc + 1 if dr == endR else dc
        dr = dr if dr == endR else dr + 1
        fromup = not fromup

if __name__ == "__main__":
    ma = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    printMatrixZigZag(ma)