# -*- coding:utf-8 -*-
"""
Q: 小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!

A: 设定两个指针分别指向数字1和数字2，并设为small和big，求和，如果大于s，则删除small并把small加1，如果小于s，则把big加1，并加入和中。如果等于目标值，就输出small到big的序列，同时把big加1，并加入和中，继续之前操作。

"""
class Solution:
    def FindContinueSequence(self, tsum):
        # write code here
        small, big = 1, 2
        res = []
        csum = small + big
        while small < big:
            if csum > tsum:
                csum -= small
                small += 1
            elif csum == tsum:
                res.append([i for i in range(small, big + 1)])
            else:
                big += 1
                csum += big
        return res