# -*- coding:utf-8 -*-
"""
https://www.nowcoder.com/study/live/202/1/3

"""
def NormalMode(s, cmmand):
    i = 0
    idx = 0
    while len(cmmand) > 0:
        cmd = cmmand.pop(0)
        if cmd == 'i':
            if not cmmand:
                return s
            cmd = cmmand.pop(0)
            while cmd != 'e':
                s.insert(idx, cmd)
                idx += 1
                if not cmmand:
                    return s
                cmd = cmmand.pop(0)

        if cmd == 'f':
            temp = cmmand[0]
            for j in range(idx + 1, len(s)):
                if temp == s[j]:
                    idx = j
                    if not cmmand:
                        return s
                    cmd = cmmand.pop(0)
                    break

        if cmd == 'x':
            del s[idx]
        if cmd == 'h':
            if idx > 0:
                idx -= 1
        if cmd == 'l':
            if idx < len(s) - 1:
                idx += 1

    return s

if __name__ == '__main__':
    s = list(input())
    cmmand = list(input())
    #print(s, cmmand)
    print(''.join(NormalMode(s, cmmand)))


