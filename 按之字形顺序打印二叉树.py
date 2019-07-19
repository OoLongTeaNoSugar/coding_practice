# -*- coding:utf-8 -*-
"""
Q: 请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，
第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。

A: 按之字形顺序打印二叉树需要两个栈。我们在打印某一行节点时，把下一层的子节点保存到相应的栈里。
如果当前打印的奇数层，则先保存左子节点再保存右子节点到第一个栈里；
如果当前打印的是偶数层，则先保存右子节点再保存左子节点到第二个栈里。
"""
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        res, nodes = [], [pRoot]
        flag = True
        while nodes:
            curStack, nextStack = [], []
            if flag:
                for node in nodes:
                    curStack.append(node.val)
                    if node.left:
                        nextStack.append(node.left)
                    if node.right:
                        nextStack.append(node.right)

            else:
                for node in nodes:
                    curStack.append(node.val)

                    if node.right:
                        nextStack.append(node.right)
                    if node.left:
                        nextStack.append(node.left)

            nextStack.reverse()
            res.append(curStack)
            flag = not flag
            nodes = nextStack

        return res

