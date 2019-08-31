def Cost(a, b, n):
    res = 0
    pa = 0
    pb = 0
    while pb < n:
        if b[pb] > 0:
            if b[pb] > a[pa]:
                res += (pb - pa)* a[pa]
                b[pb] -= a[pa]
                pa += 1

            elif b[pb] < a[pa]:
                res += (pb-pa) * b[pb]
                a[pa] -= b[pb]
                pb += 1
            else:
                res += (pb-pa) * b[pb]
                pa += 1
                pb += 1

        else:
            pb += 1
    return res

def Three(arr, n, k):
    three = 0
    yu1 = []
    yu2 = []
    for i in range(n):
        if arr[i] % 3 == 0:
            three += 1
        elif arr[i] % 3 == 1:
            yu1.append(arr[i])
        else:
            yu2.append(arr[i])
    lenth = min(len(yu1), len(yu2))
    three += min(lenth, k)
    if lenth < k:
        k -= lenth
        len1 = len(yu1) - lenth
        len2 = len(yu2) - lenth
        while k > 0:
            if len1 > 2:
                k -= 2
                three += 1
                len1 -= 3
            elif len2 > 2:
                k -= 2
                three += 1
                len2 -= 3
            else:
                break
    return three

def uniquePathsWithObstacles(obstacleGrid):
    """
    :type obstacleGrid: List[List[int]]
        :rtype: int
        """
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    mem = [[0]*n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if not obstacleGrid[i][j]:
                if i or j:
                    mem[i][j] = mem[i - 1][j] + mem[i][j - 1]
                else:
                    mem[i][j] = 1

    return mem[-1][-1]



if __name__ == "__main__":
    import sys
    arr = [[0,1],
           [0,0]]
    print(uniquePathsWithObstacles(arr))
    # n, m, s, d = map(int, sys.stdin.readline().strip().split(' '))
    # Qi = list(map(int, sys.stdin.readline().strip().split(' ')))

    # n, k = map(int, sys.stdin.readline().strip().split(' '))
    # ai = list(map(int, sys.stdin.readline().strip().split(' ')))
    # print(Three(ai, n, k))
    # n = int(sys.stdin.readline().strip())
    # a = list(map(int, sys.stdin.readline().strip().split(' ')))
    # b = list(map(int, sys.stdin.readline().strip().split(' ')))
    # sums = Cost(a, b, n)
    # print(sums)



