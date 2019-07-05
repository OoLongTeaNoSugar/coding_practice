# -*- coding:utf-8 -*-
"""
Q: 在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。

A: 长度为n的数组里，所有数字的范围都在[0,n-1]中。查重的话，可以首先对数组进行排序，然后遍历数组查找重复的数字，事件复杂度为O(nlogn)，或者建立一个哈希表，这样在O(n)的时间内查找到，但是需要O(n)的额外空间。因为数字在[0,n-1]中，如果数字没有重复，那么数组排序后数字i 将出现在index为i 的位置。存在重复的话，位置i 出现的数字就可能不是i。所以可以重排数组，从头到尾扫描所有数字，如果位置i 的数字不是i，就和位置i 的数字交换，交换后还不是，就继续交换，直到位置i 的数字为i。 如果在交换过程中，需要交换的数字，在相应位置已经存在，则该数字为重复数字，记录该数字，然后继续扫描。
"""
class Solution:
    def duplicate(self, numbers, duplication):
        # write code here
        # duplication是一数组，将重复数字复制到duplication[0]上
        # 边界情况
        if len(numbers) < 0 or not numbers:
            return False
        for i in numbers:
            if i < 0 or i > numbers:
                return False
        # 对数组遍历
        for i in range(len(numbers)):
            # i == numbers[i]：不需讨论
            while i != numbers[i]:
                # 下面情况说明已经存在重复数字
                if numbers[i] == numbers[numbers[i]]:
                    # 记录重复数字
                    duplication[0] = numbers[i]
                    return True
                else:
                    # 不相同的情况就交换两个位置的数字
                    idx = numbers[i]
                    numbers[idx], numbers[i] = numbers[i], numbers[idx]
        return False
    
