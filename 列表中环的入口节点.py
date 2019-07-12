# -*- coding:utf-8 -*-
"""
Q: 给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。

A: 首先设置两个快慢指针，移动两个指针，如果相遇，则存在环，
然后从相遇的地方设置一个指针向后遍历并计数，回到开始的位置时，计数就是环中的结点数n，
最后设置两个指针，一个先走n步，另一个再移动，两个指针每次移动一步，相遇的结点为入口。
"""
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        meetNode = self.MeetNode(pHead)
        if not meetNode:
            return None
        # 记录循环的节点数
        loop = 1
        flag = meetNode
        while flag.next != meetNode:
            loop += 1
            flag = flag.next

        fast = pHead
        # 先让快指针走loop步
        for i in range(loop):
            fast = fast.next
        slow = pHead

        # 再让慢指针同时走直至相遇
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast


    def MeetNode(self, pHead):
        if not  pHead:
            return None
        slow = pHead.next
        if not slow:
            return None
        fast = slow.next
        while fast:
            if slow == fast:
                return slow
            slow = slow.next
            fast = fast.next.next
