# -*- coding:utf-8 -*-

"""
将正方形矩阵顺时针旋转90°
"""
def rotate(matrix):
    tr = 0
    tc = 0
    dr = len(matrix) - 1
    dc = len(matrix[0]) - 1
    while tr < dr:
        rotateEdge(matrix, tr, tc, dr, dc)
        tr += 1
        tc += 1
        dr -= 1
        dc -= 1


def rotateEdge(m, tr, tc, dr, dc):
    times = dc - tc
    tmp = 0
    i = 0
    while i != times:
        tmp = m[tr][tc + i]
        m[tr][tc + i] = m[dr - i][tc]
        m[dr - i][tc] = m[dr][dc - i]
        m[dr][dc - i] = m[tr + i][dc]
        m[tr + i][dc] = tmp
        i += 1

def printMatrix(ma):
    """python3
    效果：
    1 2 3
    4 5 6
    """
    for i in range(len(ma)):
        for j in range(len(ma[0])):
            print(ma[i][j], end= " ")
        print('\n', end="")

if __name__ == "__main__":
    matr = [[1,2,3], [4, 5, 6], [7, 8, 9]]
    printMatrix(matr)
    rotate(matr)
    printMatrix(matr)