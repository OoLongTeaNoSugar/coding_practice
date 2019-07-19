# -*- coding:utf-8 -*-
"""
把二叉树打印成多行
Q: 从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。

A: 两个队列，首先把当前层的节点存入队列1中，然后遍历队列1，遍历时，如果有左子树或者右子树，依次存入队列2，然后遍历队列2.
"""


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        """
        是按之字形打印的简化版
        :param pRoot:
        :return:
        """
        if not pRoot:
            return []
        nodes, res = [pRoot], []
        while nodes:
            curStack, nextStack = [], []
            for node in nodes:
                curStack.append(node.val)
                if node.left:
                    nextStack.append(node.left)
                if node.right:
                    nextStack.append(node.right)
                nodes = nextStack
                res.append(curStack)
        return res
