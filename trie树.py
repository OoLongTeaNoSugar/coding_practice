import sys
m = int(sys.stdin.readline().strip())
values = []
for i in range(3):
    # 读取每一行
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    values.append(list(map(int, line.split())))
# print(values)
n = int(sys.stdin.readline().strip())
line = list(map(int, sys.stdin.readline().strip()))
p = int(sys.stdin.readline().strip())
key = list(map(int, sys.stdin.readline().strip()))
new_line = [0] * m
for i in range(m):
    if values[1][i] == 0:
        new_line[i] = line[0]
        line.pop(0)
values.append(new_line)
for i in range(m):
    if values[0][i] == key[0]:
        if values[1][i] == 1:
            for j in range(m):
                if values[0][j] == key[1]:
                    if values[1][j] == 1:


