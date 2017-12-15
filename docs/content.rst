Content of the library
----------------------

The main purpose of this library is to present easy-to-implement-algorithms.  So priority was put on simplicity and readability, rather than on efficiency for example.  For example even though Dijkstra's shortest path algorithm has the best worst case time complexity when implemented with a Fibonacci heap, we choose simpler implementations, which have worse but still acceptable time complexities.

The content of `our library <tryalgo/tryalgo.html#module-tryalgo.freivalds>`__ is organized by problem classes as follows.

Basic algorithms and data structures
::::::::::::::::::::::::::::::::::::

We illustrate how to read from standard input and write to standard output, using Freivald's test, see `freivalds <tryalgo/tryalgo.html#module-tryalgo.freivalds>`__.  Given n by n matrices A,B,C the goal is to decide whether AB=C.  A naive test would have a time complexity of :math:`O(n^3)`.  But `Freivald's test <https://en.wikipedia.org/wiki/Freivalds%27_algorithm>`_, generates a random vector x and tests in time :math:`O(n^2)` if :math:`ABx=Cx`.  It can be shown that the probability that the tests fails to detect difference in AB and in C is negligibly small.

A simple implementation of a first-in-first-out queue is presented in `our_queue <tryalgo/tryalgo.html#module-tryalgo.our_queue>`__, as well as of a heap in `our_heap <tryalgo/tryalgo.html#module-tryalgo.our_heap>`__.

The `union-find structure <https://en.wikipedia.org/wiki/Disjoint-set_data_structure>`_ permits to maintain a partitioning of n items (typically vertices of a graph), and implements the operation :code:`union(x,y)` to merge the two sets containing x and y, as well as :code:`find(x)` to return a canonical element of the set containing x. It is implemented in `kruskal <tryalgo/tryalgo.html#module-tryalgo.kruskal>`__.

Python orders tuples lexicographically. We illustrate this in `majority <tryalgo/tryalgo.html#module-tryalgo.majority>`__ with a small example identifying a majority element in a given list.  It is quite simple to sort a list in python, we illustrate this in `closest_values <tryalgo/tryalgo.html#module-tryalgo.closest_values>`__ a small example identifying two closest values of a given list.

The `sweepline algorithmic technique <https://en.wikipedia.org/wiki/Sweep_line_algorithm>`_ is important for many computational geometric problems. In `max_interval_intersec <tryalgo/tryalgo.html#module-tryalgo.max_interval_intersec>`__ we illustrate it on the problem of computing a value that is contained in a maximum number of intervals among a given set of intervals.

Other important techniques, include the greedy algorithm, which we illustrate in `scalar <tryalgo/tryalgo.html#module-tryalgo.scalar>`__ on the problem of permuting a vector x, so to minimize the scalar product with a given vector y.

Sometimes it is convenient to encode sets over a small universe as bit vectors in integers.  We illustrate this technique on the problem of generating an arithmetic expression with a small given set of values to reach as close as possible some target value, see `arithm_expr_target <tryalgo/tryalgo.html#module-tryalgo.arithm_expr_target>`__.

In `binary_search <tryalgo/tryalgo.html#module-tryalgo.binary_search>`__ we illustrate different variants of binary search or variants.  For example ternary_search permits to find the maximum of a bitonic function in logarithmic time in the size of the search interval.

A very interesting data structure is called `PartitionRefinement <tryalgo/tryalgo.html#module-tryalgo.partition_refinement>`.  It maintains a partition over the set {0,1,...,n-1}.  The main operation is called *refine(S)* which splits each part P of the current partition into elements that are in S and elements that are not in S.  The complexity of this operation is linear in the size of S.

Strings
:::::::

A word x is an `anagram <https://en.wikipedia.org/wiki/Anagram>`_ of a word y, if the letters of x can be permuted to form y.  In `anagrams <tryalgo/tryalgo.html#module-tryalgo.anagrams>`__ we show how to detect all anagrams among a given list of words.

The generation of mobile phone which existed before the smart phones had the possibility to type text messages with the keys 2 to 9, using a letter to digit mapping printed on the keys.  The phone predicted which was the most likely word that the user wants to type using a frequency augmented dictionary of words.  In `predictive_text <tryalgo/tryalgo.html#module-tryalgo.predictive_text>`__ we show how this can be done efficiently.

An elegant but not so well known algorithm by Manacher permits to detect all palindromes which are substrings of a given string, see `manacher <tryalgo/tryalgo.html#module-tryalgo.manacher>`__.

