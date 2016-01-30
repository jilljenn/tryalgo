.. tryalgo documentation master file, created by
   sphinx-quickstart on Sat Nov  7 13:03:23 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.



Welcome to tryalgo's documentation!
===================================

.. toctree::
   :maxdepth: 2

This Python library implements different classical and original algorithm and data-structures covering graph problems, string problems and computational geometry problems for example.

* :ref:`genindex`
* :ref:`modindex`


Installation
------------

There are two possibilities to install the library. Either download the `tar.gz <https://pypi.python.org/pypi/tryalgo/>`_ file and decompress it on your hard drive.  The library consists of a directory named tryalgo containing several Python files (the modules).  Or install it with the pip command::

    $ pip3 install tryalgo


First steps with the library
----------------------------

The functions of the library can be used like in this example.::


    #!/usr/bin/env python3

    from tryalgo.subsetsum import coin_change

    print(coin_change([3, 5, 11], 29))

Which should print :code:`True` because 29 can be expressed as the linear combination 6*3 + 0*5 + 1*11.

In order to find the longest substring that is a palindrome, you can use the implementation of Manacher's algorithm as follows.::

    from tryalgo.manacher import manacher
    print(manacher("babcbabcbaccba"))

which will print (1,10). Indeed the substring ranging from index 1 to index 10 (excluding position 10) is the palindrome "abcbabcba".

Now suppose you want to compute shortest paths in the following graph from the source vertex 0.

.. image:: _static/example_dijkstra.png
   :width: 400 px


First we need to encode the graph. For example we could use an adjacency list data structure :code:`graph`, where :code:`graph[u]` is the list of neighboring vertices of vertex u.  The edge weights are encoded simply in a squared matrix.::

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


The shortest path can be computed with Dijkstra's algorithm.  Our implementation returns the table of distances from the source and a predecessor table describing the shortest path tree.::

    from tryalgo.dijkstra import dijkstra

    dist, prec = dijkstra(graph, weights, source=0)

    print(dist[10])
    print("%i %i %i %i %i %i" % (10, prec[10], prec[prec[10]], prec[prec[prec[10]]],
          prec[prec[prec[prec[10]]]], prec[prec[prec[prec[prec[10]]]]]))

which will print for target vertex 10 the distance 9 and the shortest path 10 7 4 2 1  0 (in reverse order).

If your graph is sparse (contains few arcs), then you might want to represent it using an adjacency dictionary.  Formally the sparse graph representation is a list of dictionaries :code:`sparse` such that :code:`v` belongs to :code:`sparse[u]` if there is an arc (u,v) and the weight is the  value :code:`sparse[u][v]` of the dictionary.  For example the above graph would be represented as.::

    [{1: 1, 3: 4},
     {0: 1, 2: 1, 3: 3},
     {1: 1, 4: 3, 5: 8},
     {0: 4, 1: 3, 5: 2, 6: 2},
     {2: 3, 7: 1},
     {2: 8, 3: 2, 7: 2, 8: 7},
     {3: 2, 8: 3, 9: 2},
     {4: 1, 5: 2, 10: 3},
     {5: 7, 6: 3, 10: 2},
     {6: 2, 11: 1},
     {7: 3, 8: 2},
     {9: 1}]

This data structure encodes both the graph and the arc weights, and hence it is possible to invoke the function as.::

    dist, prec = dijkstra(sparse, sparse, source=0)

Many of our implementations of graph algorithms accept both data structures, the adjacency list or the adjacency dictionary, and this is specified in the individual function documentations.

.. include:: content.rst
