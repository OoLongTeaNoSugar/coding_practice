# -*- coding:utf-8 -*-
"""
Q: 牛客最近来了一个新员工Fish，每天早晨总是会拿着一本英文杂志，写些句子在本子上。
同事Cat对Fish写的内容颇感兴趣，有一天他向Fish借来翻看，但却读不懂它的意思。
例如，“student. a am I”。后来才意识到，这家伙原来把句子单词的顺序翻转了，正确的句子应该是“I am a student.”。
Cat对一一的翻转这些单词顺序可不在行，你能帮助他么？

A: 思路一：遍历根据空格得到list，然后再按倒序join

"""
class Solution:
    def ReverseSentence1(self, s):
        if not s or len(s) == 0:
            return ''
        return " ".join(s.split('')[::-1])

    def ReverseSentence2(self, s):
        '''
        思路二：
        先把输入的字符串完全翻转，从前往后依次遍历新字符串，
        遇到空格，就把空格前的字符串翻转，添加空格，继续遍历，
        遍历到结尾的时候，因为最后一个字符串后没有空格，所以最后要再翻转它。
        :param s:
        :return:
        '''
        if not s or len(s) == 0:
            return ''
        lst = list(s)
        lst_r = self.Reverse(lst)
        start = 0
        end = 0
        res = ''

        while end < len(s):
            if end == len(s) - 1:
                # 遍历到最后，翻转并加入res
                res.join(self.Reverse(lst_r[start:]))
                break
            if lst_r[start] == ' ':
                # 头指针是空格时，跳过；两个指针同时加一，添加空格
                start += 1
                end += 1
                # 添加空格
                res.join(' ')
            elif lst_r[end] == ' ':
                # end指针是空格时，表明读到一个单词。
                # 翻转添加
                res.join(self.Reverse(lst_r[start:end]))
                # 头指针移到尾指针处，继续遍历
                start = end
            else:
                # 尾指针向右移
                end += 1

        return res


    def Reverse(self, s):
        if not s or len(s) == 0:
            return ''
        l = 0
        r = len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

        return s