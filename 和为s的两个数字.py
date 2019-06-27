# -*- coding:utf-8 -*-
"""
Q: 输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。

A: 两个指针，一个指向起点，一个指向终点，然后对两个数字求和，如果大于s，则前移后一个指针，如果小于s，则把前一个指针后移。

"""
class Solution:
    def Find2NumberwithSum(self, array, tsum):
        if not array or not tsum:
            return []
        start = 0
        end = len(array) - 1
        csum = array[start] + array[end]
        while start < end:
            if csum < tsum:
                csum -= array[start]
                start += 1
                csum += array[start]
            else:
                if csum == tsum:
                    return [array[start], array[end]]
                csum -= array[end]
                end -= 1
                csum += array[end]
        return []