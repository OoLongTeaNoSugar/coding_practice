def lihe(s):
    count = 0
    for i in s:
        if i == '(':
            count += 1
        if i == ')':
            count -= 1
        if i == '0':
            break
    return count

def solution2(total_disk,total_memory,app_list):
    res = 0
    val3 = sorted(app_list, key=lambda x:x[2])
    while len(val3) != 0:
        cur = val3.pop()
        total_disk -= cur[0]
        total_memory -= cur[1]
        if total_disk >= 0 and total_memory >= 0:
            res += cur[2]
        else:
            break
    return res


def solution3(boxes):
    n = len(boxes)
    """
    字串的动态规划
    """
    dp = [[[0]*n for _ in range(n)]for _ in range(n)]
    return rebot(boxes, dp, 0, n-1, 0)

def rebot(boxes, dp, x, y, k):
    if x > y:
        return 0
    if dp[x][y][k] > 0:
        return dp[x][y][k]
    while x > y and boxes[y] == boxes[y-1]:
        y -= 1
        k += 1

    dp[x][y][k] = rebot(boxes, dp, x, y-1, 0) + (k+1) * (k+1)
    for i in range(x, y):
        if boxes[i] == boxes[y]:
            dp[x][y][k] = max(dp[x][y][k], rebot(boxes, dp, x, i, k+1)+rebot(boxes, dp, i+1, y-1, 0))
    return dp[x][y][k]




if __name__ == "__main__":
    input1 = input()
    disk = int(input1.split()[0])
    memory = int(input1.split()[1])
    input2 = input1.split()[2]
    app_list = [[int(j) for j in i.split(',')] for i in input2.split('#')]
    print(solution2(disk, memory, app_list))