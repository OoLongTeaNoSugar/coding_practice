<!--
 * @Author: Zhanglei
 * @Date: 2022-02-27 15:15:24
 * @LastEditors: Zhanglei
 * @LastEditTime: 2022-02-27 15:28:27
 * @Description: file content
-->


# Leetcode993. 二叉树的堂兄弟节点
 在二叉树中，根节点位于深度 0 处，每个深度为 k 的节点的子节点位于深度 k+1 处。

如果二叉树的两个节点深度相同，但 父节点不同 ，则它们是一对堂兄弟节点。

我们给出了具有唯一值的二叉树的根节点 root ，以及树中两个不同节点的值 x 和 y 。

只有与值 x 和 y 对应的节点是堂兄弟节点时，才返回 true 。否则，返回 false。



> ## 题解

二叉树问题无非就是“遍历” 和“分治”

这个问题应该使用遍历方法，确定返回`true`的条件为

1. `x` 和`y`的父节点是不同的
2. `x` 和`y`应位于同一层，即两者的深度相同。

所以，在遍历找到`x`和`y`的同时将其父节点信息和深度信息一同记录

二叉树遍历的框架为

```cpp
void traverse(root，参数){
    if(root == null) return;
    //前
    traverse(root.left);
    //中
    traverse(root.right);
    //后
}
 ```

 此题中需要找到深度和父节点，参数中需要深度信息`depth` 和父节点` TreeNode* parent`。

 另外为找到`x`和`y`的位置，要比较`root->val`所以在前序遍历位置写入。

 解答如下：


 ```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    //定义几个全局变量
    //父节点、深度，x、y的值
    TreeNode* parentX = nullptr;
    TreeNode* parentY = nullptr;
    int depthX = 0, depthY = 0;
    int x, y;

    bool isCousins(TreeNode* root, int x, int y) {
        this->x = x;
        this->y = y;
        traverse(root, 0,nullptr);

        //父节点不同且深度相同即符合条件
        if(parentX != parentY && depthY == depthX){
            return true;
        }
        return false;
    }

    //输入 root 当前深度，父节点，记录相应值
    void traverse(TreeNode* root, int depth, TreeNode* parent){
        if(root == nullptr) return;
        //前序位置

        if(root->val == x) {
            //记录x 深度和父节点
            parentX = parent;
            depthX = depth;
        }
        if(root->val == y){
            //记录y
            parentY = parent;
            depthY = depth;
        }
        
        traverse(root->left, depth+1, root);
        traverse(root->right, depth+1, root);
    }
};
 ```