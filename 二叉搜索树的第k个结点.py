# -*- coding:utf-8 -*-
"""
Q: 给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8） 中，按结点数值大小顺序第三小结点的值为4。

A: 中序遍历，输出第k个结点。先左后根最后右
"""
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        if not  pRoot or not k:
            return
        res = []
        def traverse(node):
            # 中序遍历
            # res已经有k个以上的值就不用继续遍历
            if len(res) >= k or not node:
                return
            traverse(node.left)
            res.append(node)
            traverse(node.right)
        traverse(pRoot)
        if len(res) < k:
            return
        return res[k-1]