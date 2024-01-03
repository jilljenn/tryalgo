
# Changelog

## 1.6

- Added the data structure PC_tree
- Improved the implementations of maximum cardinality bipartite matching

## 1.5

- Corrected a bug in GraphNamedVertices. Now only the minimum weight edge is kept among multiple edges with same endpoints.
- Added algorithm a_star to compute shortest paths
- Added hamiltonian_cycle to compute a Hamiltonian cycle
- Started to add types to some function parameters

## 1.4

- Move to GitHub Actions and drop Python 2.7 support completely
- Added a Graph class in the module graph, which allows accessing vertices by names instead of indices
- Added alternative versions of union_rectangles
- Added an alternative version of bellman_ford which marks with distance -infinity the vertices reachable from the source by paths of arbitrary small weight
- Added an alternative version of subsetsum
- Added FenwickMin, a minimum variant of Fenwick Trees 
- Added module fft for the Fast Fourier Transformation
- Added module karatsuba for multiplying polynomials
- Added module pareto for computing the Pareto set in 2 or 3 dimensions
- An alternative version of floyd_warshall added by Pascal Ortiz
- Changed the web host of the documentation
- Corrected the function building the Huffman tree
- Fenwick Trees indices now start at zero
- Removed erroneous PQ_trees
- Renamed module eratosthene into primes. Added the Gries-Misra sieve in this module
- Simplified interval_cover
- Simplified knuth_morris_pratt.maximum_border_length

## 1.3

- Added LazySegmentTree
- Added shortest_cycle
- Functions and classes are now provided also directly by tryalgo without the need to specify the module

## 1.2

- Added horn\_sat
- Added partition_refinement
- Added left\_right\_inversions
