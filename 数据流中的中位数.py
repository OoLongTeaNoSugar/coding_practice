# -*- coding:utf-8 -*-
"""
Q: 如何得到一个数据流中的中位数？
如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。

A: 构建一个最大堆，一个最小堆，分别存储比中位数小的数和大的数。
当两个堆的总数为偶数时，把数字存入最大堆，然后重排最大堆，
如果最大堆堆顶的数字大于最小堆堆顶的数字，则交换，然后重排两个堆。
此时两个堆总数为奇数，输出最大堆堆顶的数字；
当两个堆总数为奇数时，把数字存入最小堆，重排最小堆，
如果最大堆堆顶数字大于最小堆堆顶的数字，则交换，重排两个堆，
此时两堆总是为偶数，输出两堆堆顶的数字的平均值。
"""
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.left = []
        self.right = []
        self.count = 0
    def Insert(self, num):
        # 输入的时候就分成两堆
        if self.count & 1 == 0:
            self.left.append(num)
        else:
            self.right.append(num)
        self.count += 1

    def GetMedian(self, x):
        if self.count == 1: # 如果只有一个数字
            return self.left[0]
        # 最大堆储存比中位数小的数字，最小堆储存比中位数大的数字
        self.MaxHeap(self.left) # 最大堆排序
        self.MinHeap(self.right)
        if self.left[0] > self.right[0]:
            self.left[0], self.right[0] = self.right[0], self.left[0]
        self.MaxHeap(self.left)
        self.MinHeap(self.right)
        if self.count & 1 == 0: # 总数为偶数
            return (self.left[0] + self.right[0])/2.0
        else:
            return self.left[0]

    def MaxHeap(self, alist):
        length = len(alist)
        if alist == None or length <= 0:
            return
        if length == 1:
            return alist
        for i in range(length//2-1, -1, -1):
            k = i; temp = alist[k]; heap = False
            while not heap and 2*k < length-1:
                index = 2*k+1
                if index < length - 1:
                    if alist[index] < alist[index + 1]: index += 1
                if temp >= alist[index]: heap = True
                else:
                    alist[k] = alist[index]
                    k = index
            alist[k] = temp

    def MinHeap(self, alist):
        length = len(alist)
        if alist == None or length <= 0:
            return
        if length == 1:
            return alist
        for i in range(length//2-1, -1, -1):
            k = i; temp = alist[k]; heap = False
            while not heap and 2 * k < length - 1:
                index = 2 * k+1
                if index < length - 1:
                    if alist[index] > alist[index + 1]: index += 1
                if temp <= alist[index]:
                    heap = True
                else:
                    alist[k] = alist[index]
                    k = index
            alist[k] = temp
