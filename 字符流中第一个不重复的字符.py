# -*- coding:utf-8 -*-
"""
Q:请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。
当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。


"""
class Solution:
    # 返回对应char
    def __init__(self):
        # 用一个字典来记录字符的出现次数
        self.dic = {}
        # 用一个队列来实现，比较第一个元素是否为1，若是则返回第一个元素；若不是，则弹出
        self.lst = []
    def FirstAppearingOnce(self):
        # write code here
        while len(self.lst) > 0 and self.dic[self.lst[0]] == 2:
            self.lst.pop(0)
        if len(self.lst) == 0:
            return '#'
        else:
            return self.lst[0]
    def Insert(self, char):
        # write code here
        if char not in self.dic.keys():
            self.dic[char] = 1
            self.lst.append(char)
        elif self.dic[char]:
            self.dic[char] = 2