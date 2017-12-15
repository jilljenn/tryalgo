# jill-jenn vie et christoph durr - 2015
# -*- coding: utf-8 -*-

import unittest
import random
from collections import deque

from tryalgo.graph import write_graph, extract_path, make_flow_labels
from tryalgo.graph import tree_adj_to_prec, tree_prec_to_adj
from tryalgo.graph import matrix_to_listlist, listlist_and_matrix_to_listdict
from tryalgo.graph import listdict_to_listlist_and_matrix, dictdict_to_listdict
from tryalgo.anagrams import anagrams
from tryalgo.arithm import inv
from tryalgo.arithm_expr_eval import arithm_expr_eval, arithm_expr_parse
from tryalgo.arithm_expr_target import arithm_expr_target
from tryalgo.bellman_ford import bellman_ford
from tryalgo.knapsack import knapsack, knapsack2
from tryalgo.graph import write_graph, extract_path, make_flow_labels
from tryalgo.bfs import bfs
from tryalgo.biconnected_components import cut_nodes_edges, cut_nodes_edges2
from tryalgo.binary_search import continuous_binary_search, discrete_binary_search, optimized_binary_search, ternary_search
from tryalgo.bipartite_matching import max_bipartite_matching, max_bipartite_matching2
from tryalgo.bipartite_vertex_cover import bipartite_vertex_cover
from tryalgo.closest_points import closest_points
from tryalgo.closest_values import closest_values
from tryalgo.convex_hull import left_turn, andrew
from tryalgo.dancing_links import dancing_links
from tryalgo.dfs import find_cycle, dfs_recursive, dfs_iterative, dfs_grid
from tryalgo.dijkstra import dijkstra_update_heap, dijkstra
from tryalgo.dilworth import dilworth
from tryalgo.dinic import dinic
from tryalgo.dist_grid import dist_grid
from tryalgo.edmonds_karp import edmonds_karp
from tryalgo.eratosthene import eratosthene
from tryalgo.eulerian_tour import eulerian_tour_directed, random_eulerien_graph, is_eulerian_tour
from tryalgo.fast_exponentiation import fast_exponentiation, fast_exponentiation2
from tryalgo.fenwick import Fenwick
from tryalgo.floyd_warshall import floyd_warshall
from tryalgo.ford_fulkerson import ford_fulkerson
from tryalgo.freivalds import freivalds
from tryalgo.gale_shapley import gale_shapley
from tryalgo.gauss_jordan import gauss_jordan, GJ_ZERO_SOLUTION, GJ_UNE_SOLUTION, GJ_PLUSIEURS_SOLUTIONS
from tryalgo.graph01 import dist01
from tryalgo.horn_sat import horn_sat
from tryalgo.huffman import huffman
from tryalgo.interval_tree import interval_tree, intervals_containing
from tryalgo.interval_cover import interval_cover
from tryalgo.intervals_union import intervals_union
from tryalgo.knuth_morris_pratt_border import maximum_border_length, powerstring_by_border
from tryalgo.knuth_morris_pratt import knuth_morris_pratt
from tryalgo.kruskal import kruskal
from tryalgo.kuhn_munkres_n4 import kuhn_munkres as kuhn_munkres_n4
from tryalgo.kuhn_munkres    import kuhn_munkres as kuhn_munkres_n3
from tryalgo.rabin_karp import rabin_karp_matching
from tryalgo.roman_numbers import roman2int, int2roman
from tryalgo.laser_mirrors import laser_mirrors
from tryalgo.left_right_inversions import left_right_inversions
from tryalgo.levenshtein import levenshtein
from tryalgo.longest_common_subsequence import longest_common_subsequence
from tryalgo.longest_increasing_subsequence import longest_increasing_subsequence
from tryalgo.lowest_common_ancestor import LowestCommonAncestorShortcuts, LowestCommonAncestorRMQ
from tryalgo.majority import majority
from tryalgo.manacher import manacher
from tryalgo.matrix_chain_mult import matrix_mult_opt_order, matrix_chain_mult
from tryalgo.max_interval_intersec import max_interval_intersec
from tryalgo.merge_ordered_lists import merge
from tryalgo.min_mean_cycle import min_mean_cycle
from tryalgo.next_permutation import next_permutation
from tryalgo.our_heap import OurHeap
from tryalgo.our_queue import OurQueue
from tryalgo.permutation_rank import permutation_rank, rank_permutation
from tryalgo.partition_refinement import PartitionRefinement
from tryalgo.polygon import area, is_simple
from tryalgo.pq_tree import consecutive_ones_property
from tryalgo.predictive_text import predictive_text, propose
from tryalgo.rabin_karp import rabin_karp_factor
from tryalgo.range_minimum_query import RangeMinQuery, LazySegmentTree
from tryalgo.rectangles_from_grid import rectangles_from_grid
from tryalgo.rectangles_from_histogram import rectangles_from_histogram
from tryalgo.rectangles_from_points import rectangles_from_points
from tryalgo.scalar import min_scalar_prod
from tryalgo.shortest_cycle import shortest_cycle, powergraph
from tryalgo.skip_list import SortedSet, SortedDict
from tryalgo.strongly_connected_components import tarjan, kosaraju, tarjan_recursif
from tryalgo.subsetsum_divide import subset_sum as subset_sum1
from tryalgo.subsetsum import subset_sum as subset_sum2, coin_change
from tryalgo.sudoku import sudoku
from tryalgo.three_partition import three_partition
from tryalgo.topological_order import topological_order_dfs, topological_order
from tryalgo.trie import Trie, spell_check
from tryalgo.two_sat import two_sat
from tryalgo.union_rectangles import union_rectangles
from tryalgo.windows_k_distinct import windows_k_distinct