A well studied problems on strings, is the problem of finding a searching a string t inside a string s.  This is generally solved using the algorithm by Knuth-Morris-Pratt.  In addition to `knuth_morris_pratt <tryalgo/tryalgo.html#module-tryalgo.knuth_morris_pratt>`__  we show in `knuth_morris_pratt_border <tryalgo/tryalgo.html#module-tryalgo.knuth_morris_pratt_border>`__ how to compute the `longest border <http://algorithmsforcontests.blogspot.fr/2012/08/borders-of-string.html>`_ for each prefix of a  given string w.  An application is to compute for a string x the largest power k such that there is a string y, and x is the result of concatenating k copies of y.

An alternative algorithm for the string matching problem has been given by `Rabin-Karp <https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm>`_, see `rabin_karp <tryalgo/tryalgo.html#module-tryalgo.rabin_karp>`__.  This algorithm has the advantage of generalizing to searching for multiple strings, or to search patterns in 2-dimensions, or even to find the longest common substring to two given strings.

A `trie <https://en.wikipedia.org/wiki/Trie>`_, or prefix tree is a data structure storing a set of words, which permits to search for a given word, allowing spelling errors.  This is the data-structure one needs in a spell checker. Our implementation is in `trie <tryalgo/tryalgo.html#module-tryalgo.trie>`__.

Sequences and Arrays
::::::::::::::::::::

Many problem on sequences (which are basically strings) can be solved with dynamic programming.
A classical example is the computation of the `edit distance <https://en.wikipedia.org/wiki/Edit_distance>`_ (also called Levenshtein distance) between two given strings, see `levenshtein <tryalgo/tryalgo.html#module-tryalgo.levenshtein>`__.  Other examples include the longest common subsequence (`longest_common_subsequence <tryalgo/tryalgo.html#module-tryalgo.longest_common_subsequence>`__) and the longest increasing subsequence (`longest_increasing_subsequence <tryalgo/tryalgo.html#module-tryalgo.longest_increasing_subsequence>`__).

A very easy problem consisting of computing the sorted union of two given sorted lists, see `merge_ordered_lists <tryalgo/tryalgo.html#module-tryalgo.merge_ordered_lists>`__.  In the area of caching it is interesting to compute maximal time intervals, where no cache fault happened. For this purpose one is given a list of items, and need to identify all inclusion wise maximal intervals that contain at most k distinct items.  This problem is solved with the sliding window technique, which we illustrate in `windows_k_distinct <tryalgo/tryalgo.html#module-tryalgo.windows_k_distinct>`__.

A data structure for an array is an object that stores the array (possibly in an implicit manner) and allows access and modification to the array, as well as different query operations.  For example the range minimum query structure permits to modify individual items of an array and to query the minimum in a given interval of indices.  This is solved generally with a segment tree, allowing logarithmic complexity (in the array size) for these operations, see `range_minimum_query <tryalgo/tryalgo.html#module-tryalgo.range_minimum_query>`__.  There is a cute variant — called `LazySegmentTree` — which allows updates over index ranges, setting to a value or adding a value, and at the same time allows queries over index ranges, asking for the maximum, the minimum or the sum.

A similar structure is the `Fenwick tree <https://en.wikipedia.org/wiki/Fenwick_tree>`_ also called BIT or binary indexed tree. It permits again to modify individual items of the array, but also to query the sum over a given interval of indices, see `fenwick <tryalgo/tryalgo.html#module-tryalgo.fenwick>`__.

Intervals
:::::::::

The tryalgo library covers two nice problems on intervals. The first one is a data structure called `interval tree <https://en.wikipedia.org/wiki/Interval_tree>`_, which stores a set of intervals and permits to select all those that contain a given value, see `interval_tree <tryalgo/tryalgo.html#module-tryalgo.interval_tree>`__.

The other problem consists in finding a smallest hitting set for a given set of intervals, that is to find a smallest set of values, that intersect each interval.  This problem is solved with the sweep line technique mentioned above, see `interval_cover <tryalgo/tryalgo.html#module-tryalgo.interval_cover>`__.

Graphs
::::::

