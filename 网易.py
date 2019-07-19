import sys
lines = sys.stdin.readlines()
line = lines[0]
n = int(line[0])
m = int(line[1])
dic = {}
for line in lines[1:-1]:
    line = line.strip().split()
    if not line:
        continue
    dic[int(line[0])] = int(line[1])
arr = sorted(dic.keys())