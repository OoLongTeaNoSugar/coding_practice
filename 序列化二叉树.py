# -*- coding:utf-8 -*-
"""
序列化二叉树
Q: 请实现两个函数，分别用来序列化和反序列化二叉树

A: 二叉树的序列化，通过前序遍历二叉树输出节点，然后碰到左子节点和右子节点为None的时候，输出一个特殊字符。
对于反序列化，就是通过输入的序列构建二叉树，针对前序遍历，可以先设置一个指针，
先指向序列的开头，然后把指针位置的数字转化成节点，当遇到特殊字符时或者超出序列长度时，对应节点为none。然后继续遍历。
"""


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.flag = -1

    def Serialize(self, root):
        # write code here
        # 树转换成序列
        if not root:
            return '#,'
        # 前序遍历的顺序，根先同级左至右
        return str(root.val) + ',' + self.Serialize(root.left) + self.Serialize(root.right)

    def Deserialize(self, s):
        # write code here
        # v序列转换成树
        self.flag += 1
        l = s.split(',')

        if self.flag >= len(s): # 超过序列长度，len(s)？应该是len(l)？
            return None
        root = None

        if l[self.flag] != '#': # 遇到非法字符，同样输出None
            root = TreeNode(int(l[self.flag]))
            root.left = self.Deserialize(s)
            root.right = self.Deserialize(s)
        return root