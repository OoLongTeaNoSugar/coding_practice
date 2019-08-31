
if __name__ == '__main__':
    g = Graph()

    start = 'a'
    end = 'e'
    shortestPath, len = g.get_shortest_path(start, end)
    print('{}->{}的最短路径是：{}，最短路径为：{}'.format(start, end, shortestPath, len))
# class Node:
#     def __init__(self, x):
#         self.value = x
#         self.intu = 0
#         self.out = 0
#         self.nexts = []
#         self.edges = []
#
# class Edge:
#     def __init__(self, x, y, z):
#         self.weight = x
#         self.froms = Node(y)
#         self.to = Node(z)
#
# class Graph:
#     def __init__(self):
#         self.nodes = {}
#         self.edges = []
#
# def createGraph(matix):
#     graph = Graph()
#     for i in range(len(matix)):
#         weight = matix[i][0]
#         froms = matix[i][1]
#         to = matix[i][2]
#         if froms not in graph.nodes:
#             graph.nodes[froms] = Node(froms)
#
#         if to not in graph.nodes:
#             graph.nodes[to] = Node(to)
#
#         fromNode = Node(graph.nodes[froms])
#         toNode = Node(graph.nodes[to])
#         newEdge = Edge(weight, fromNode, toNode)
#         fromNode.nexts.append(newEdge)
#         fromNode.out += 1
#         toNode.intu += 1
#         fromNode.edges.append(newEdge)
#         graph.edges.append(newEdge)
#
#     return graph
#
# def Dijkstra(head):
#     dis = {}
#     T = [head]
#
#     minNode = getmindisNode(dis, T)
#     while minNode:
#         distance = dis[minNode]
#         for edge in minNode.edges:
#             toNode = edge.to
#             if toNode not in dis:
#                 dis[toNode] = distance + edge.weight
#             dis[edge.to] = min(dis[toNode], distance + edge.weight)
#
#         T.append(minNode)
#         minNode = getmindisNode(dis, T)
#
#     return dis
#
#
# def getmindisNode(dismap, selectedNodes):
#     minNode = Node(None)
#     mindistance = sys.float_info.max
#     for key in dismap.keys():
#         if key not in selectedNodes and dismap[key] < mindistance:
#             mindistance = dismap[key]
#             minNode = key
#     return minNode
#
# # def BFS(node):# 边权相等
# #     if not node:
# #         return
# #
# # def DFS(cur, dis): # 边权不等
# #     if dis > min()
#
# def linjietrix(matrix, n):
#     linjie = [[sys.float_info.max] * n for _ in range(n)]
#     for i in range(len(matrix)):
#         linjie[matrix[i][1] - 1][matrix[i][2] - 1] = matrix[i][0]
#     return linjie
#
# def Dijkstra2(start, linjietrix):
#     dis = linjietrix[start - 1]
#     T = [start]
#     minvale = min(dis)
#
#
# if __name__ == "__main__":
#     import sys
#     matrix = [[10, 1, 3],
#               [30, 1, 5],
#               [100, 1, 6],
#               [50, 3, 4],
#               [60, 5, 6],
#               [20, 5, 4],
#               [10, 4, 6]]
#     # m = [[0 ]* 2 for _ in range(2)]
#     print(linjietrix(matrix, 6))
#     # print(m)
#