For this library we decided to encode graphs using in two different manners, at your convenience.
In the `adjacency list` a graph on n vertices is encoded as a list of n elements, where the i-th element is the adjacency list of the i-th vertex.  Labels on edges or on vertices are stored in separate matrices or lists.  We call it the *listlist* graph format.  In contrast in the `adjacency dictionary` a graph is encoded as a list of n dictionary, such that the keys of the i-th dictionary are the neighbors of the i-th vertex, and the values are the attached edge weights.  We call this one the *listdict* graph format.  Undirected graphs are represented as directed graphs by duplicating each edge into two opposite facing arcs.  All functions in our library work with the *listlist* graph format, and most work also with the *listdict* graph format. This is documented for each function.


Some graph libraries, like `PADS <https://www.ics.uci.edu/~eppstein/PADS/>`_, choose to represent graphs as dictionaries, where :code:`graph[u]` would again be a dictionary mapping each neighbor :code:`v` to the arc weight :code:`graph[u][v]`.  In this representation, nodes can be any hashable objects, like strings for example, or tuples. We call it the *dictdict* graph format, and provide functions to convert between the different graph representations, namely
`matrix_to_listlist  <tryalgo/tryalgo.html#module-tryalgo.graph>`__,
`listlist_and_matrix_to_listdict  <tryalgo/tryalgo.html#module-tryalgo.graph>`__,
`listdict_to_listlist_and_matrix  <tryalgo/tryalgo.html#module-tryalgo.graph>`__,
`dictdict_to_listdict  <tryalgo/tryalgo.html#module-tryalgo.graph>`__.


We use several representations for trees.  A tree can be represented as an adjacency table, as a graph.  In case the tree is rooted, it can be represented in form of a node structure that contains references to descendant nodes, or in form of an antecedent table, storing at index i the antecedent vertex of the i-th vertex in the tree, using `None` for the root.

In `graph <tryalgo/tryalgo.html#module-tryalgo.graph>`__ we provide several helper functions to read a graph from a file, or to write it into a file in the `DOT format <http://www.graphviz.org/>`_.  This module contains also functions to convert between different tree representations and between graph representations.

Important operations on graphs are explorations along the edges, for examples to detect connected components, or shortest paths.  The depth first search is implemented in `dfs <tryalgo/tryalgo.html#module-tryalgo.dfs>`__, and illustrated in its iterative and recursive form, as well as the special case of exploring grids.  The breadth-first search is implemented in `bfs <tryalgo/tryalgo.html#module-tryalgo.bfs>`__.

The problem of detecting the connected components in a graph is best solved using Kruskal's algorithm, see `kruskal <tryalgo/tryalgo.html#module-tryalgo.kruskal>`__.

A cut vertex is a vertex which removal splits a connected components.  A cut edge is defined similarly.  Detecting cut vertices and cut edges is important in order to determine `biconnected components <https://en.wikipedia.org/wiki/Biconnected_component>`_, which are particular vertex sets such that each pair of vertices is connected by two vertex disjoint paths.  These sets are important for communication networks.  A subtle modification of the depth first search permits to detect these cut vertices and cut edges, see `biconnected_components <tryalgo/tryalgo.html#module-tryalgo.biconnected_components>`__.

For directed graphs there are two important problems.  The first one is the `topological sorting <https://en.wikipedia.org/wiki/Topological_sorting>`_, which consists in ordering the vertices, such that every arc points only from left to right, see `topological_order <tryalgo/tryalgo.html#module-tryalgo.topological_order>`__.

Another important problem consists in determining strongly connected components, which are vertex sets such that for each vertex pair there is a directed path connecting them.  These can be computed by an algorithm by Tarjan or by an algorithm by Kosaraju, see `strongly_connected_components <tryalgo/tryalgo.html#module-tryalgo.strongly_connected_components>`__.  The main application is the resolution of 2-SAT boolean formulas, see `two_sat <tryalgo/tryalgo.html#module-tryalgo.two_sat>`__.
Another polynomial variant of SAT is Horn-SAT, see  `horn_sat <tryalgo/tryalgo.html#module-tryalgo.horn_sat>`__.

Cycles
::::::

The library contains implementations of 4 cycle finding algorithms.  The most basic problem consists of finding any cycle in a given undirected graph.  In the second problem we are given an edge weighted graph and want to compute a cycle of minimum total weight. For the third problem we want to minimize the total cycle weight over the cycle length. And in the last problem we want to find a cycle that visits every edge exactly once.

