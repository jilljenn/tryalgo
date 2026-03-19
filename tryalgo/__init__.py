#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""\
TryAlgo package

A collection of algorithms and data structures implemented in Python.

jill-jênn vie et christoph dürr - 2025
"""

from .a_star import a_star
from .anagrams import anagrams
from .arithm_expr_eval import arithm_expr_eval, arithm_expr_parse
from .arithm_expr_target import arithm_expr_target
from .arithm import pgcd, bezout, inv, binom, binom_modulo
from .bellman_ford import bellman_ford, bellman_ford2
from .bfs import bfs, bfs_implicit
from .biconnected_components import cut_nodes_edges, cut_nodes_edges2
from .binary_search import (discrete_binary_search, continuous_binary_search,
                            optimized_binary_search_lower,
                            optimized_binary_search, ternary_search)
from .bipartite_matching import max_bipartite_matching
from .bipartite_vertex_cover import bipartite_vertex_cover
from .closest_points import closest_points
from .closest_values import closest_values
from .convex_hull import andrew, left_turn
from .dancing_links import dancing_links
from .dfs import (dfs_recursive, dfs_iterative, dfs_tree, dfs_grid_recursive,
                  dfs_grid, find_cycle, is_bipartite)
from .dijkstra import dijkstra, dijkstra_update_heap
from .dilworth import dilworth
from .dinic import dinic
from .dist_grid import dist_grid
from .dyn_prog_tricks import (dyn_prog_Monge, decode_root_matrix_to_level,
                              opt_bin_search_tree1, opt_bin_search_tree2)
from .edmonds_karp import edmonds_karp
from .eulerian_tour import (eulerian_tour_undirected, eulerian_tour_directed,
                            write_cycle, random_eulerien_graph,
                            is_eulerian_tour_directed,
                            is_eulerian_tour_undirected)
from .fast_exponentiation import fast_exponentiation, fast_exponentiation2
from .fenwick import Fenwick, FenwickMin
from .fft import pad, fft, inv_fft, mul_poly_fft
from .floyd_warshall import floyd_warshall, floyd_warshall2
from .ford_fulkerson import ford_fulkerson
from .freivalds import freivalds
from .gale_shapley import gale_shapley
from .gauss_jordan import (gauss_jordan, GJ_ZERO_SOLUTIONS, GJ_SINGLE_SOLUTION,
                           GJ_SEVERAL_SOLUTIONS, diagonalize)
from .graph import(GraphNamedVertices, Graph, make_flow_labels, extract_path,
                   dictdict_to_listdict, listlist_and_matrix_to_listdict,
                   listdict_to_listlist_and_matrix, matrix_to_listlist,
                   add_reverse_arcs, tree_adj_to_prec, tree_prec_to_adj,
                   write_graph, read_graph, readtab, readval)
from .graph01 import dist01
from .hamiltonian_cycle import hamiltonian_cycle
from .horn_sat import horn_sat
from .huffman import huffman, extract
from .interval_cover import interval_cover
from .interval_tree import interval_tree, intervals_containing
from .intervals_union import intervals_union
from .karatsuba import eval_poly, add_poly, sub_poly, mul_poly
from .knapsack import knapsack, knapsack2
from .knuth_morris_pratt import (maximum_border_length, knuth_morris_pratt,
                                 powerstring_by_border, powerstring_by_find)
from .kruskal import kruskal
from .kuhn_munkres_n4 import kuhn_munkres as kuhn_munkres_n4
from .kuhn_munkres import kuhn_munkres
from .laser_mirrors import laser_mirrors
from .left_right_inversions import left_right_inversions
from .levenshtein import levenshtein
from .longest_common_subsequence import longest_common_subsequence
from .longest_increasing_subsequence import longest_increasing_subsequence
from .lowest_common_ancestor import (LowestCommonAncestorShortcuts,
                                     LowestCommonAncestorRMQ)
from .majority import majority
from .manacher import manacher
from .matrix_chain_mult import matrix_mult_opt_order, matrix_chain_mult
from .max_interval_intersec import max_interval_intersec
from .merge_ordered_lists import merge
from .min_mean_cycle import min_mean_cycle
from .next_permutation import next_permutation, solve_word_addition
from .our_heap import OurHeap
from .our_queue import OurQueue
from .our_std import readint, readstr, readarray, readmatrix
from .pareto import pareto2d, pareto3d
from .partition_refinement import PartitionRefinement
from .PC_tree import PC_tree
from .permutation_rank import permutation_rank, rank_permutation
from .polygon import area, is_simple
from .predictive_text import predictive_text, propose
from .primes import eratosthene, gries_misra
from .rabin_karp import rabin_karp_matching, rabin_karp_factor
from .range_minimum_query import RangeMinQuery, LazySegmentTree
from .rectangles_from_grid import rectangles_from_grid
from .rectangles_from_histogram import rectangles_from_histogram
from .rectangles_from_points import rectangles_from_points
from .roman_numbers import roman2int, int2roman
from .Sequence import Sequence
from .scalar import min_scalar_prod
from .shortest_cycle import shortest_cycle, powergraph
from .skip_list import SortedSet, SortedDict
from .strongly_connected_components import (tarjan_recursif, tarjan,
                                            kosaraju, reverse)
from .subsetsum_divide import (part_sum, subset_sum as subset_sum_divide,
                               part_sum2, subset_sum2)
from .subsetsum import subset_sum as subset_sum_basic, coin_change
from .sudoku import sudoku
from .suffix_array import sort_class, sort_cyclic_shifts, suffix_array
from .three_partition import three_partition
from .topological_order import topological_order_dfs, topological_order
from .tortoise_hare import tortoise_hare
from .trie import Trie, add, spell_check, search, TrieNode
from .two_sat import two_sat
from .union_rectangles import (union_rectangles_fast, union_rectangles_fastest,
                               rectangles_contains_point,
                               union_rectangles_naive, union_rectangles)
from .windows_k_distinct import windows_k_distinct

__all__ = ['a_star', 'anagrams', 'arithm_expr_eval', 'arithm_expr_parse',
           'arithm_expr_target', 'pgcd', 'bezout', 'inv', 'binom',
           'binom_modulo', 'bellman_ford', 'bellman_ford2', 'bfs',
           'bfs_implicit', 'cut_nodes_edges', 'cut_nodes_edges2',
           'discrete_binary_search', 'continuous_binary_search',
           'optimized_binary_search_lower','optimized_binary_search',
           'ternary_search', 'max_bipartite_matching',
           'bipartite_vertex_cover', 'closest_points', 'closest_values',
           'andrew', 'left_turn', 'dancing_links', 'dfs_recursive',
           'dfs_iterative', 'dfs_tree', 'dfs_grid_recursive', 'dfs_grid',
           'find_cycle', 'is_bipartite', 'dijkstra', 'dijkstra_update_heap',
           'dilworth', 'dinic', 'dist_grid', 'dyn_prog_Monge',
           'decode_root_matrix_to_level', 'opt_bin_search_tree1',
           'opt_bin_search_tree2', 'edmonds_karp', 'eulerian_tour_undirected',
           'eulerian_tour_directed', 'write_cycle', 'random_eulerien_graph',
           'is_eulerian_tour_directed', 'is_eulerian_tour_undirected',
           'fast_exponentiation', 'fast_exponentiation2', 'Fenwick',
           'FenwickMin', 'pad', 'fft', 'inv_fft', 'mul_poly_fft',
           'floyd_warshall', 'floyd_warshall2', 'ford_fulkerson', 'freivalds',
           'gale_shapley', 'gauss_jordan', 'GJ_ZERO_SOLUTIONS',
           'GJ_SINGLE_SOLUTION', 'GJ_SEVERAL_SOLUTIONS', 'diagonalize',
           'GraphNamedVertices', 'Graph', 'make_flow_labels', 'extract_path',
           'dictdict_to_listdict', 'listlist_and_matrix_to_listdict',
           'listdict_to_listlist_and_matrix', 'matrix_to_listlist',
           'add_reverse_arcs', 'tree_adj_to_prec', 'tree_prec_to_adj',
           'write_graph', 'read_graph', 'readtab', 'readval', 'dist01',
           'hamiltonian_cycle', 'horn_sat', 'huffman', 'extract',
           'interval_cover', 'interval_tree', 'intervals_containing',
           'intervals_union', 'eval_poly', 'add_poly', 'sub_poly', 'mul_poly',
           'knapsack', 'knapsack2', 'maximum_border_length',
           'knuth_morris_pratt', 'powerstring_by_border',
           'powerstring_by_find', 'kruskal', 'kuhn_munkres_n4', 'kuhn_munkres',
           'laser_mirrors', 'left_right_inversions', 'levenshtein',
           'longest_common_subsequence', 'longest_increasing_subsequence',
           'LowestCommonAncestorShortcuts', 'LowestCommonAncestorRMQ',
           'majority', 'manacher', 'matrix_mult_opt_order',
           'matrix_chain_mult', 'max_interval_intersec', 'merge',
           'min_mean_cycle', 'next_permutation', 'solve_word_addition',
           'OurHeap', 'OurQueue', 'readint', 'readstr', 'readarray',
           'readmatrix', 'pareto2d', 'pareto3d', 'PartitionRefinement',
           'PC_tree', 'permutation_rank', 'rank_permutation', 'area',
           'is_simple', 'predictive_text', 'propose', 'eratosthene',
           'gries_misra', 'rabin_karp_matching', 'rabin_karp_factor',
           'RangeMinQuery', 'LazySegmentTree', 'rectangles_from_grid',
           'rectangles_from_histogram', 'rectangles_from_points', 'roman2int',
           'int2roman', 'Sequence', 'min_scalar_prod', 'shortest_cycle',
           'powergraph', 'SortedSet', 'SortedDict', 'tarjan_recursif',
           'tarjan', 'kosaraju', 'reverse', 'part_sum', 'subset_sum_divide',
           'part_sum2', 'subset_sum2', 'subset_sum_basic', 'coin_change',
           'sudoku', 'sort_class', 'sort_cyclic_shifts', 'suffix_array',
           'three_partition', 'topological_order_dfs', 'topological_order',
           'tortoise_hare', 'Trie', 'add', 'spell_check', 'search', 'TrieNode',
           'two_sat', 'union_rectangles_fast', 'union_rectangles_fastest',
           'rectangles_contains_point', 'union_rectangles_naive',
           'union_rectangles', 'windows_k_distinct']
