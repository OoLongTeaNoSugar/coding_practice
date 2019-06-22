# -*- coding:utf-8 -*-
"""
Q: 输入n个整数，找出其中最小的K个数。
例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。

A: 第一种思路：基于划分的方法，使比第k个数字小的数都位于数组的左边，大的位于数组右边。
第二种思路：基于二叉树或堆。首先把前k个数字构建一个堆，从第k+1个数字开始遍历，
遍历到的元素如果小于堆的最大元素，则交换，继续遍历到结束，最后剩下的就是最小的k个数。
"""
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        '''

        :param tinput:
        :param k:
        :return:
        '''
        if not tinput or k > len(tinput):
            return []
        tinput = self.QuickSort(tinput)
        return tinput[:k]


    def QuickSort(self, arr):
        '''

        :param arr:
        :return:
        '''
        if not arr:
            return []
        kval = arr[0]
        left = self.QuickSort([x for x in arr[1:] if x < kval])
        right = self.QuickSort([x for x in arr[1:] if x >= kval])
        return left + [kval] + right