=========================== ========== ======================= ============================================================================== ===============
problem                     graph      complexity              algorithm                                                                      implementation
=========================== ========== ======================= ============================================================================== ===============
find a cycle                undirected :math:`O(|V| + |E|)`    depth-first search                                                             `find_cycle <tryalgo/tryalgo.html#module-tryalgo.dfs>`__
shortest cycle              undirected :math:`O(|V|\cdot|E|)`  breath-first search                                                            `shortest_cycle <tryalgo/tryalgo.html#module-tryalgo.shortest_cycle>`__
minimum weight cycle        directed   :math:`O(|V|\cdot |E|)` `Bellman-Ford <https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm>`_ `bellman_ford <tryalgo/tryalgo.html#module-tryalgo.bellman_ford>`__
minimum mean cycle          directed   :math:`O(|V|\cdot |E|)` `Karp <http://www.sciencedirect.com/science/article/pii/0012365X78900110>`_    `min_mean_cycle <tryalgo/tryalgo.html#module-tryalgo.min_mean_cycle>`__
Eulerian cycle              both       :math:`O(|V|+|E|)`      `Greedy <https://en.wikipedia.org/wiki/Eulerian_path>`_                        `eulerian_tour <tryalgo/tryalgo.html#module-tryalgo.eulerian_tour>`__
=========================== ========== ======================= ============================================================================== ===============


Shortest paths
::::::::::::::

Several shortest path algorithms are included in the library, which apply for different classes of graphs.  They are summarized in the following table. For the complexity indication we assume that :math:`|E|\geq |V|`.

============================ ======================== ============================================================================== ===============
problem                      complexity               algorithm                                                                      implementation
============================ ======================== ============================================================================== ===============
unweighted graph             :math:`O(|E|)`           `breadth-first search <https://en.wikipedia.org/wiki/Breadth-first_search>`_   `bfs <tryalgo/tryalgo.html#module-tryalgo.bfs>`__
grid                         :math:`O(|E|)`           breadth-first search adapted to the grid graph                                 `dist_grid <tryalgo/tryalgo.html#module-tryalgo.dist_grid>`__
{0,1} weighted graph         :math:`O(|E|)`           `Dijkstra with a deque <http://goo.gl/w67Hs1>`_                                `graph01 <tryalgo/tryalgo.html#module-tryalgo.graph01>`__
non negative weighted graph  :math:`O(|E| \log |V|)`  `Dijkstra <https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm>`_             `dijkstra <tryalgo/tryalgo.html#module-tryalgo.dijkstra>`__
arbitrary weighted graph     :math:`O(|E| \cdot |V|)` `Bellman-Ford`_                                                                `bellman_ford <tryalgo/tryalgo.html#module-tryalgo.bellman_ford>`__
all source destination pairs :math:`O(|V|^3)`         `Floyd-Warshall <https://en.wikipedia.org/wiki/Floyd-Warshall_algorithm>`_     `floyd_warshall <tryalgo/tryalgo.html#module-tryalgo.floyd_warshall>`__
============================ ======================== ============================================================================== ===============


Matching, flows and related
:::::::::::::::::::::::::::

======================================================== ============================== ============================================================================== ===========================
problem                                                  complexity                     algorithm                                                implementation
======================================================== ============================== ============================================================================== ===========================
maximum cardinality bipartite matching                   :math:`O(|E|\cdot|V|)`         `augmenting path algorithm <https://goo.gl/lGtp9f>`_                           `bipartite_matching <tryalgo/tryalgo.html#module-tryalgo.bipartite_matching>`__
minimum bipartite vertex cover                           :math:`O(|E|\cdot|V|)`         `reduction to matching <goo.gl/AkBUQH>`_                                       `bipartite_vertex_cover <tryalgo/tryalgo.html#module-tryalgo.bipartite_vertex_cover>`__
maximum profit bipartite matching                        :math:`O(|U|^2|V|)`            `Hungarian algorithm <https://en.wikipedia.org/wiki/Hungarian_algorithm>`_     `kuhn_munkres <tryalgo/tryalgo.html#module-tryalgo.kuhn_munkres>`__
stable bipartite matching                                :math:`O(|V|^2)`               `Gale-Shapley <https://en.wikipedia.org/wiki/Stable_marriage_problem>`_        `gale_shapley <tryalgo/tryalgo.html#module-tryalgo.gale_shapley>`__
max flow capacities in {1,...,C}                         :math:`O(|V|\cdot|E|\cdot|C|)` `Ford-Fulkerson <https://en.wikipedia.org/wiki/Ford-Fulkerson_algorithm>`_     `ford_fulkerson <tryalgo/tryalgo.html#module-tryalgo.ford_fulkerson>`__
max flow arbitrary capacities                            :math:`O(|V|\cdot|E|^2)`       `Edmonds-Karp <https://en.wikipedia.org/wiki/Edmonds-Karp_algorithm>`_         `edmonds_karp <tryalgo/tryalgo.html#module-tryalgo.edmonds_karp>`__
max flow arbitrary capacities                            :math:`O(|V|^2\cdot|E|)`       `Dinic <https://en.wikipedia.org/wiki/Dinic%27s_algorithm>`_                   `dinic <tryalgo/tryalgo.html#module-tryalgo.dinic>`__
minimum paths decomposition of a directed acyclic graph  :math:`O(|E|\cdot|V|)`         `Dilworth <https://en.wikipedia.org/wiki/Dilworth%27s_theorem>`_               `dilworth <tryalgo/tryalgo.html#module-tryalgo.dilworth>`__
======================================================== ============================== ============================================================================== ===========================


