# -*- coding: utf-8 -*-

"""
Q: 统计一个数字在排序数组中出现的次数。

A: 有序数组的元素查找，可以考虑二分查找。找到该数字在数组中第一次出现的位置和最后一次出现的位置即可。

"""
class Solution:
    def GetNumberOfk(self, data, k):
        if not data:
            return 0
        if self.GetFirstk(data, k) == -1 and self.GetLastk(data, k) == -1:
            return 0
        return self.GetLastk(data, k) - self.GetFirstk(data, k) + 1


    def GetFirstk(self, data, k):
        low = 0
        high = len(data) - 1
        while low <= high:
            mid = (low + high) // 2
            if data[mid] < k:
                low = mid + 1
            elif data[mid] > k:
                high = mid - 1
            else:
                #list只剩下一个元素或者前面没有k时返回当前mid
                if mid == low or data[mid - 1] != k:
                    return mid
                else:
                    high = mid - 1
        return -1

    def GetLastk(self, data, k):
        low = 0
        high = len(data) - 1
        while low <= high:
            mid = (low + high) // 2
            if data[mid] > k:
                high = mid - 1
            elif data[mid] < k:
                low = mid + 1
            else:
                if mid == low or data[mid + 1] != k:
                    return mid
                else:
                    low = mid + 1
        return -1
