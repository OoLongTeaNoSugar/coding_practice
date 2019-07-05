# -*- coding:utf-8 -*-
"""
Q: 给定一个数组A[0,1,…,n-1],请构建一个数组B[0,1,…,n-1],其中B中的元素B[i]=A[0] A[1]…A[i-1] A[i+1]…A[n-1]。不能使用除法。

A: 把B[i]分成两部分， 一部分是A[0,…,i-1]的连乘，记为C[i]，一部分是A[i+1,…,n-1]的连乘，记为D[i]，所以，C[i]=C[i-1] A[i-1]， D[i]=D[i+1] A[i+1]。
"""
class Solution:
    def multiply(self, A):
        # 边界
        if not A or len(A) <= 0:
            return
        lenth = len(A)
        B = [1] * lenth
        # 先计算前i-1
        # B[i] = A[0]A[1]...A[i-1]
        for i in range(1, lenth):
            B[i] = B[i-1] * A[i-1]
        temp = 1
        # temp = A[i+1]...A[n-1]
        for i in range(lenth - 2, -1, -1): # 从倒数2位开始往前
            
            temp = temp * A[i+1]
            B[i] *= temp
        return B[i]
