# def findbest(s, n):
#


# def diimond(a, b, n, total, cost):
#     pa = 0
#     pb = 0
#     rest_a = [0] * n
#     dimond = 0
#     while pa < n:
#         for i in range(n):
#             if b[i] == a[pa]:
#                 rest_a[pa] = i+1
#                 break
#         pa += 1
#     index =rest_a.index(min(rest_a))
#     while index < n:
#         pb = rest_a[index]
#         b = b[pb:]
#         rest_a = rest_a[index+1:]
#         index = rest_a.index(min(rest_a))
#         dimond += 1
#         total -= cost
#         if total < len(rest_a) + len(b):
#             break
#     return dimond


if __name__ == "__main__":
    import sys
    # n = int(input())
    # s = input().split(' ')
    # for i in range(len(s)):
    #     if s[i] == '+':
    #         if s[i+2] == '+' or s[i+2] == '-':
    #             if int(s[i-1]) > int(s[i+1]):
    #                 s[i - 1], s[i+1] = s[i+1],s[i-1]
    #
    n, total, cost = map(int, input().split(' '))
    a = list(map(int, input().split(' ')))
    b = list(map(int, input().split(' ')))
    # print(a,b)
    pa = 0
    pb = 0
    rest_a = [sys.float_info.max] * n
    dimond = 0
    while pa < n:
        for i in range(n):
            if b[i] == a[pa]:
                rest_a[pa] = i+1
                break
        pa += 1
    min_ = min(rest_a)
    index = rest_a.index(min_)
    while index < n:
        pb = rest_a[index]
        rest_a = rest_a[index+1:]
        dimond += 1
        total -= cost
        if total < len(rest_a) + len(b[pb:]):
            break
        if len(rest_a) == 0:
            break
        min_ = min(rest_a)
        index = rest_a.index(min_)

    print(dimond)