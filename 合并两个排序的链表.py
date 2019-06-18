# -*- coding:utf-8 -*-
"""
Q: 输入两个单调递增的链表，输出两个链表合成后的链表，
当然我们需要合成后的链表满足单调不减规则。

A: 每个链表建立一个指针，合并时，比较头节点大小，小的作为合并后链表的头节点，
再比较剩余部分和另一个链表的头节点，取小的，然后一直循环此过程
"""

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        '''

        :param pHead1:有序链表
        :param pHead2: 有序链表
        :return: 合并后的链表

        '''
        if pHead1 == None:
            return pHead2
        '''
        如果其中一个链表为空时，头结点应该为另一个链表，故返回另一个链表；
        否则在合并后会产生丢失最后一个值的结果
        '''
        if pHead2 == None:
            return pHead1

        pMerge = None
        if pHead1.val < pHead2.val:
            pMerge = pHead1
            pMerge.next = self.Merge(pHead1.next, pHead2)

        else:
            pMerge = pHead2
            pMerge.next = self.Merge(pHead1, pHead2.next)

        return pMerge
