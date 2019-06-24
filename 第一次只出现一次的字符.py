# -*- coding:utf-8 -*-
"""
Q: 在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置,
如果没有则返回 -1（需要区分大小写）.

A: 先遍历一遍字符串，用一个hash表存放每个出现的字符和字符出现的次数。
在遍历一遍字符串，找到hash值等于1的即可。
"""
class Solution:
    def FirstNotRepeatingChar(self, s):
        if not s:
            return -1

        # python中的字典是一种hash表
        # dict{keys: values}
        char_dict = {}

        for i in s:
            # 添加keys（i）
            if i not in char_dict.keys():
                char_dict[i] = 0
            # key值计数
            char_dict[i] += 1

        for i in s:
            if char_dict[i] == 1:
                return s.index(i)
                # 注意：python2.7版本的字典是无序的，python3.x是有序的

        return -1