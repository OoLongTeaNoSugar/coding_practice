# -*- coding:utf-8 -*-
"""
Q: 汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，就是用字符串模拟这个指令的运算结果。对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。是不是很简单？OK，搞定它！

A:经过三次翻转实现
例如：s ='abcdefg' n = 3
首先，翻转（0, n-1）s = 'cbadefg'
第二步，翻转(n, len(s)-1) s = 'cbagfed'
第三步：翻转所有, s = 'defgabc'
complete
"""
class Solution:
    def LeftRotatingstr(self, s, n):
        if not s or not n or len(s) < n:
            return ''
        # 一定要做list处理
        s = list(s)
        self.Reverse(s, 0, n - 1)
        self.Reverse(s, n, len(s) - 1)
        self.Reverse(s, 0, len(s) - 1)
        # 最后用join直接输出str
        return ''.join(s)

    def Reverse(self, s, l, r):
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -=1
