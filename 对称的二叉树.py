# -*- coding:utf-8 -*-
"""
Q: 请实现一个函数，用来判断一颗二叉树是不是对称的。
注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。

A: 把叶子节点的None结点加入到遍历中，按照前序遍历的方式遍历二叉树，存入一个序列中，然后按照和前序遍历对应的先父节点，然后右节点，最后左结点遍历二叉树，存入一个序列中，如果两个序列相等，则对称。
"""
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        return self.selfIsSym(pRoot,pRoot)

    def selfIsSym(self, root1, root2):
        if root1 == root2 and root2 == None:
            return True
        if root1 == None or root2 == None:
            return False
        if root1.val != root2.val:
            return False
        return self.selfIsSym(root1.left, root2.right) and self.selfIsSym(root1.right, root2.left)
    