Trees
:::::

A classical example of a problem solved by the greedy algorithm is the problem of constructing optimal `Huffman codes <https://en.wikipedia.org/wiki/Huffman_coding>`_.  An implementation can be found in the module `huffman <tryalgo/tryalgo.html#module-tryalgo.huffman>`__.

Another example, which is as classical and famous, is the problem of constructing a `minimum weight spanning tree <https://en.wikipedia.org/wiki/Minimum_spanning_tree>`_ for a given edge weighted connected graph.  It is solved with the greedy Kruskal's algorithm, see `kruskal <tryalgo/tryalgo.html#module-tryalgo.kruskal>`__.

The lowest common ancestor problem consists of building a data structure that stores a rooted tree and can answer efficiently queries of the form: "Which vertex is the closest common ancestor to two given vertices".  The most elegant solution consists in a reduction to the minimum range query problem, see `lowest_common_ancestor <tryalgo/tryalgo.html#module-tryalgo.lowest_common_ancestor>`__.


Sets
::::

A simple data structure to store an ordered set allowing insertions and deletions is the `skip tree <tryalgo/tryalo.html#module-tryalgo.skip_tree>`__. The expected cost of an update is :math:`O(\log n)`.

Many problems defined on sets can be solved by dynamic programming. This is the case of the `Knapsack problem <https://en.wikipedia.org/wiki/Knapsack_problem>`_. We are given n items, each has a size and a value, and we wish to find a subset of maximum total value which size does not exceed a given capacity C.  This problem is NP-hard, but can be solved efficiently in time O(nC) if the capacity is bounded by a small value, see `knapsack <tryalgo/tryalgo.html#module-tryalgo.knapsack>`__.

In the coin change problem, we are given a collection of coins of n different values and unbounded number of coins for each value and a target value C.  The goal is to find a set of coins of total value C.  Again this problem can be solved by dynamic programming in time O(nC), see `subsetsum <tryalgo/tryalgo.html#module-tryalgo.subsetsum>`__.  A similar problem is called the `subset sum problem <https://en.wikipedia.org/wiki/Subset_sum_problem>`_ and consists of finding a subset out of n given values that sum up to a target value C.  It can be solved with the same method.  When n is small and C large, there is a different algorithm with complexity :math:`O(n^{\lceil n/2 \rceil})`, see `subsetsum_divide <tryalgo/tryalgo.html#module-tryalgo.subsetsum_divide>`__.

An interesting problem with sets, which has also a connection with intervals graphs, consists in finding a total order on a ground set such that every given subset is consecutive in this ground set. This problem can be solved using `PQ trees <tryalgo/tryalgo.html#module-tryalgo.pq_tree>`__.

Geometry
::::::::

A very classical problem in computational geometry is the computation of the convex hull of a given point set in the Euclidean space. Generally text books present Graham's algorithm.  But for this library we made the choice of Andrew's sweepline algorithm, which has the advantage of avoiding trigonometric operations, see `convex_hull <tryalgo/tryalgo.html#module-tryalgo.convex_hull>`__.  (With some work Graham's algorithm can also be implemented without trigonometric operations, but it is a bit more tricky than Andrew's algorithm.)

Another not less classical problem is the problem of determining a closest pair among a given point set.  It can be solved in time O(n log n) with a sweep line algorithm or using a divide and conquer approach.  In this library we present a randomized very simple algorithm with an expected linear running time, see `closest_points <tryalgo/tryalgo.html#module-tryalgo.closest_points>`__.

