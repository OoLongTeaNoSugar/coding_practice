# -*- coding:utf-8 -*-
"""
Q: 输入两个链表，找出它们的第一个公共结点。

A: 首先依次遍历两个链表，记录两个链表的长度m和n，
假设m>n，就先让长的链表走m-n个节点，然后两个链表同时遍历，遍历到相同节点的时候停止即可
"""
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        p1 = pHead1
        p2 = pHead2

        len1 = 0
        len2 = 0
        while p1:
            len1 += 1
            p1 = p1.next

        while p2:
            len2 += 1
            p2 = p2.next

        if len1 > len2:
            while len1 - len2 > 0:
                pHead1 = pHead1.next
                len1 -= 1
        else:
            while len2 - len1 > 0:
                pHead2 = pHead2.next
                len2 -= 1

        while pHead1 and pHead2:
            if pHead1 is pHead2:
                return pHead1
            pHead1 = pHead1.next
            pHead2 = pHead2.next

        return None