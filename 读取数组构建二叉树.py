# -*- coding: utf-8 -*-
# from __future__ import print_function
"""
重构二叉树结构
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 层次遍历
def PrintFromTopToBottom(root):
    ans = []
    if root == None:
        return ans
    else:
        q = [root]
        while q:
            node = q.pop(0)
            ans.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return ans
# 重建二叉树
def createtree(l):
    if l[0] != '#': # 输入中‘#’代表空
        root = TreeNode(int(l[0]))
        nodes = [root]
        id = 1
        while nodes and id < len(l):
            node = nodes[0]  # 依次为每个节点分配子节点
            node.left = TreeNode(int(l[id])) if l[id] != '#' else None
            nodes.append(node.left)
            node.right = TreeNode(int(l[id + 1])) if id < len(l) - 1 and l[id + 1] != '#' else None
            nodes.append(node.right)
            id += 2  # 每次取出两个节点
            nodes.pop(0)
        return root
    else:
        return None

# 前序和中序遍历重建
def reConstructBinaryTree(pre, tin):#pre、tin分别是前序序列和中序序列
    # write code here
    if len(pre)>0:
        root=TreeNode(pre[0])#前序序列的第一个肯定是当前子树的根节点
        rootid=tin.index(root.val)#通过根节点在中序序列中的位置划分出左右子树包含的节点
        root.left=reConstructBinaryTree(pre[1:1+rootid],tin[:rootid])#重建左子树
        root.right=reConstructBinaryTree(pre[1+rootid:],tin[rootid+1:])#重建右子树
        return root


def FindPath(root, expectNumber):
    """
    A: 用前序遍历的方式访问二叉树的节点，当访问到一个节点时，将该节点加到路径中，并累加节点的值。
    直到访问到符合要求的节点或者访问到叶节点，然后递归访问该节点的父节点，
    在函数退出时要删除当前节点，并减去当前节点的值。
    实际上是一个出栈和入栈的过程。
    """
    # write code here
    if not root or root.val > expectNumber:
        return []

    if not root.left and not root.right and root.val == expectNumber:
        return [[root.val]]
    else:
        expectNumber -= root.val
        left = FindPath(root.left, expectNumber)
        right = FindPath(root.right, expectNumber)

        result = [[root.val] + i for i in left]
        for i in right:
            result.append([root.val] + i)

    return sorted(result, key=lambda x: -len(x))

if __name__ == "__main__":
    import sys
    arr = sys.stdin.readline().strip().split()
    root = createtree(arr)
    tar = 8
    # print(FindPath(root,tar))
    result = FindPath(root, tar)

    # 打印矩阵解决方案
    i = 0
    while i < len(result):
        for j in result[i]:
            print(j),
        print("\n"),
        i += 1


'''
    for i in range(len(result)):
            print(result[i], end= " ")
'''


