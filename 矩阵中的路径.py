# -*-coding:utf-8 -*-
"""
Q: 请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。 例如 a b c e s f c s a d e e 这样的3 X 4 矩阵中包含一条字符串”bcced”的路径，但是矩阵中不包含”abcb”路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。

A: 回溯法。任选一个格子作为路径的起点。假设矩阵中某个格子的字符为ch并且这个格子将对应于路径上的第i个字符。如果路径上的第i个字符不是ch，那么这个格子不可能处在路径上的第i个位置。如果路径上的第i个字符正好是ch，那么往相邻的格子寻找路径上的第i+1个字符。除在矩阵边界上的格子外，其他各自都有4个相邻的格子。重复这个过程直到路径上的所有字符都在矩阵中找到相应的位置。


"""
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        if matrix == None or rows < 1 or cols < 1 or path == None:
            return False
        visited = [False] * (rows * cols)

        pathLenth = 0 # 记录已经走过的路径长度
        for row in range(rows):
            for col in range(cols):
                if self.hasPathCore(matrix, rows, cols, row, col, path, pathLenth, visited):
                    return True
        return False


    def hasPathCore(self, matrix, rows, cols, row, col, path, pathLength, visited):
        # 记录的字符串长度等于原始字符串长度返回true
        if len(path) == pathLength:
            return True

        HasPath = False
        if row >= 0 and row < rows and col >= 0 and col < cols and matrix[row * cols + col] == path[pathLength] and not \
        visited[row * cols + col]:

            pathLength += 1 # 对上了一个字符
            visited[row * cols + col] = True # 已经进入过的标记
            # 对后面一步的字符（四周）进行回溯
            HasPath = self.hasPathCore(matrix, rows, cols, row - 1, col, path, pathLength, visited) or \
                      self.hasPathCore(matrix, rows, cols, row, col - 1, path, pathLength, visited) or \
                      self.hasPathCore(matrix, rows, cols, row + 1, col, path, pathLength, visited) or \
                      self.hasPathCore(matrix, rows, cols, row, col + 1, path, pathLength, visited)
            # 如果不符合字符串，即四周的字符均不满足要求，对下个格子进行处理
            if not HasPath:
                pathLength -= 1
                visited[row * cols + col] = False  # 已经进入过的标记取消，对下一个各自进行处理

        return HasPath

if __name__ == "__main__":
    # 测试用例
    matrix = [
        'a', 'b', 'c', 'd',
        'e', 'f', 'g', 'h'
    ]
    rows = 2
    cols = 4
    path = ''
    print(Solution().hasPath(matrix, rows, cols, path))

