# -*- coding:utf-8 -*-
"""
Q: LL今天心情特别好,因为他去买了一副扑克牌,发现里面居然有2个大王,2个小王(一副牌原本是54张^_^)…他随机从中抽出了5张牌,想测测自己的手气,看看能不能抽到顺子,如果抽到的话,他决定去买体育彩票,嘿嘿！！“红心A,黑桃3,小王,大王,方片5”,“Oh My God!”不是顺子…..LL不高兴了,他想了想,决定大\小 王可以看成任何数字,并且A看作1,J为11,Q为12,K为13。上面的5张牌就可以变成“1,2,3,4,5”(大小王分别看作2和4),“So Lucky!”。LL决定去买体育彩票啦。 现在,要求你使用这幅牌模拟上面的过程,然后告诉我们LL的运气如何， 如果牌能组成顺子就输出true，否则就输出false。为了方便起见,你可以认为大小王是0。

A: 把这5张牌组成的顺子看成数组，所以先对数组排序，然后求出大小王 即0的个数，然后除去0之外的数字，求出在数组中的数字间隔，然后比较间隔和0的个数，如果出现成对的，肯定不是顺子，再求间隔的时候需要鉴别。

"""
class Solution:
    def IsContinues(self, numbers):
        '''
        # 思路较为清楚，对排序后的数组计算0的个数，然后计算间隔，若相等则true
        :param numbers:
        :return:
        '''

        # 先把A，J，K，Q转换成数字
        transfom = {
            'A' : 1,
            'J' : 11,
            'Q' : 12,
            'K' : 13
        }
        for i in range(len(numbers)):
            if numbers[i] in transfom.keys():
                numbers[i] = transfom[numbers[i]]

        # 排序
        numbers = sorted(numbers)

        # 计算0的个数
        count0 = 0
        for i in range(len(numbers)):
            if numbers[i] == 0:
                count0 += 1
        '''
        i = 0
        while i < len(numbers) and numbers[i] == 0:
            count0 += 1
            i += 1
        '''

        # 计算间隔数
        zero_gap = 0
        left = count0
        right = left + 1
        while right < len(numbers):
            if numbers[left] == numbers[right]:
                return False
            zero_gap += numbers[right] - numbers[left] - 1
            left = right
            right += 1

        return False if zero_gap > count0 else True