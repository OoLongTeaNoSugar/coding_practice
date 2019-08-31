# tree dp

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def treedp(root):
    if not root:
        return 0, 0
    left_dp = treedp(root.left)
    right_dp = treedp(root.right)
    p1 = left_dp[0]
    p2 = right_dp[0]
    p3 = left_dp[1] + 1 + right_dp[1]
    max_dis = max(p3, max(p1, p2))
    height = max(left_dp[1], right_dp[1]) + 1
    return max_dis, height

x = TreeNode(3)
print(treedp(x))