The area of a given simple polygon can be computed in linear time, see `polygon <tryalgo/tryalgo.html#module-tryalgo.polygon>`__.  And testing whether a given rectilinear polygon is simple can be verified with a sweepline algorithm in time O(n log n), see `is_simple <tryalgo/tryalgo.html#module-tryalgo.polygon>`__.

Here is an algorithmic puzzle that we like a lot. Given a set of n points in the plane, we which to find out how many 4-tuples we can form such that they are the 4 corners of a rectangle.  The solution can be found in `rectangles_from_points <tryalgo/tryalgo.html#module-tryalgo.rectangles_from_points>`__.

Speaking of rectangles, a nice problem illustrating the amortized analysis consists in finding a largest rectangle under a given histogram.  A linear time algorithm is implemented in `rectangles_from_histogram <tryalgo/tryalgo.html#module-tryalgo.rectangles_from_histogram>`__.  This algorithm is the key to solve another interesting problem. Given a binary matrix, we want to find the largest rectangular sub-matrix consisting only of ones.  The linear time solution can be found in `rectangles_from_grid <tryalgo/tryalgo.html#module-tryalgo.rectangles_from_grid>`__.

Computing the area of the union of n given rectilinear rectangles can be done in time O(n log n) using a sweep line algorithm and a dynamic data structure called segment tree, see `union_rectangles <tryalgo/tryalgo.html#module-tryalgo.union_rectangles>`__.


Arithmetic
::::::::::

Prime numbers are best generated with Eratosthene's method, see `eratosthene <tryalgo/tryalgo.html#module-tryalgo.eratosthene>`__.

The library contains functions to compute the greatest common divisor (GCD in english or PGCD in french), to compute the Bezot coefficients and the binomial coefficients, see `arithm <tryalgo/tryalgo.html#module-tryalgo.arithm>`__.

Fast exponentiation is a very powerful technique, which applies also to exponentiation of matrices, see `fast_exponentiation <tryalgo/tryalgo.html#module-tryalgo.fast_exponentiation>`__.

An arithmetic expression given in form of a string can be evaluated in different manners. The library contains a simple method using a stack for the operations and for the intermediate values, see `arithm_expr_eval <tryalgo/tryalgo.html#module-tryalgo.arithm_expr_eval>`__.

For solving a system of linear equations, a classical method is to use the Gauss-Jordan triangulation technique, see `gauss_jordan <tryalgo/tryalgo.html#module-tryalgo.gauss_jordan>`__.

When multiplying a sequence of matrices the order of evaluation does not matter, but placing the parenthesis in a good manner, permits to minimize the number of arithmetic operations necessary for the computation.  This is a classical problem which can be solved by dynamic programming, see `matrix_chain_mult <tryalgo/tryalgo.html#module-tryalgo.matrix_chain_mult>`__.

The module `roman_numbers <tryalgo/tryalgo.html#module-tryalgo.roman_numbers>`__ provides functions to convert an integer into its roman number representation string and vice-versa.

Backtracking
::::::::::::

Sometimes all our known techniques fail on some problems, and then we need to attack it with brute force and backtracking.  This technique is illustrated in `laser_mirrors <tryalgo/tryalgo.html#module-tryalgo.laser_mirrors>`__ on a problem consisting of a grid containing in some cells two sided mirrors which can be oriented at angles 45 or 225 degrees.  The goal is to find an orientation which permits to orient the trajectory of a laser beam entering at a specific position on the left border of the grid, so it reaches a specific position on the right side of the grid.

The Rolls-Royce of backtracking algorithms is the dancing link algorithm, which solves quite efficiently the NP-hard problem /exact set cover/.  It is implemented in `dancing_links <tryalgo/tryalgo.html#module-tryalgo.dancing_links>`__ and is illustrated on the classical Sudoku problem in `sudoku <tryalgo/tryalgo.html#module-tryalgo.sudoku>`__.

Finally a useful procedure is :py:func:`next_permutation` which takes as input a table of size n containing a permutation of the integers 1 to n and puts them in the lexicographically next permutation order, see `next_permutation <tryalgo/tryalgo.html#module-tryalgo.next_permutation>`__.


Last words
~~~~~~~~~~

We hope that you find the library instructive and useful.  If you miss some functionality, let us know, and you might want to have a look at `PADS <http://www.ics.uci.edu/~eppstein/PADS/>`__. and `NetworkX <https://pypi.python.org/pypi/networkx/>`__.
