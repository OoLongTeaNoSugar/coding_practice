# -*- coding:utf-8 -*-
"""
Q: 输入一个正整数数组，把数组里所有数字拼接起来排成一个数，
打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，
则打印出这三个数字能排成的最小数字为321323。

A: 将数组中的数字全部转换成字符串存储在一个新的数组中，
然后比较每两个数字串的拼接的mn和nm的大小，
如果mn小于nm，则m更小，反之n更小。
然后把小的数放入一个新的列表中输出。
"""
class Solution:
    def PrintMinNumber(self, numbers):
        if not numbers:
            return ''

        # Q1:为什么转换成字符串
        # A1:字符串可以前后直接加减，方便操作
        nums = [str(m) for m in numbers]

        # i的取值是前n-1个数字，j的取值是i后面所有元素
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                # 如果mn大于nm，m和n互换位置
                if nums[i] + nums[j] > nums[j] + nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]

        return ''.join(nums)
