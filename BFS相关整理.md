- [BFS相关整理](#bfs相关整理)
  - [## 算法框架](#-算法框架)
  - [eg.1 二叉树的最小高度](#eg1-二叉树的最小高度)
  - [eg.2 打开转盘锁](#eg2-打开转盘锁)
    - [双向BFS解题](#双向bfs解题)



# BFS相关整理

BFS 相对 DFS 的最主要的区别是：**BFS 找到的路径一定是最短的，但代价就是空间复杂度可能比 DFS 大很多**

-------------------------------


## 算法框架
---------------------------

问题的本质是在一幅「图」中找到从起点 `start` 到终点 `target` 的最近距离。

```cpp
// 计算从起点 start 到终点 target 的最近距离
int BFS(Node start, Node target) {
    Queue<Node> q; // 核心数据结构
    Set<Node> visited; // 避免走回头路
    
    q.offer(start); // 将起点加入队列
    visited.add(start);
    int step = 0; // 记录扩散的步数

    while (q not empty) {
        int sz = q.size();
        /* 将当前队列中的所有节点向四周扩散 */
        for (int i = 0; i < sz; i++) {
            Node cur = q.poll();
            /* 划重点：这里判断是否到达终点 */
            if (cur is target)
                return step;
            /* 将 cur 的相邻节点加入队列 */
            for (Node x : cur.adj())
                if (x not in visited) {
                    q.offer(x);
                    visited.add(x);
                }
        }
        /* 划重点：更新步数在这里 */
        step++;
    }
}
```


## eg.1 二叉树的最小高度

[链接](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/submissions/)

## eg.2 打开转盘锁
[leetcode链接](https://leetcode-cn.com/problems/open-the-lock/)
普通BFS解法

### 双向BFS解题


