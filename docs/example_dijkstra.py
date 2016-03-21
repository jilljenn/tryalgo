#!/usr/bin/env python3

from tryalgo.dijkstra import dijkstra
from tryalgo.graph import listlist_and_matrix_to_listdict

graph = [[1, 3],
         [0, 2, 3],
         [1, 4, 5],
         [0, 1, 5, 6],
         [2, 7],
         [2, 3, 7, 8],
         [3, 8, 9],
         [4, 5, 10],
         [5, 6, 10],
         [6, 11],
         [7, 8],
         [9]]

_ = None
#           0  1  2  3  4  5  6  7  8  9 10 11
weights = [[_, 1, _, 4, _, _, _, _, _, _, _, _], # 0
           [1, _, 1, 3, _, _, _, _, _, _, _, _], # 1
           [_, 1, _, _, 3, 8, _, _, _, _, _, _], # 2
           [4, 3, _, _, _, 2, 2, _, _, _, _, _], # 3
           [_, _, 3, _, _, _, _, 1, _, _, _, _], # 4
           [_, _, 8, 2, _, _, _, 2, 7, _, _, _], # 5
           [_, _, _, 2, _, _, _, _, 3, 2, _, _], # 6
           [_, _, _, _, 1, 2, _, _, _, _, 3, _], # 7
           [_, _, _, _, _, 7, 3, _, _, _, 2, _], # 8
           [_, _, _, _, _, _, 2, _, _, _, _, 1], # 9
           [_, _, _, _, _, _, _, 3, 2, _, _, _], #10
           [_, _, _, _, _, _, _, _, _, 1, _, _]] #11

dist, prec = dijkstra(graph, weights, source=0)

print(dist[10])
print("%i %i %i %i %i %i" % (10, prec[10], prec[prec[10]], prec[prec[prec[10]]],
      prec[prec[prec[prec[10]]]], prec[prec[prec[prec[prec[10]]]]]))

sparse_graph = listlist_and_matrix_to_listdict(weights)


# provides the same behavior

dist, prec = dijkstra(graph, weights, source=0)

print(dist[10])
print("%i %i %i %i %i %i" % (10, prec[10], prec[prec[10]], prec[prec[prec[10]]],
      prec[prec[prec[prec[10]]]], prec[prec[prec[prec[prec[10]]]]]))
