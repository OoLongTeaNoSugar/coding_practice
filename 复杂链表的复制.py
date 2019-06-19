# -*- coding:utf-8 -*-
"""
Q: 输入一个复杂链表
（每个节点中有节点值，以及两个指针，一个指向下一个节点，
另一个特殊指针指向任意一个节点），
返回结果为复制后复杂链表的head。
（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）

A: 复制原始链表的每个结点，将复制的结点链接在其原始结点的后面，
然后将复制后的链表中的复制结点的random指针，
指向被复制结点的random指针指向结点的下一个结点，
最后拆分链表，
拆分成原始链表结点组成的新链表和复制结点组成的复制链表。
"""
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        # 边界条件 如果pHead为空
        if not pHead:
            return None
        pNode = pHead

        while pNode:
            # 
            pClone = RandomListNode(pNode.label)
            pClone.next = pNode.next
            pNode.next = pClone
            pNode = pClone.next

        pNode = pHead

        while pNode:
            pClone = pNode.next
            if pNode.random != None:
                pClone.random = pNode.random.next
            pNode = pClone.next

        pNode = pHead
        pCloneHead = pCloneNode = pNode.next
        pNode.next = pCloneHead.next
        pNode = pNode.next

        while pNode:
            pCloneNode.next = pNode.next
            pCloneNode = pCloneNode.next
            pNode.next = pCloneNode.next
            pNode = pNode.next

        return pCloneHead



