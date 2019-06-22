# -*- coding:utf-8 -*-
"""
Q: HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。
今天测试组开完会后,他又发话了:在古老的一维模式识别中,
常常需要计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。
但是,如果向量中包含负数,是否应该包含某个负数,并期望旁边的正数会弥补它呢？
例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。
给一个数组，返回它的最大连续子序列的和，你会不会被他忽悠住？(子向量的长度至少是1)

A: 对于连续子数组，可以用一个数值来存储当前的和，
如果当前和小于0，那么在进行到下一个元素时，直接把当前和赋值为下一个元素，
如果当前和大于0，则累加下一个元素，同时用一个链表存储最大值并随时更新。
"""
class Solution:
    def FindGreatestSumOfSubArray(self, array):

        '''

        :param array:
        :return:
        '''
        if not array:
            return 0

        cur_sum = 0
        max_sum = array[0]

        for i in range(len(array)):
            if cur_sum <= 0:
                cur_sum = array[i]
            else:
                cur_sum += array[i]

            if cur_sum > max_sum:
                max_sum = cur_sum

        return max_sum