class TestTryalgo(unittest.TestCase):


    def unorder(self, L):
        return sorted(sorted(group) for group in L)

    def test_anagrams(self):
        L = [("le chien marche vers sa niche et trouve une "
                       "limace de chine nue pleine de malice "
                       "qui lui fait du charme".split(),
                       [['nue', 'une'],
                        ['limace', 'malice'],
                        ['marche', 'charme'],
                        ['chien', 'niche', 'chine']]),
            (["aba", "baa", "abb"], [["aba", "baa"]]),
            (["aba"], []),
            ([], [])]
        for words, res in L:
            self.assertEqual(self.unorder(anagrams(words)), self.unorder(res))

    def test_arithm(self):
        self.assertEqual(inv(8, 17), 15)

    def test_arithm_expr_eval(self):
        L = [("13 + A47 * ZZ22", 37),
             ("4 / 7 + 4 / 7", 0),
             ("3 * 3 / 7", 1),
             ("12", 12)]
        for str_expr, val in L:
            cell = {"ZZ22": 3, "A47": 8}
            expr = arithm_expr_parse(str_expr.split())
            self.assertEqual(arithm_expr_eval(cell, expr), val)

    def test_arithm_expr_target(self):
        L = [([3, 100, 8, 8, 10, 6], 683, 683 ),
         ([3, 75, 2, 4, 1, 1],   997, 1000)]
        for vals, target, res in L:
            answer = arithm_expr_target(vals, target)
            closest = int(answer[ answer.find('=')+1: ])
            self.assertEqual(closest, res)


    graph_undir_1 = [[1,3], [0,1,2], [1,5], [0,4,6], [3,5,7], [2,4,8], [3,7], [4,6,8], [5,7]]
    graph_undir_2 = [[1], [0,1,2], [1,5], [4,6], [3,7], [2,8], [3,7], [4,6], [5]]

    _ = None

    # title, graph, weight, has_neg_circuit_reachable, shortest_path from 0 to n-1
    L_dir = [("reachable_neg_cycle",
               [[1], [2], [5], [6], [3], [4,8], [7], [4], [2]],
                 #  0  1  2  3  4  5  6  7  8
                 [[ _, 1, _, 0, _, _, _, _, _],  # 0
                  [ 1, 1, 4, _, _, _, _, _, _],  # 1
                  [ _, 4, _, _, _,-3, _, _, 2],  # 2
                  [ 0, _, _, _, 1, _, 3, _, _],  # 3
                  [ _, _, _, 1, _, 5, _, 1, _],  # 4
                  [ _, _,-3, _, 5, _, _, _, 2],  # 5
                  [ _, _, _, 3, _, _, _,-6, _],  # 6
                  [ _, _, _, _, 1, _,-6, _,-2],  # 7
                  [ _, _, 2, _, _, 2, _,-2, _],  # 8
                  ], True, None),
            ("non_reachable_neg_cycle",
               [[1], [2], [5], [6], [3], [8], [7], [4], [2]],
                 #  0  1  2  3  4  5  6  7  8
                 [[ _, 1, _, 0, _, _, _, _, _],  # 0
                  [ 1,-1, 4, _, _, _, _, _, _],  # 1
                  [ _, 4, _, _, _,-3, _, _, 2],  # 2
                  [ 0, _, _, _, 1, _, 3, _, _],  # 3
                  [ _, _, _, 1, _, 5, _, 1, _],  # 4
                  [ _, _,-3, _, 5, _, _, _, 2],  # 5
                  [ _, _, _, 3, _, _, _,-6, _],  # 6
                  [ _, _, _, _, 1, _,-6, _,-2],  # 7
                  [ _, _, 2, _, _, 2, _,-2, _],  # 8
                  ], False, [0,1,2,5,8]),
            ("single_vertex",
                [[]],
                [[_]], False, [0]),
            ("single_arc",
                [[1], []],
                 [[ _, -3],
                 [ _, _]], False, [0, 1]),
            ("two_nodes",
                [[], []],
                 [[ _, _],
                 [ _, _]], False, None),
            ("neg_self_loop",
                [[0, 1], [0, 1]],
                [[ 2,  3],
                 [ 3, -1]], True, None)
            ]

    def test_bellman_ford(self):
        for title, graph, weight, has_circuit, shortest_path in self.L_dir:
            sparse = listlist_and_matrix_to_listdict(graph, weight)
            for g,w in [(graph, weight), (sparse, sparse)]:
                dist, prec, detect = bellman_ford(g, w)
                self.assertEqual(has_circuit, detect)
                if not has_circuit:
                    target = len(graph) - 1
                    if shortest_path is not None:
                        path = extract_path(prec, target)
                        self.assertEqual(path, shortest_path)
                    else:
                        self.assertEqual(dist[target], float('inf'))


    def test_bfs(self):
        # graphe complet plus un sommet isolé
        n = 7
        G1 = [[j for j in range(n) if j != i] for i in range(n)]   # graphe complet
        G1.append([])                                              # sommet isolé
        A1 = ([0] + [1] * (n-1) + [float('inf')],
                                  [None] +  [0] * (n-1) + [None])
        # arbre binaire complet
        G2 = [[], [2, 3]] + [[2 * i, 2 * i + 1, i // 2] for i in range(2, 8)] + \
             [[i // 2] for i in range(8, 16)]
        A2 = ([float('inf'), 0, 1, 1, 2, 2, 2, 2,
                                                  3, 3, 3, 3, 3, 3, 3, 3],
                                     [None, None, 1, 1, 2, 2, 3, 3, 4,
                                                  4, 5, 5, 6, 6, 7, 7])
        # list of graph, source, answer tuples
        L = [(G1, 0, A1), (G2, 1, A2),
             ([[]], 0, ([0], [None])),
             ([[], []], 0, ([0, float('inf')], [None, None])),
             ([[1], [0]], 0, ([0, 1], [None, 0]))]
        for graph, source, answer in L:
            V = range(len(graph))
            for g in [graph, listlist_and_matrix_to_listdict(graph)]:
                self.assertEqual(bfs(g, source), answer)


    def test_cut_nodes_edges(self):
            G0 = [[1, 2, 5],
                  [0, 5],
                  [0, 3, 4],
                  [2, 4, 5, 6],
                  [2, 3, 5, 6],
                  [0, 1, 3, 4],
                  [3, 4]]
            A0 = ([], [])
            G1 = [[], [2, 4], [1, 3, 5], [2, 4, 5], [3, 1], [2, 3, 6, 7], [5, 7, 8],
                  [5, 6, 8], [6, 7, 9], [8, 10, 11], [9, 11], [9, 10]]
            A1 = ([5, 8, 9], [(8, 9)])
            G2 = [[2, 5],
                  [3, 8],
                  [0, 3, 5],
                  [1, 2, 6, 8],
                  [7],
                  [0, 2],
                  [3, 8],
                  [4],
                  [1, 3, 6]]
            A2 = ([2, 3], [(2, 3), (4, 7)])
            G3 = [[1, 2], [0, 2], [0, 1, 3], [2]]
            A3 = ([2], [(2, 3)])
            big = 10000
            G4 =   [[(i + 1) % big, (i - 1) % big] for i in range(big)] \
                 + [[big + ((i + 1) % big), big + ((i - 1) % big)] for i in range(big)]
            G4[0].append(big)
            G4[big].append(0)
            A4 = ([0, big], [(0, big)])
            L = [(G0, A0), (G1, A1), (G2, A2), (G3, A3), (G4, A4),
                 ([[]], ([], [])),
                 ([[1,2],[0],[0]], ([0], [(0, 1), (0, 2)])),
                 ([[1], [0]], ([], [(0, 1)])),
                 ([[1], [0, 2], [1]], ([1], [(0, 1), (1, 2)]))]
            for graph, answer in L:
                cn, ce = cut_nodes_edges(graph)
                self.assertEqual( (sorted(cn), sorted(ce)), answer)
            for graph, answer in L:
                if len(graph) <= 5000:
                    cn, ce = cut_nodes_edges2(graph)
                    self.assertEqual( (sorted(cn), sorted(ce)), answer)

            # for G, name in [(G0, "g0"), (G1, 'g1'), (G2, 'g2')]:
            #     cut_nodes, cut_edges = cut_nodes_edges(G)
            #     write_graph("biconnexes_%s.dot" % name, G,
            #                 node_mark=cut_nodes, arc_mark=set(cut_edges))


    def test_binary_search(self):
        L = 1 << 19
        for x0 in [0, 1, (1 << 18) - 1, 1 << 18, (1 << 18) + 1, (1 << 19) - 1]:

            def f(x):
                return x >= x0

            self.assertEqual( continuous_binary_search(f, 0, L) - x0 < 1e-4, True)

            T = [(x >= x0) for x in range(L)]
            self.assertEqual( discrete_binary_search(T, 0, L - 1), x0)
            self.assertEqual( optimized_binary_search(T, 20), x0)

    def test_max_bipartite_matching(self):
        self.assertEqual( [None], max_bipartite_matching([[]]))
        self.assertEqual( [], max_bipartite_matching2([[]]))
        self.assertEqual( [None, None], max_bipartite_matching([[], []]))
        self.assertEqual( [], max_bipartite_matching2([[], []]))
        self.assertEqual( [0, None], max_bipartite_matching([[0], [0]]))
        self.assertEqual( [0], max_bipartite_matching2([[0], [0]]))
        self.assertEqual( [0, 1], max_bipartite_matching([[0], [0, 1]]))
        self.assertEqual( [0, 1], max_bipartite_matching2([[0], [0, 1]]))
        self.assertEqual( [0, 1, 2, 4, None],
                        max_bipartite_matching([[0], [0, 1], [2, 3], [1], [0, 3]]))
        self.assertEqual( [0, 1, 2, 4],
                        max_bipartite_matching2([[0], [0, 1], [2, 3], [1], [0, 3]]))


    def test_bipartite_vertex_cover(self):
        for n in range(1, 10):                   # try different random bipartite graphs
            V = range(n)
            bigraph = [[] for u in V]
            for i in range(100):
                for _ in range(n*n // 8):
                    u = random.choice(V)
                    v = random.choice(V)
                    if v not in bigraph[u]:
                        bigraph[u].append(v)
                matching = max_bipartite_matching(bigraph)
                low = n - matching.count(None)
                Su, Sv = bipartite_vertex_cover(bigraph)
                high = Su.count(True) + Sv.count(True)
                self.assertEqual(low, high)      # verify cardinalities
                for u in V:                      # verify vertex cover
                    for v in bigraph[u]:
                        self.assertTrue( Su[u] or Sv[v] )

    def test_closest_points(self):
        S = [(3*i, 3*i) for i in range(1000)]
        S.append((501, 501))
        self.assertEqual(set(closest_points(S)), {(501, 501), (501, 501)})
        self.assertEqual(set(closest_points([(0,0), (1,1)])), {(0,0), (1,1)})

    def test_closest_values(self):
        L = [0, 2]
        self.assertEqual(closest_values(L), (0, 2))
        L = list(range(0, 1000000, 10)) + [56]
        self.assertEqual(closest_values(L), (56, 60))


    def test_left_turn(self):

        def add(a, b):
            return (a[0] + b[0], a[1] + b[1])

        def mul(a, b):
            return (a[0] * b[0], a[1] * b[1])

        def f(p):
            return mul(add(p, (dx, dy)), (s, s))

        L = [(0, 0), (1, 2), (-2, -1)]
        for dx in [-10, 0, 10]:
            for dy in [-10, 0, 10]:
                for s in [-1, +1]:
                    self.assertEqual(left_turn(*map(f, L)), True)


    def test_andrew(self):
        P = [(0,0), (1,0), (2,1), (2,4), (1,3), (0,3)]
        self.assertEqual(andrew(P + [(1,2)]), [(0, 0), (1, 0), (2, 1), (2, 4), (0, 3)])
        self.assertEqual(andrew(P + [(0,2)]), [(0, 0), (1, 0), (2, 1), (2, 4), (0, 3)])
        self.assertEqual(andrew(P + [(-1,2)]), [(-1, 2), (0, 0), (1, 0), (2, 1), (2, 4), (0, 3)])
        self.assertEqual(andrew([(0,0), (1,0)]), [(0,0), (1,0)])
        self.assertEqual(andrew([(0,0), (0,1)]), [(0,0), (0,1)])


    def test_dancing_links(self):
        self.assertEqual(dancing_links(7, [[2, 4, 5], [3, 4, 6], [1, 2, 5], [0, 3], [1, 6], [3, 4, 6]]),
                            [3, 0, 4])
        self.assertEqual(dancing_links(1, [[0]]), [0])
        self.assertEqual(dancing_links(2, [[0], [0, 1]]), [1])


    def test_dfs(self):

        def reachable(graph, start, dfs):
            """Nodes reachable from a start vertex

            :param graph: adjacency list
            :param start: start vertex
            :param dfs: implementation of DFS to use
            :returns: list of vertices in the component containing start
            """
            n = len(graph)
            seen = [False] * n
            dfs(graph, start, seen)
            retval = [node for node in range(n) if seen[node]]
            seen = [False] * n
            dfs(listlist_and_matrix_to_listdict(graph), start, seen)
            self.assertEqual(retval, [node for node in range(n) if seen[node]])
            return retval

        n = 100000
        G = [[v for v in range(u + 1, min(u + 10, n))] for u in range(n)]
        self.assertEqual( reachable(G, 3, dfs_iterative), list(range(3, n)))

        # tests sur la profondeur possible de la récursion
        # from random import *
        # from sys    import *

        # G2 = [[] for u in range(n)]
        # for _ in range(15 * n):
        #     u = random.randint(0, n - 1)
        #     v = random.randint(0, n - 1)
        #     G2[u].append(v)
        #     G2[v].append(u)

        # setrecursionlimit(2 * n + 10)
        # graph = G2
        # seen = [None] * n
        # dfs(0)
        # print( "aha")
        # exit(0)

        for f in [dfs_recursive, dfs_iterative]:
            self.assertEqual( reachable([[]], 0, f), [0] )
            self.assertEqual( reachable([[1], []], 0, f), [0, 1] )
            self.assertEqual( reachable([[1], []], 1, f), [1] )
            self.assertEqual( reachable([[1], [2], []], 1, f), [1, 2] )
            self.assertEqual( reachable([[1, 5], [2, 3, 5], [3], [4, 5], [5], []], 2, f), [2, 3, 4, 5] )


    def test_dfs_grid(self):
        inTextGrid = """\
##########
.....#...#
####.###.#
#..#.#...#
#..#.#.###
###..#.#.#
#.#.####.#
#........#
########.#\
"""

        outTextGrid = """\
##########
XXXXX#...#
####X###.#
#..#X#...#
#..#X#.###
###XX#.#X#
#X#X####X#
#XXXXXXXX#
########X#\
"""
        grid = [list(line.strip()) for line in inTextGrid.split('\n')]
        out = [list(line.strip()) for line in outTextGrid.split('\n')]
        dfs_grid(grid, 1, 0)
        self.assertEqual( str(grid), str(out) )

    def test_find_cycle(self):
        L = [ ([], None),
              ([[]], None),
              ([[], []], None),
              ([[1], [0]], None),
              ([[], [2], [1]], None),
              ([[1, 2], [0, 2], [0, 1]], {0,1,2}),
              ([[1, 2], [0], [0], [2, 4], [3]], [2, 3]),
              ([[1, 2], [0], [0]], None),
              ([[1, 2], [0], [0], [4, 5], [3, 5], [3, 4]], [4, 5, 3]) ]
        for graph, result in L:
            for g in [graph, listlist_and_matrix_to_listdict(graph)]:
                answer = find_cycle(g)
                if isinstance(result, set):
                    self.assertEqual(set(answer), result)
                else:
                    self.assertEqual(answer, result)


    def test_dijkstra(self):
        _ = None
        L_dir = [("reachable_cycle",
               [[1], [2], [5], [6], [3], [4, 8], [7], [4], [2]],
                 #  0  1  2  3  4  5  6  7  8
                 [[ _, 1, _, 0, _, _, _, _, _],  # 0
                  [ 1, 1, 4, _, _, _, _, _, _],  # 1
                  [ _, 4, _, _, _, 3, _, _, 2],  # 2
                  [ 0, _, _, _, 1, _, 3, _, _],  # 3
                  [ _, _, _, 1, _, 5, _, 1, _],  # 4
                  [ _, _, 3, _, 5, _, _, _, 2],  # 5
                  [ _, _, _, 3, _, _, _, 6, _],  # 6
                  [ _, _, _, _, 1, _, 6, _, 2],  # 7
                  [ _, _, 2, _, _, 2, _, 2, _],  # 8
                  ], [0, 1, 2, 5, 8]),
            ("single_vertex",
                [[]],
                [[_]], [0]),
            ("single_arc",
                [[1], []],
                [[ _, 3],
                 [ _, _]], [0, 1]),
            ("two_nodes",
                [[], []],
                [[ _, _],
                 [ _, _]], None),
            ]
        for f in [dijkstra, dijkstra_update_heap]:
            for title, graph, weight, shortest_path in L_dir:
                sparse = listlist_and_matrix_to_listdict(graph, weight)
                for g, w in [(graph, weight), (sparse, sparse)]:
                    source = 0
                    target = len(g)-1
                    dist, prec = f(g, w, source, target)
                    path = extract_path(prec, target)
                    if shortest_path is None:
                        self.assertFalse(path[0] == source)
                    else:
                        self.assertEqual(path, shortest_path)
                        val = sum(weight[path[i]][path[i+1]] for i in range(len(path)-1))
                        self.assertEqual(dist[target], val)


    def test_dilworth(self):
        G = [[1],
             [2, 3, 5],
             [6, 7],
             [7, 8],
             [5, 6],
             [8],
             [8],
             [],
             []]
        for graph in [G, listlist_and_matrix_to_listdict(G)]:
            self.assertEqual(set(dilworth(graph)), {0,1,2})
        # write_graph(dotfile="dilworth.dot", graph=G, directed=True, node_label=p)


    def test_flow(self):
        graph = [[1, 2, 3, 4],
                 [0, 5, 7],
                 [0, 5, 7],
                 [0, 5],
                 [0, 5],
                 [1, 2, 3, 4, 6],
                 [5, 7, 8, 9, 10],
                 [1, 2, 6, 11],
                 [6, 11],
                 [6, 11],
                 [6, 11],
                 [7, 8, 9, 10]]
        _ = None
        capacity = [[0, 10, 3, 15, 7, _, _, _, _, _, _, _],
                  [10, 0, _, _, _, 99, _, 99, _, _, _, _],
                  [3, _, 0, _, _, 99, _, 99, _, _, _, _],
                  [15, _, _, 0, _, 99, _, _, _, _, _, _],
                  [7, _, _, _, 0, 99, _, _, _, _, _, _],
                  [_, 99, 99, 99, 99, 0, 9, _, _, _, _, _],
                  [_, _, _, _, _, 9, 0, 99, 99, 99, 99, _],
                  [_, 99, 99, _, _, _, 99, 0, _, _, _, 15],
                  [_, _, _, _, _, _, 99, _, 0, _, _, 3],
                  [_, _, _, _, _, _, 99, _, _, 0, _, 7],
                  [_, _, _, _, _, _, 99, _, _, _, 0, 10],
                  [_, _, _, _, _, _, _, 15, 3, 7, 10, 0]]
        for f in [dinic, edmonds_karp, ford_fulkerson]:
            sparse = listlist_and_matrix_to_listdict(graph, capacity)
            for g, w in [(graph, capacity), (sparse, sparse)]:
                flow_matr, flow_val = f(g, w, 0, 11)
                self.assertEqual(flow_val, 35)
                labels = make_flow_labels(g, flow_matr, w)
                # write_graph("dinic.dot", graph, directed=True, arc_label=labels)
        graph = [{1: 9, 2: 9}, {3: 1}, {4: 1}, {5: 9}, {5: 9}, {}]
        for f in [dinic, edmonds_karp, ford_fulkerson]:
            flow_matr, flow_val = f(graph, graph, 0, 5)
            self.assertEqual(flow_val, 2)



    def test_dist_grid(self):
        G = '''\
#### ##   #  #
#    #   ### #
##   #    #  #
#  # # #     #
#  # # #     #
#  ### #  ####
#      #     #
##############'''
        grid = []
        for line in G.split('\n'):
            grid.append(list(line))
        dist_grid(grid, (1, 1), (6, 12))
        H = '\n'.join([''.join(line) for line in grid])
        self.assertEqual(H, """\
####^##^^># ^#
#s>>>#^^^###^#
##vvv#^>>>#^^#
#<v#v#^#vv>>>#
#vv#v#^#vvvvv#
#vv###^#vv####
#vv>>>>#vv>>t#
##############""")

        G = '''\
###
 ##
 ##
 ##
 ##
 ##
 ##
###'''

        grid = list(map(lambda line: list(line), G.split('\n')))
        dist_grid(grid, (1, 0), (6, 0))
        H = '\n'.join((''.join(line) for line in grid))
        self.assertEqual(H, """\
###
s##
v##
v##
v##
v##
t##
###""")


    def test_eratosthene(self):
        self.assertEqual(eratosthene(98), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])


    def test_eulerian_tour_directed(self):
        graphs = [random_eulerien_graph(50),
                  [[1, 2], [0, 2, 3, 4], [0, 1, 3, 4], [1, 2], [1, 2]],
                  [[1, 2], [0, 2, 3, 4], [0, 1, 3, 4], [1, 2, 4], [1, 2, 3]],
                  [[1, 3, 4], [0, 2], [1], [0, 4], [0, 3]],
                  [[1, 2], [0, 2, 3, 4], [0, 1], [1, 4],
                   [1, 3, 5, 6], [4, 6], [4, 5]],
                  [[1], [0]],
                  [[1, 2], [0, 3], [0, 3], [1, 2, 4], [3]],
                  [[1, 2], [0, 2], [0, 1]],
                  [[1, 2], [0, 2], [3], [1]],
                  [[1], [2], [3], [4, 5], [3, 6], [4], [0]]]
        for g in graphs:
            # for g in [graph, listlist_and_matrix_to_listdict(graph)]:
            self.assertTrue(is_eulerian_tour(g, eulerian_tour_directed(g)))


    def test_fast_exponentation(self):
        for f in [fast_exponentiation, fast_exponentiation2]:
            self.assertEqual( f(1, 23, 1000), 1 )
            self.assertEqual( f(23, 1, 1000), 23 )
            self.assertEqual( f(23, 2, 1000), 23 * 23 )
            self.assertEqual( f(23, 0, 1000), 1 )
            self.assertEqual( f(7, 23, 1000000000), 80916343 )
            self.assertEqual( f(7, 2323474, 1000000000), 428796849 )


    def test_fenwick(self):
        F = Fenwick([0, 1, 2, 4, 8, 16, 32, 64, 128, 256])
        self.assertEqual( bin(F.intervalSum(3, 7)), "0b1111100" )
        self.assertEqual( bin(F.intervalSum(2, 5)), "0b11110" )
        F.add(4, -8)
        self.assertEqual( bin(F.intervalSum(3, 7)), "0b1110100" )
        self.assertEqual( bin(F.intervalSum(2, 5)), "0b10110" )


    def test_floyd_warshall(self):
        # https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm#/media/File:Floyd-Warshall_example.svg
        _ = float('inf')
        weight = [[ _, _,-2, _],
                  [ 4, _, 3, _],
                  [ _, _, _, 2],
                  [ _,-1, _, _]]
        self.assertFalse(floyd_warshall(weight))
        self.assertEqual(weight,  [[3, -1, -2, 0], [4, 3, 2, 4], [5, 1, 3, 2], [3, -1, 1, 3]])


    def test_freivalds(self):
        A = [[2,3], [3,4]]
        B = [[1,0], [1,2]]
        C = [[5,6], [7,8]]
        self.assertTrue(freivalds(A, B, C))
        # [!] might fail with small probability


    def test_gale_shapley(self):
        self.assertEqual(gale_shapley([[0, 1, 2], [2, 1, 0], [0, 2, 1]],
                                      [[0, 1, 2], [1, 2, 0], [1, 2, 0]]), [0, 2, 1])


    def test_gauss_jordan(self):
        x = [0, 0, 0]
        self.assertEqual( gauss_jordan([[3, 2, -1], [2, -2, 4], [-1, .5, -1]],
                            x, [1, -2, 0]), GJ_UNE_SOLUTION)
        x = [0, 0]
        self.assertEqual( gauss_jordan([[3, 2], [6, 4]],
                            x, [6, 12]), GJ_PLUSIEURS_SOLUTIONS)
        self.assertEqual( gauss_jordan([[1, -2], [3, 5], [4, 3]],
                            x, [-1, 8, 7]), GJ_UNE_SOLUTION)
        self.assertEqual( gauss_jordan([[3, 2], [3, 2]], x, [6, 12]), GJ_ZERO_SOLUTION)
        self.assertEqual( gauss_jordan([[1, 1], [2, 1], [3, 2]],
                            x, [1, 1, 3]), GJ_ZERO_SOLUTION)

    def test_dist01(self):
        _ = None
        L_dir = [("reachable_cycle",
               [[1,3], [0,1,2], [1,5], [0,4,6], [3,5,7], [2,4,8], [3,7], [4,6], [5]],
                 #  0  1  2  3  4  5  6  7  8
                 [[ _, 0, _, 0, _, _, _, _, _],  # 0
                  [ 0, 0, 1, _, _, _, _, _, _],  # 1
                  [ _, 1, _, _, _, 1, _, _, _],  # 2
                  [ 0, _, _, _, 1, _, 0, _, _],  # 3
                  [ _, _, _, 1, _, 1, _, 0, _],  # 4
                  [ _, _, 1, _, 1, _, _, _, 0],  # 5
                  [ _, _, _, 0, _, _, _, 0, _],  # 6
                  [ _, _, _, _, 0, _, 0, _, _],  # 7
                  [ _, _, _, _, _, 0, _, _, _],  # 8
                  ], [0, 3, 6, 7, 4, 5, 8]),
            ("single_vertex",
                [[]],
                [[_]], [0]),
            ("single_arc",
                [[1], []],
                [[ _, 1],
                 [ _, _]], [0, 1]),
            ("two_nodes",
                [[], []],
                [[ _, _],
                 [ _, _]], None),
            ]
        for title, g, w, shortest_path in L_dir:
            sparse = listlist_and_matrix_to_listdict(g, w)
            for graph, weight in [(g, w), (sparse, sparse)]:
                source = 0
                target = len(graph) - 1
                dist, prec = dist01(graph, weight, source, target)
                path = extract_path(prec, target)
                if shortest_path is None:
                    self.assertFalse(path[0] == source)
                else:
                    self.assertEqual(path, shortest_path)
                    val = sum(weight[path[i]][path[i+1]] for i in range(len(path)-1))
                    self.assertEqual(dist[target], val)


    def test_horn_sat(self):
        F1 = [(1, []), (1, []), (None, [2])]
        F2 = [(1, []), (2, []), (3, [1, 2]),
              (3, [5]), (4, [1, 3, 3, 3]), (5, [1, 1, 6])]
        F3 = [(1, [1, 2]), (2, [])]
        F4 = F2 + [(None, [1, 3])]
        F5 = [(1, [2, 2]), (2, [])]
        self.assertEqual(horn_sat(F1), {1} )
        self.assertEqual(horn_sat(F2), {1, 2, 3, 4} )
        self.assertEqual(horn_sat(F3), {2} )
        self.assertEqual(horn_sat(F4), None )
        self.assertEqual(horn_sat(F5), {1, 2} )

    def test_huffman(self):
        self.assertEqual(huffman({'a': 7, 'b': 7, 'c': 7, 'd': 7}),
                                 {'a': '00', 'c': '10', 'b': '01', 'd': '11'})
        self.assertEqual(huffman({'a': 40, 'b': 5, 'c': 2, 'd': 1}),
                                 {'a': '1', 'c': '001', 'b': '01', 'd': '000'})


    def test_interval_tree(self):

        def check(L, R):
          IT = interval_tree(sorted(L))
          for x in R:
              A = intervals_containing(IT, x)
              B = [(l, r) for (l, r) in L if l <= x and x < r]
              self.assertEqual( sorted(A), sorted(B) )

        R = list(range(10))
        Q = [([], R), ([(1, 3)], R), ([(1, 3), (5, 7)], R),
             ([(1, 3), (3, 6), (5, 7)], R)]
        for L, R in Q:
            check(L, R)
        for q in range(100):
            L = []
            for _ in range(100):
                a = random.randint(1, 1000)
                b = random.randint(1, 1000)
                a, b = min(a, b), max(a, b) + 1
                L.append((a, b))
            R = [random.randint(-10, 1010) for _ in range(100)]
            check(L, R)


    def test_intervals_cover(self):
        L = [([(0,1)], 1),
             ([(0,3), (1,2)], 1),
             ([(0,2), (1,3)], 1),
             ([(0,2), (2,3)], 1),
             ([(0,2), (3,4)], 2),
             ([(0,4), (1,3), (2,6), (5,8), (7,9), (9,10)], 3)]
        for instance, res in L:
            self.assertEqual(len(interval_cover(instance)), res)

    def test_intervals_union(self):
        L = [(2, 3), (4, 6), (1, 5), (6, 7), (8, 10)]
        self.assertEqual( intervals_union(L), [(1, 7), (8, 10)])
        self.assertEqual( intervals_union([]), [])
        self.assertEqual( intervals_union([(0, 1)]), [(0, 1)])
        self.assertEqual( intervals_union([(1, 2), (0, 1)]), [(0, 2)])
        self.assertEqual( intervals_union([(2, 3), (0, 1)]), [(0, 1), (2, 3)])

    def test_knapsack(self):
        L = [([580, 1616, 1906, 1942, 50, 294],
              [874, 620, 345, 269, 360, 470], 2000, 1704),
             ([2, 3, 5], [6, 4, 2], 9, 10),
             ([5, 4, 3, 2, 1], [30, 19, 20, 10, 20], 10, 70),
             ([3, 3, 2, 2, 2], [40, 40, 10, 20, 30], 7, 90),
             ([2], [42], 1, 0),
             # ([], [], 0, 0),
             ([1], [42], 0, 0)]
        for f in [knapsack, knapsack2]:
            for p, v, cmax, opt in L:
                self.assertEqual(knapsack(p, v, cmax)[0], opt)


    def test_knuth_morris_pratt_border(self):
        self.assertEqual( maximum_border_length("aba#abababaababb"),
                         [0, 0, 1, 0, 1, 2, 3, 2, 3, 2, 3, 1, 2, 3, 2, 0])
        self.assertEqual( powerstring_by_border("ababab"), 3)
        self.assertEqual( powerstring_by_border("abaab"), 1)


    def test_kruskal(self):
        # from http://www.ics.uci.edu/~eppstein/PADS/MinimumSpanningTree.py
        sparse = [{1:11,2:13,3:12}, {0:11,3:14}, {0:13,3:10}, {0:12,1:14,2:10}]
        tree = [(2, 3), (0, 1), (0, 3)]
        for graph, weight in [(sparse, sparse), listdict_to_listlist_and_matrix(sparse)]:
            self.assertEqual(kruskal(graph, weight), tree)


    def test_knuth_morris_pratt(self):
        for match in [rabin_karp_matching, knuth_morris_pratt]:
            p = "a" * 10 + "b"
            t = "a" * 100 + "b"
            self.assertEqual( match(t, p), len(t) - len(p) )
            p = ''.join(map(str, [random.randint(0, 9) for _ in range(10)]))
            t = ''.join(map(str, [random.randint(0, 9) for _ in range(100)]))
            self.assertEqual( match(t, p), -1 )  # hopefully
            self.assertEqual( match("ab", "a"), 0  )
            self.assertEqual( match("ab", "b"), 1  )
            self.assertEqual( match("ab", "c"), -1 )
            self.assertEqual( match("",   "c"), -1 )

    def test_kuhn_munkres(self):
        for kuhn_munkres in [kuhn_munkres_n3, kuhn_munkres_n4]:
            self.assertEqual( kuhn_munkres([[1]])[0] , [0] )
            self.assertEqual( kuhn_munkres([[1, 1], [1, 1]])[0], [1, 0] )
            self.assertEqual( kuhn_munkres([[1, 2], [1, 1]])[0] , [1, 0] )
            self.assertEqual( kuhn_munkres([[1, 1], [2, 1]])[0], [1, 0] )
            self.assertEqual( kuhn_munkres([[2, 1], [1, 1]])[0], [0, 1] )
            self.assertEqual( kuhn_munkres([[1, 1], [1, 2]])[0], [0, 1] )
            self.assertEqual( kuhn_munkres([[-1, -2, -3], [-6, -5, -4],
                                 [-1, -1, -1]])[0], [0, 2, 1] )
            self.assertEqual( kuhn_munkres([[1, 2, 3], [6, 5, 4], [1, 1, 1]])[0], [2, 0, 1] )
            self.assertEqual( kuhn_munkres([[7,   53, 183, 439, 863],
                                [497, 383, 563,  79, 973],
                                [287,  63, 343, 169, 583],
                                [627, 343, 773, 959, 943],
                                [767, 473, 103, 699, 303]])[1], 3315 )
            self.assertEqual( kuhn_munkres([[7,  53, 183, 439, 863, 497, 383, 563,
                                  79, 973, 287,  63, 343, 169, 583],
                                [627, 343, 773, 959, 943, 767, 473, 103,
                                 699, 303, 957, 703, 583, 639, 913],
                                [447, 283, 463,  29,  23, 487, 463, 993,
                                 119, 883, 327, 493, 423, 159, 743],
                                [217, 623,   3, 399, 853, 407, 103, 983,
                                 89, 463, 290, 516, 212, 462, 350],
                                [960, 376, 682, 962, 300, 780, 486, 502,
                                 912, 800, 250, 346, 172, 812, 350],
                                [870, 456, 192, 162, 593, 473, 915,  45,
                                 989, 873, 823, 965, 425, 329, 803],
                                [973, 965, 905, 919, 133, 673, 665, 235,
                                 509, 613, 673, 815, 165, 992, 326],
                                [322, 148, 972, 962, 286, 255, 941, 541,
                                 265, 323, 925, 281, 601,  95, 973],
                                [445, 721,  11, 525, 473,  65, 511, 164,
                                 138, 672,  18, 428, 154, 448, 848],
                                [414, 456, 310, 312, 798, 104, 566, 520,
                                 302, 248, 694, 976, 430, 392, 198],
                                [184, 829, 373, 181, 631, 101, 969, 613,
                                 840, 740, 778, 458, 284, 760, 390],
                                [821, 461, 843, 513,  17, 901, 711, 993,
                                 293, 157, 274,  94, 192, 156, 574],
                                [34, 124,   4, 878, 450, 476, 712, 914,
                                 838, 669, 875, 299, 823, 329, 699],
                                [815, 559, 813, 459, 522, 788, 168, 586,
                                 966, 232, 308, 833, 251, 631, 107],
                                [813, 883, 451, 509, 615,  77, 281, 613,
                                 459, 205, 380, 274, 302,  35, 805]])[1], 13938 )
        # https://www.youtube.com/watch?v=aPVtIhnwHPE
        self.assertEqual( kuhn_munkres_n3([[62, 78, 50, 101, 82],
                                           [71, 84, 61, 73, 59],
                                           [87, 92, 111, 71, 81],
                                           [48, 64, 87, 77, 80]]),
                          ([3, 1, 2, 4], 376) )
        # test non-symmetrical graphs
        inf = float('inf')
        self.assertEqual( kuhn_munkres_n3([[10, -inf]]),              ([0], 10))
        self.assertEqual( kuhn_munkres_n3([[10]], 0),                 ([0], 10))
        self.assertEqual( kuhn_munkres_n3([[5, 0, 1], [8, 5, 4]], 0), ([0, 1], 10))

    def test_laser_mirrors(self):
        self.assertEqual( laser_mirrors(2, 2, [(0, 0), (0, 1),
                                    (1, 0), (1, 1)]), [1, 0, 1, 0] )
        self.assertEqual( laser_mirrors(7, 8, [(0, 1), (0, 4), (0, 6), (2, 3), (2, 4),
                                    (4, 1), (4, 4), (4, 6), (6, 0), (6, 3),
                                    (6, 4)]) ,[1, None, 0, 0, 1, 1,
                                                 0, 0, None, 1, 0] )
        self.assertEqual( laser_mirrors(5, 4, [(0, 0), (1, 0), (1, 1), (1, 2), (1, 3),
                                    (2, 0), (2, 1), (2, 2), (2, 3), (3, 0),
                                    (3, 1), (3, 2), (3, 3), (4, 0), (4, 1),
                                    (4, 2), (4, 3)]) , None )

    def test_lazy_segment_tree(self):
        for n in [1, 2, 10, 1000]:
            tab = [random.randint(-100, 100) for _ in range(n)]
            tree = LazySegmentTree(tab)
            for t in range(1000):
                i = random.randint(0, n-1)
                j = random.randint(0, n-1)
                v = random.randint(-100, 100)
                if i > j:
                    i, j = j, i
                if t % 2 == 0:
                    tree.set(i, j, v)
                    for k in range(i, j):
                        tab[k] = v
                else:
                    tree.add(i, j, v)
                    for k in range(i, j):
                        tab[k] += v
                if i == j:
                    self.assertEqual(tree.max(i, j), float('-inf'))
                    self.assertEqual(tree.min(i, j), float('+inf'))
                    self.assertEqual(tree.sum(i, j), 0)
                else:
                    self.assertEqual(tree.max(i, j), max(tab[i:j]))
                    self.assertEqual(tree.min(i, j), min(tab[i:j]))
                    self.assertEqual(tree.sum(i, j), sum(tab[i:j]))

    def test_left_right_inversions(self):
        for n in range(1, 12):
            for _ in range(20):
                tab = [random.randint(1,n) for _ in range(n)]
                left, right = left_right_inversions(tab)
                for j in range(n):
                    self.assertEqual(left[j], len([i for i in range(j) if tab[i] > tab[j] ]))
                    self.assertEqual(right[j], len([k for k in range(j+1, n) if tab[k] < tab[j] ]))


    def test_levenshtein(self):
        self.assertEqual( levenshtein("AUDI", "LADA"), 3)
        self.assertEqual( levenshtein("kitten", "sitting"), 3)


    def test_longest_common_subsequence(self):
        self.assertEqual( longest_common_subsequence("GAC", "AGCAT") , "GA" )
        L = "ABCDEFGHI"
        self.assertEqual( longest_common_subsequence(L, L) , L )
        self.assertEqual( longest_common_subsequence(L, "D") , "D" )
        self.assertEqual( len(longest_common_subsequence(L, L[::-1])) , 1 )
        self.assertEqual( len(longest_common_subsequence(L, "X")), 0 )
        self.assertEqual( len(longest_common_subsequence(L, "")) , 0 )
        self.assertEqual( len(longest_common_subsequence("", "")) , 0 )

    def test_longest_increasing_subsequence(self):
        L = list(range(0, 10, 2))
        self.assertEqual(  longest_increasing_subsequence(L) , L )
        self.assertEqual(  longest_increasing_subsequence(L * 2) , L )
        self.assertEqual(  longest_increasing_subsequence(L[::-1]) , [0] )
        self.assertEqual(  longest_increasing_subsequence([]), [] )
        self.assertEqual(  longest_increasing_subsequence([7]) , [7] )
        self.assertEqual(  longest_increasing_subsequence([-2, 4, 4]) ,[-2, 4] )
        self.assertEqual(  longest_increasing_subsequence([4, 4, -2]) , [-2] )
        Q = [3, 1, 4, 1, 5, 9, 2, 6, 5, 4, 5, 3, 9, 7, 9]
        A = [1, 2, 4, 5, 7, 9]
        self.assertEqual(  longest_increasing_subsequence(Q) , A )


    def test_LCA_shortcuts(self):
        nodes = list(range(16))
        prec = [u // 2 for u in nodes]
        prec[0] = 0
        LCA = LowestCommonAncestorShortcuts(prec)
        self.assertEqual( LCA.query(9, 9) , 9 )
        self.assertEqual( LCA.query(9, 0) , 0 )
        self.assertEqual( LCA.query(0, 0) , 0 )
        self.assertEqual( LCA.query(0, 1) , 0 )
        self.assertEqual( LCA.query(1, 1) , 1 )
        self.assertEqual( LCA.query(4, 11) , 2 )

    def test_LCA_RMQ(self):
        graph = [[1], [0, 2, 9], [1, 3, 5], [2, 4], [3],
                 [2, 6, 7, 8], [5], [5], [5], [1]]
        LCA = LowestCommonAncestorRMQ(graph)
        self.assertEqual( LCA.query(3, 7) , 2 )
        self.assertEqual( LCA.query(3, 2) , 2 )
        self.assertEqual( LCA.query(3, 7) , 2 )
        self.assertEqual( LCA.query(9, 4) , 1 )
        self.assertEqual( LCA.query(4, 9) , 1 )
        self.assertEqual( LCA.query(4, 4) , 4 )
        self.assertEqual( LCA.query(3, 4) , 3 )
        self.assertEqual( LCA.query(4, 3) , 3 )
        self.assertEqual( LCA.query(5, 7) , 5 )
        self.assertEqual( LCA.query(7, 5) , 5 )

    def test_majority(self):
        L = ['d', 'd', 'r', 'r', 'x', 'boo']
        self.assertEqual( majority(L), 'd')

    def test_manacher(self):
        self.assertEqual( manacher("a") , (0, 1) )
        self.assertEqual( manacher("aa") , (0, 2) )
        self.assertEqual( manacher("ab") , (1, 2) )
        self.assertEqual( manacher("aba") , (0, 3) )
        self.assertEqual( manacher("baa") , (1, 3) )
        self.assertEqual( manacher("aab") , (0, 2) )
        self.assertEqual( manacher("babcbabcbaccba") , (1, 10) )


    def test_matrix_mult(self):
        dim = [(30, 35), (35, 15), (15, 5), (5, 10), (10, 20), (20, 25)]
        M = []
        for (r, c) in dim:
            M.append([[random.randint(0, 4) for i in range(c)] for j in range(r)])
        opt, arg = matrix_mult_opt_order(M)
        self.assertEqual( opt[0][5] ,15125 )
        self.assertEqual( arg[0][4] , 2 )
        matrix_chain_mult(M)  # just to check that there is no runtime error


    def test_max_interval_intersect(self):
        self.assertEqual( max_interval_intersec([(0, 2)]) , (1, 0) )
        self.assertEqual( max_interval_intersec([]) ,(0, None) )
        self.assertEqual( max_interval_intersec([(0, 2), (2, 4)]) , (1, 0) )
        self.assertEqual( max_interval_intersec([(0, 2), (1, 4)]) , (2, 1) )
        self.assertEqual( max_interval_intersec([(0, 2), (3, 4)]) , (1, 0) )
        self.assertEqual( max_interval_intersec([(0, 2), (0, 6), (1, 5), (2, 5),
                                                 (2, 5), (4, 8), (7, 8)]), (5, 4))


    def test_merge_ordered_lists(self):
        x = range(0, 10, 2)
        y = range(1, 10, 2)
        self.assertEqual( merge(x, y) , list(range(10)) )


    def test_min_mean_cycle(self):
        W0 = [[None, -5,   None, None],
              [None, None, -3,      0],
              [9,    None, None,    2],
              [7,    0,    -1,   None]]
        W1 = [[None, 10, None], [None, -2, None], [None, None, -20]]
        W2 = [[None, 10, 10], [None, -8, -8], [None, -8, -8]]
        W3 = [[None, None], [0, -4]]

        A0 = ([2, 3, 1], -1./3)
        A1 = ([1], -2)
        A2 = ([1], -8)
        A3 = None

        for w, answ in [(W0, A0), (W1, A1), (W2, A2), (W3, A3)]:
            g = matrix_to_listlist(w)
            sparse = listlist_and_matrix_to_listdict(g, w)
            for graph, weight in [(g, w), (sparse, sparse)]:
                self.assertEqual( min_mean_cycle(graph, weight), answ)


    def test_next_permutation(self):
        L = [2,2,0,0,1,1,0]
        self.assertEqual( next_permutation(L), True)
        self.assertEqual(L, [2,2,0,1,0,0,1])
        L = [2,2,1,1,0,0,0]
        self.assertEqual( next_permutation(L), False)
        L = [2]
        self.assertEqual( next_permutation(L), False)
        L = []
        self.assertEqual( next_permutation(L), False)

    def test_OurHeap(self):
        L = [(random.randint(1, 100), i) for i in range(10000)]
        Q = OurHeap(L)
        for _ in range(10000):
            i = random.randint(0, len(L) - 1)
            v = random.randint(1, 100)
            if v == 100:
                v = float('inf')
            Q.update(L[i], (v, i))
            L[i] = (v, i)
        self.assertEqual( sorted(L), [Q.pop() for _ in L])

    def test_OurQueue(self):
        q1 = deque()
        q2 = OurQueue()
        for _ in range(10000):
            self.assertTrue( (q1 and q2 or not q1 and not q2) )
            if random.randint(0, 2) == 0:
                x = random.randint(0, 100)
                q1.append(x)
                q2.push(x)
            else:
                if q1:
                    self.assertEqual( q1.popleft() , q2.pop() )

    def test_permutation_rank(self):
        for n, nfact in [(1, 1), (2, 2), (3, 6), (4, 24)]:
            for r in range(nfact):
                self.assertEqual(permutation_rank(rank_permutation(r, 4)), r)
            self.assertEqual(rank_permutation(0, n), list(range(n)))
            self.assertEqual(rank_permutation(nfact - 1, n), list(range(n))[::-1])


    def test_partition_refinement(self):
        P = PartitionRefinement(10)
        self.assertEqual( P.tolist(), [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]])
        P.refine([3, 4, 5])
        P.refine([2, 3])
        P.refine([-1, 2, 3, 10])
        self.assertEqual( P.tolist(), [[3], [4, 5], [2], [0, 1, 6, 7, 8, 9]])
        flattened = [val for sublist in P.tolist() for val in sublist]
        self.assertEqual(flattened, P.order())


    def test_polygon_area(self):
        self.assertEqual( area([(1, 0), (2, 3), (2, 4), (0, 3)]) , 4 )
        self.assertEqual( area([(1, 1), (2, 1), (2, 2), (1, 2)]), 1 )


    def test_pq_tree(self):

        check_automaton = [[0, 1], [2, 1], [2, 3], [3, 3]]

        def check_positive(sets):
            order = consecutive_ones_property(sets)
            for S in sets:
                state = 0
                for i in order:
                    state = check_automaton[state][int(i in S)]
                    if state == 3:
                        return False
            return True

        self.assertIsNone(consecutive_ones_property([
           {2, 3, 4, 5, 6},
           {3, 6, 7},
           {4, 7}]))
        self.assertTrue(check_positive([
           {2, 3, 4, 5, 6},
           {3, 6, 7},
           {7}]))
        self.assertTrue(check_positive([
           {2, 3, 10},
           {3, 6, 8},
           ]))
        self.assertTrue(check_positive([
           {2, 3, 4},
           {1, 2, 3},
           {4, 5},
           ]))
        self.assertIsNone(consecutive_ones_property([
            {3,4}, {3,4,6}, {3,4,5}, {4,5}, {2,6}, {1,2}, {4,5}, {5,3}]))
        self.assertTrue(check_positive([
            {1,4}, {3,0,2,5,4}, {0,2,5,4}, {2,5}, {0,2}]))


    def test_polygon_is_simple(self):
        # +---+
        # |   |
        # +---+
        self.assertTrue( is_simple([(0, 0), (0, 1), (1, 1), (1, 0)]) )
        # +-------+
        # |       |
        # +---+   |
        #     |   |
        # +---+   |
        # |       |
        # +-------+
        self.assertTrue( is_simple([(0, 0), (0, 1), (1, 1), (1, 2), (0, 2), (0, 3), (2, 3), (2, 0)]) )
        # +-------+
        # |       |
        # +-------+
        #         |
        # +-------+
        # |       |
        # +-------+
        self.assertFalse( is_simple([(0, 0), (0, 1), (2, 1), (2, 2), (0, 2), (0, 3), (2, 3), (2, 0)]) )
        # +-------+
        # |       |
        # +-------+
        # |
        # +-------+
        # |       |
        # +-------+
        self.assertFalse( is_simple([(0, 0), (0, 3), (2, 3), (2, 2), (0, 2), (0, 1), (2, 1), (2, 0)]) )
        #     +---+
        #     |   |
        # +---+---+
        # |   |
        # +---+
        self.assertFalse( is_simple([(0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (2, 1), (1, 1), (1, 0)]) )
        #     +---+
        #     |   |
        # +---+---+---+
        # |           |
        # +-----------+
        self.assertFalse( is_simple([(0, 0), (0, 1), (2, 1), (2, 2), (1, 2), (1, 1), (3, 1), (3, 0)]) )
        # +---+
        # |   |
        # +-------+
        #     |   |
        # +-------+
        # |   |
        # +---+
        self.assertFalse( is_simple([(0, 0), (0, 1), (2, 1), (2, 2), (0, 2), (0, 3), (1, 3), (1, 0)]) )
        # +---+
        # |   |
        # +-----------+
        #     |       |
        #     |   +---+
        #     |   |
        # +-------+
        # |   |
        # +---+
        self.assertFalse( is_simple([(0, 0), (0, 1), (2, 1), (2, 2), (3, 2), (3, 3), (0, 3), (0, 4), (1, 4), (1, 0)]) )
        #     +---+
        #     |   |
        # +-------+
        # |   |
        # +---+
        self.assertFalse( is_simple([(2, 20), (1, 20), (1, 0), (0, 0), (0, 10), (2, 10)]) )
        #     +-------+
        #     |       |
        #     |   +---+
        #     |   |
        # +-------+
        # |   |
        # +---+
        self.assertFalse( is_simple([(0, 0), (0, 1), (2, 1), (2, 2), (3, 2), (3, 3), (1, 3), (1, 0)]) )
        # +---+
        # |   |
        # +-------+
        #     |   |
        #     |   +---+
        #     |       |
        #     +-------+
        self.assertFalse( is_simple([(0, 3), (0, 2), (2, 2), (2, 1), (3, 1), (3, 0), (1, 0), (1, 3)]) )



    def test_tree_adj_to_prec(self):
        graph = [[1], [0, 2, 9], [1, 3, 5], [2, 4], [3], [2, 6, 7, 8],
                 [5], [5], [5], [1]]
        prec = [None, 0, 1, 2, 3, 2, 5, 5, 5, 1]
        self.assertEqual( tree_adj_to_prec(graph) , prec )
        self.assertEqual( tree_prec_to_adj(prec) , graph )
        cycle = [[1, 2], [0, 2], [0, 1]]
        tree_adj_to_prec(cycle)  # test that there is no infinite loop


    def test_our_heap(self):
        L = [(random.randint(1, 100), i) for i in range(10000)]
        Q = OurHeap(L)
        for _ in range(100):
            i = random.randint(0, len(L) - 1)
            v = random.randint(1, 100)
            if v == 100:
                v = float('inf')
            Q.update(L[i], (v, i))
            L[i] = (v, i)
        self.assertEqual(sorted(L), [Q.pop() for _ in L])


    def test_our_queue(self):
        q1 = deque()
        q2 = OurQueue()
        for _ in range(100):
            self.assertEqual(len(q1), len(q2))
            if random.randint(0, 2) == 0:
                x = random.randint(0, 100)
                q1.append(x)
                q2.push(x)
            else:
                if q1:
                    self.assertEqual(q1.popleft(), q2.pop())


    def test_pick(self):
        self.assertEqual(area([(1, 0), (2, 3), (2, 4), (0, 3)]), 4)
        self.assertEqual(area([(1, 1), (2, 1), (2, 2), (1, 2)]), 1)


    def test_powergraph(self):
        """  0  1
             U  U         self-loops
        """
        G1 = [[0], [1]]
        for k in range(1,4):
            self.assertEqual(powergraph(G1, k), G1)
        """  0  1
             U
        """
        G2 = [[0], []]
        self.assertEqual(powergraph(G1, 1), G1)
        self.assertEqual(powergraph(G1, 2), G1)
        """ 0---1---2---4
             \ /        U
              3
        """
        G1 = [[0, 1, 3], [0, 1, 2, 3], [1, 2, 4], [0, 1, 3], [2, 4]]
        """   0---1
              |\ /| \    .
              |/ \|  \   .
              3---2---4
        """
        G2 = [[0, 1, 2, 3], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3], [1, 2, 4]]
        G0 = [[0], [1], [2], [3], [4]]
        self.assertEqual(powergraph(G1, 0), G0)
        self.assertEqual(powergraph(G1, 1), G1)
        self.assertEqual(powergraph(G1, 2), G2)


    def test_predictive_text(self):
        dico = [("another", 5),  ("contest", 6),  ("follow", 3),
                ("give", 13),  ("integer", 6),  ("new", 14),  ("program", 4)]
        prop = predictive_text(dico)
        A = ""
        for seq in ["7764726", "639", "468", "2668437", "7777"]:
            for i in range(len(seq)):
                A += propose(prop, seq[:i + 1]) + " "
        self.assertEqual( A, "p pr pro prog progr progra program n ne new g "\
                    "in int c co con cont anoth anothe another p pr None None ")

    def test_rabin_karp(self):
        # rabin_karp_matching is tested in test_knuth_morris_pratt
        self.assertEqual(rabin_karp_factor("h", "h", 1), (0, 0))
        self.assertEqual(rabin_karp_factor("h", "h", 2), None)
        self.assertEqual(rabin_karp_factor("ab", "ab", 2), (0, 0))
        self.assertEqual(rabin_karp_factor("ab", "ba", 2), None)
        self.assertEqual(rabin_karp_factor("ab", "ba", 1), (0, 1))
        M = 30
        s = "a" * M + "b" * M + "a" * M
        t = "c" * M + "b" * M + "c" * M
        self.assertEqual((rabin_karp_factor(s, t, M)), (M, M))

    def test_range_minimum_query(self):
        for L in [1, 2, 3, 1023, 1024, 1025]:
            T = [random.randint(1, 100) for _ in range(L)]
            R = [(random.randint(0, 1), random.randint(0, L-1), random.randint(0, L-1))
                 for _ in range(1000)]
            S = RangeMinQuery(T)
            for q, i, k in R:
                if q:
                    # if i == k:
                    #     continue
                    if i > k:
                        i, k = k, i
                    if i == k:
                        self.assertEqual(S.range_min(i, k), float('inf'))
                    else:
                        self.assertEqual(S.range_min(i, k), min(T[i:k]))
                else:
                    S[i] = k
                    T[i] = k

    def test_rectangles_from_grid(self):
        R = ["10110111",
             "01000101",
             "11011000",
             "00111010",
             "11011101",
             "01000101"]
        self.assertEqual(rectangles_from_grid(R, noir='1'), (6, 3, 4, 5, 1))


    def test_rectangles_from_histogram(self):
        for L in range(100):
            T = [random.randint(1, 100) for _ in range(L)]
            best = (float('-inf'), 0, 0)
            for j in range(1, L + 1):
                for i in range(j):
                    area = ((j - i) * min(T[i:j]), i, j)
                    if area > best:
                        best = area
            self.assertEqual(best[0], rectangles_from_histogram(T)[0])


    def test_rectangles_from_points(self):
        L = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 2), (3, 1), (2, 0), (1, 0)]
        A = [0, 0, 0, 0, 0, 1, 3, 6]
        while L:
            self.assertEqual(rectangles_from_points(L), A[-1])
            A.pop()
            L.pop()


    def test_roman_numbers(self):
        for val in range(1, 10000):
            self.assertEqual(roman2int(int2roman(val)), val)
        self.assertEqual(int2roman(68), "LXVIII")
        self.assertEqual(int2roman(890), "DCCCXC")


    def test_scalar(self):
        n = 10
        x = list(range(n))
        y = list(range(n))
        random.shuffle(x)
        random.shuffle(y)
        self.assertEqual(min_scalar_prod(x, y), sum(i * (n - 1 - i) for i in range(n)))


    def test_shortest_cycle(self):
        def check(graph, cycle):
            for i in range(len(cycle)):        # check presence of edges
                self.assertTrue(cycle[i - 1] in graph[cycle[i]])

        def matrix_mult(A, B):
            n = len(A)
            C = []
            for i in range(n):
                row = []
                for j in range(n):
                    v = sum(A[i][k] * B[k][j] for k in range(n))
                    row.append(v)
                C.append(row)
            return C

        def has_selfloops(graph):
            for v in range(len(graph)):
                if v in graph[v]:
                    return True
            return False

        """  0---2---3
              \ /
               1
        """
        graph = [[1, 2], [0, 2], [0, 1, 3], [2]]
        cycle = shortest_cycle(graph)
        check(graph, cycle)
        """  0---2---3
                /
               1
        """
        graph = [[2], [2], [0, 1, 3], [2]]
        self.assertIsNone(shortest_cycle(graph))
        for _ in range(100):               # check on some random undirected graphs
          n = 10
          graph = [[] for u in range(n)]   # add random edges to initially empty graph
          G = [[0 for u in range(n)] for v in range(n)]
          for i in range(n * n // 15):     # this edge number makes about half cycle free graphs
              v = random.randint(1, n-1)
              u = random.randint(0, v-1)
              if u in graph[v]:            # do not create multi-edges
                  continue
              graph[u].append(v)
              graph[v].append(u)
              G[u][v] = G[v][u] = 1
          cycle = shortest_cycle(graph)
          M = [[int(u==v) for u in range(n)] for v in range(n)]
          if cycle is None:
              pass  # right now we have no tools to check the absence of a cycle
          else:
              check(graph, cycle)


    def test_strongly_connected_components(self):
        def check(f, G, b):
            a = f(G)
            # self.assertEqual(a, f(listlist_and_matrix_to_listdict(G)))
            # print("sccp(%s)=%s" % (G, a))
            n = len(b)
            C = [None] * n
            for comp in a:
                rep = min(comp)
                for v in comp:
                    C[v] = rep
            self.assertEqual(C, b)

        for f in [tarjan, kosaraju, tarjan_recursif]:
            check(f, [[]], [0])
            check(f, [[0]], [0])
            check(f, [[1], [2], [0]], [0, 0, 0])
            check(f, [[1], [2], []], [0, 1, 2])
            check(f, [[], [0], [1]], [0, 1, 2])
            check(f, [[1], [2], [0, 3], [4], [5], [3]], [0, 0, 0, 3, 3, 3])
            check(f, {0: [1], 1: [2, 3], 2: [4, 5],
                      3: [4, 5], 4: [6], 5: [], 6: []}, [0, 1, 2, 3, 4, 5, 6])
            check(f, {0: [1], 1: [2, 3, 4], 2: [0, 3], 3: [4], 4: [3]},
                  [0, 0, 0, 3, 3])
            n = 100
            G = [[v for v in range(u + 1, min(u + 10, n))] for u in range(n)]
            check(f, G, list(range(n)))
            G[-1].append(0)
            check(f, G, [0] * n)

    def test_subsetsum(self):
        L = [2, 4, 8, 16, 32]
        for subset_sum in [subset_sum1, subset_sum2]:
            self.assertEqual(subset_sum(L, 27), False)
            self.assertEqual(subset_sum(L, 28), True)
        C = [3, 5, 11]
        B = [b for b in range(30) if not coin_change(C, b)]
        self.assertEqual(B, [1, 2, 4, 7])

    def test_sudoku(self):
        T = "*E***D57*0B**F**"\
            "*46C8****9*1**5*"\
            "**7*********2**3"\
            "*0**A******F1*C*"\
            "**4*3A*1********"\
            "*9*****582**40E*"\
            "E*2*F**DA*359***"\
            "8****9*2*E64C7*D"\
            "1*9*73****E*0***"\
            "******FB****8***"\
            "*3*2*6*****9*B*1"\
            "6**BC***5D****9*"\
            "***DB876**C3****"\
            "*****29***5*A**C"\
            "*5*3*C**9*F***4E"\
            "B**********E**62"
        A = "0123456789ABCDEF"
        G = [[] for _ in range(16)]
        for i in range(256):
            r = G[i // 16]
            v = A.find(T[i])
            r.append(v + 1)
        sudoku(G)
        n = int(len(G) ** 0.5)
        all_terms = list(range(1, n * n + 1))
        for line in G:
            self.assertEqual(sorted(line), all_terms)
        for j in range(n * n):
            self.assertEqual(sorted(G[i][j] for i in range(n * n)), all_terms)
        for i in range(n):
            for j in range(n):
                self.assertEqual(sorted(G[n * i + di][n * j + dj] for di in range(n) for dj in range(n)), all_terms)

    def test_ternary_search(self):
        x = ternary_search(lambda x: -x*(x-4), 0, 4)
        self.assertTrue( 1.9 <= x <= 2.1 )
        x = ternary_search(lambda x: x*(x-4), 0, 4)
        self.assertTrue( x <= 0.1 or 3.9 <= x )
        x = ternary_search(lambda x: x, 0, 4)
        self.assertTrue( 3.9 <= x <= 4 )
        x = ternary_search(lambda x: 1, 0, 4)
        self.assertTrue( 0 <= x <= 4 )

    def test_three_partition(self):
        self.assertEqual(three_partition([5, 5, 3, 2]), (1, 2, 12))
        self.assertEqual(three_partition([1, 4, 5, 3, 2]), (3, 4, 24))
        self.assertEqual(three_partition([10, 2, 3]), None)

    def test_topological_order(self):
        n = 100
        G = [[v for v in range(u + 1, min(u + 10, n))] for u in range(n)]
        L = [([], []),
             ([[]], [0]),
             ([[], [0]], [1, 0]),
             ([[1], []], [0, 1]),
             ([[1, 5], [2, 3, 5], [3], [4, 5], [5], []],  [0, 1, 2, 3, 4, 5]),
             (G, list(range(n))  ) ]
        for f in [topological_order_dfs, topological_order]:
            for graph, result in L:
                self.assertEqual(f(graph), result)

    def test_trie(self):
        T = Trie(["as", "porc", "pore", "pre", "pres", "pret"])
        for w, closest in zip(["a", "aas", "ass", "pars", "por", "pes", "pred", "pire", "brzlgrmpf"],
                              ["as", "as", "as", "porc", "porc", "pres", "pres", "pore", "pres"]):
            self.assertEqual(spell_check(T, w), closest)

    def test_two_sat(self):
        def instance_aleatoire(nb_variables, nb_clauses):
            clauses = []
            for _ in range(nb_clauses):
                x = 1 - 2 * random.randint(0, 1) * random.randint(1, nb_variables)
                y = 1 - 2 * random.randint(0, 1) * random.randint(1, nb_variables)
                clauses.append((x, y))
            return clauses

        def check(formula, affectations):
            for x, y in formula:
                if x > 0:
                    vx = affectations[x - 1]
                else:
                    vx = not affectations[-x - 1]
                if y > 0:
                    vy = affectations[y - 1]
                else:
                    vy = not affectations[-y - 1]
                self.assertTrue(vx or vy)

        def verify(formula, satisfiable):
            affectations = two_sat(formula)
            if not satisfiable:
                self.assertIsNone(affectations)
            else:
                self.assertIsNotNone(affectations)
                check(formula, affectations)

        verify([(2, 2)], True)
        verify([(-1, 1)], True)

        verify([[2, -1], [-3, -3], [3, -2], [2, 2]], False)
        verify([[3, -2], [3, 2], [2, -2], [-1, -1]], True)
        verify([(-1, 2), (-1, 3), (-2, -1), (-2, 3)], True)
        verify([(-1, 2), (-2, -1), (1, 3), (-3, 4), (-3, 2), (-4, 1)], False)
        for _ in range(5):
            formula = instance_aleatoire(100, 100)
            aff = two_sat(formula)
            if aff:
                check(formula, aff)

    def test_union_rectangles(self):
        R = [(0, 0, 3, 5), (1, 3, 2, 4), (0, 2, 5, 4), (4, 0, 6, 2), (7, 2, 10, 3)]
        self.assertEqual(union_rectangles([]), 0)
        self.assertEqual(union_rectangles([(0, 0, 5, 10)]), 50)
        self.assertEqual(union_rectangles(R), 26)

    def test_windows_k_distinct(self):
        L = [("abbaca", 2), ("abbaca", 1), ("abbabacccabaabaccacab", 2)]
        for x, k in L:
            for i, j in windows_k_distinct(x, k):
                self.assertEqual(len(set(x[i:j])), k)
                if i>0:
                    self.assertFalse(len(set(x[i-1:j])) == k)
                if j<len(x):
                    self.assertFalse(len(set(x[i:j+1])) == k)

    def test_graph_conversion(self):
        Gdd = {'A': {'B': 7}, 'B': {'A': 6, 'B': 1, 'C': 0,  'D': -1}, 'C': {}, 'D':{'C': 8}}
        Gld, name2node, node2name = dictdict_to_listdict(Gdd)
        self.assertEqual(Gld, [{1: 7}, {0: 6, 1: 1, 2: 0, 3: -1}, {}, {2: 8}])
        self.assertEqual(node2name, ['A', 'B', 'C', 'D'])
        self.assertEqual(name2node, {'A': 0, 'B': 1, 'C': 2, 'D': 3})
        Gll, W = listdict_to_listlist_and_matrix(Gld)
        self.assertEqual(Gll, [[1], [0, 1, 2, 3], [], [2]])
        self.assertEqual(W, [[None, 7, None, None], [6, 1, 0, -1], [None, None, None, None], [None, None, 8, None]])
        Hld = listlist_and_matrix_to_listdict(Gll, W)
        self.assertEqual(Hld, Gld)
        Hll = matrix_to_listlist(W)
        self.assertEqual(Hll, Gll)

    def test_SortedSet(self):
        s1 = set()
        s2 = SortedSet()
        for _ in range(50):
            i = random.randint(0, 20)
            try:
                nK = next(k for k in sorted(s1) if k >= i)
            except StopIteration:
                nK = None
            self.assertEqual(s2.nextKey(i), nK)
            try:
                lK = next(k for k in reversed(sorted(s1)) if k < i)
            except StopIteration:
                lK = None
            self.assertEqual(s2.lastKey(i), lK)
            if i in s1:
                for s in (s1, s2):
                    s.remove(i)
            else:
                for s in (s1, s2):
                    s.add(i)
            self.assertEqual(set(s2), s1)

    def test_SortedDict(self):
        d1 = dict()
        d2 = SortedDict()
        for _ in range(50):
            i = random.randint(0, 20)
            j = random.randint(0, 20)
            for d in (d1, d2):
                d[i] = j
            self.assertEqual(dict(d2), d1)


if __name__ == '__main__':
    unittest.main()

