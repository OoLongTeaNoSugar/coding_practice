<!--
 * @Author: Zhanglei
 * @Date: 2022-02-25 11:28:32
 * @LastEditors: Zhanglei
 * @LastEditTime: 2022-02-25 11:37:13
 * @Description: file content
-->




# Leetcode.250 统计同值子树

## 题目描述

给定一个二叉树，统计该二叉树数值相同的子树个数。

同值子树是指该子树的所有节点都拥有相同的数值。

[题目链接](https://leetcode-cn.com/problems/count-univalue-subtrees/)

因为要得到子树的相关信息，利用后序遍历得到子树的信息。



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
    int res = 0;
    int countUnivalSubtrees(TreeNode* root) {
        // 先保证父节点不为空
        if(root == nullptr) return 0;
        getUnivalue(root);
        return res;
    }

    // 输入一个节点
    // 如果是同值子树 返回true
    // 不是同值子树返回false
    bool getUnivalue(TreeNode* root){
        
        if(root == nullptr) return true;
        
        bool left = getUnivalue(root->left);
        bool right = getUnivalue(root->right);
        //后序遍历位置
        
        // 已经得到子树信息
        
        if(root->left && root->val != root->left->val){
            return false;
        }
        if(root->right && root->val != root->right->val){
            return false;
        }
        if(right && left){
            res++;
            return true;
        }
        return false;

    }
};
```