#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Reading graphs from files and writing into files
# jill-jênn vie et christoph dürr - 2015-2018


def readval(file, ty):
    """Reads a line from file with an item of type ty

    :param file: input stream, for example sys.stdin
    :param ty: a type, for example int
    :returns: an element of type ty
    """
    return ty(file.readline())


def readtab(fi, ty):
    """Reads a line from file with a space separated list
       of items of type ty

    :param file: input stream, for example sys.stdin
    :param ty: a type, for example int
    :returns: a tuple with elements of type ty
    """
    return tuple(map(ty, fi.readline().split()))


def read_graph(filename, directed=False, weighted=False, default_weight=None):
    """Read a graph from a text file

    :param filename: plain text file. All numbers are separated by space.
              Starts with a line containing n (#vertices) and m (#edges).
              Then m lines follow, for each edge.
              Vertices are numbered from 0 to n-1.
              Line for unweighted edge u,v contains two integers u, v.
              Line for weighted edge u,v contains three integers u, v, w[u,v].

    :param directed: true for a directed graph, false for undirected
    :param weighted: true for an edge weighted graph
    :returns: graph in listlist format, possibly followed by weight matrix
    :complexity: O(n + m) for unweighted graph,
                 :math:`O(n^2)` for weighted graph
    """
    with open(filename, 'r') as f:
        while True:
            line = f.readline()         # ignore leading comments
            if line[0] != '#':
                break
        nb_nodes, nb_edges = tuple(map(int, line.split()))
        graph = [[] for u in range(nb_nodes)]
        if weighted:
            weight = [[default_weight] * nb_nodes for v in range(nb_nodes)]
            for v in range(nb_nodes):
                weight[v][v] = 0
            for _ in range(nb_edges):
                u, v, w = readtab(f, int)
                graph[u].append(v)
                weight[u][v] = w
                if not directed:
                    graph[v].append(u)
                    weight[v][u] = w
            return graph, weight
        else:
            for _ in range(nb_edges):
                # si le fichier contient des poids, ils seront ignorés
                u, v = readtab(f, int)[:2]
                graph[u].append(v)
                if not directed:
                    graph[v].append(u)
            return graph


def write_graph(dotfile, graph, directed=False,
                node_label=None, arc_label=None, comment="",
                node_mark=set(), arc_mark=set()):
    """Writes a graph to a file in the DOT format

    :param dotfile: the filename.
    :param graph: directed graph in listlist or listdict format
    :param directed: true if graph is directed, false if undirected
    :param weight: in matrix format or same listdict graph or None
    :param node_label: vertex label table or None
    :param arc_label: arc label matrix or None
    :param comment: comment string for the dot file or None
    :param node_mark: set of nodes to be shown in gray
    :param arc_marc: set of arcs to be shown in red
    :complexity: `O(|V| + |E|)`
    """
    with open(dotfile, 'w') as f:
        if directed:
            f.write("digraph G{\n")
        else:
            f.write("graph G{\n")
        if comment:
            f.write('label="%s";\n' % comment)
        V = range(len(graph))
        #                              -- vertices
        for u in V:
            if node_mark and u in node_mark:
                f.write('%d [style=filled, color="lightgrey", ' % u)
            else:
                f.write('%d [' % u)
            if node_label:
                f.write('label="%u [%s]"];\n' % (u, node_label[u]))
            else:
                f.write('shape=circle, label="%u"];\n' % u)
        #                              -- edges
        if isinstance(arc_mark, list):
            arc_mark = set((u, arc_mark[u]) for u in V)
        for u in V:
            for v in graph[u]:
                if not directed and u > v:
                    continue   # don't show twice the edge
                if arc_label and arc_label[u][v] == None:
                    continue   # suppress arcs with no label
                if directed:
                    arc = "%d -> %d " % (u, v)
                else:
                    arc = "%d -- %d " % (u, v)
                if arc_mark and ( (v,u) in arc_mark or (not directed and (u,v) in arc_mark) ):
                    pen = 'color="red"'
                else:
                    pen = ""
                if arc_label:
                    tag = 'label="%s"' % arc_label[u][v]
                else:
                    tag = ""
                if tag and pen:
                    sep = ", "
                else:
                    sep = ""
                f.write(arc + "[" + tag + sep + pen + "];\n")
        f.write("}")


# snip{ tree_representations
def tree_prec_to_adj(prec, root=0):
    """Transforms a tree given as predecessor table into adjacency list form

    :param prec: predecessor table representing a tree, prec[u] == v iff u is successor of v,
                 except for the root where prec[root] == root
    :param root: root vertex of the tree
    :returns: undirected graph in listlist representation
    :complexity: linear
    """
    n = len(prec)
    graph = [[prec[u]] for u in range(n)]   # add predecessors
    graph[root] = []
    for u in range(n):                      # add successors
        if u != root:
            graph[prec[u]].append(u)
    return graph


def tree_adj_to_prec(graph, root=0):
    """Transforms a tree given as adjacency list into predecessor table form.
    if graph is not a tree: will return a DFS spanning tree

    :param graph: directed graph in listlist or listdict format
    :returns: tree in predecessor table representation
    :complexity: linear
    """
    prec = [None] * len(graph)
    prec[root] = root            # mark to visit root only once
    to_visit = [root]
    while to_visit:              # DFS
        node = to_visit.pop()
        for neighbor in graph[node]:
            if prec[neighbor] is None:
                prec[neighbor] = node
                to_visit.append(neighbor)
    prec[root] = None            # put the standard mark for root
    return prec
# snip}


# snip{ add_reverse_arcs
def add_reverse_arcs(graph, capac = None):
    """Utility function for flow algorithms that need for every arc (u,v),
    the existence of an (v,u) arc, by default with zero capacity.
    graph can be in adjacency list, possibly with capacity matrix capac.
    or graph can be in adjacency dictionary, then capac parameter is ignored.

    :param capac: arc capacity matrix
    :param graph: in listlist representation, or in listdict representation, in this case capac is ignored
    :complexity: linear
    :returns: nothing, but graph is modified
    """
    for u in range(len(graph)):
        for v in graph[u]:
            if u not in graph[v]:
                if type(graph[v]) is list:
                    graph[v].append(u)
                    if capac:
                        capac[v][u] = 0
                else:
                    assert type(graph[v]) is dict
                    graph[v][u] = 0
# snip}

# -----------------------------------------------------------------------------
# transformations between different graph representations

# listlist is an adjacency list G,
#        where G[u] is the list of vertices v such that there is an arc (u,v)
# if the graph is weighted, the weights are represented by a matrix W
#        such that W[u][v] is the weight of arc (u,v)

# listdict is an arc weighted adjacency list G,
#        where G[u] is a dictionary.
#        For each arc (u,v), G[u][v] is the weight of the arc.

# dictdict is an arc weighted adjacency dictionary G,
#        where G[u] is a dictionary.
#        For each arc (u,v), G[u][v] is the weight of the arc.

# matrix is an adjacency matrix M,
#        such that M[u][v] is None if there is no arc (u,v)
#        otherwise it is the weight of the arc.
#        Value M[u][v]=True can be used for unweighted graphs.


def matrix_to_listlist(weight):
    """transforms a squared weight matrix in a adjacency table of type listlist
    encoding the directed graph corresponding to the entries of the matrix
    different from None

    :param weight: squared weight matrix, weight[u][v] != None iff arc (u,v) exists
    :complexity: linear
    :returns: the unweighted directed graph in the listlist representation,
                       listlist[u] contains all v for which arc (u,v) exists.
    """
    graph = [[] for _ in range(len(weight))]
    for u in range(len(graph)):
        for v in range(len(graph)):
            if weight[u][v] != None:
                graph[u].append(v)
    return graph


def listlist_and_matrix_to_listdict(graph, weight=None):
    """Transforms the weighted adjacency list representation of a graph
    of type listlist + optional weight matrix
    into the listdict representation

    :param graph: in listlist representation
    :param weight: optional weight matrix
    :returns: graph in listdict representation
    :complexity: linear
    """
    if weight:
        return [{v:weight[u][v] for v in graph[u]} for u in range(len(graph))]
    else:
        return [{v:None for v in graph[u]} for u in range(len(graph))]


def listdict_to_listlist_and_matrix(sparse):
    """Transforms the adjacency list representation of a graph
    of type listdict into the listlist + weight matrix representation

    :param sparse: graph in listdict representation
    :returns: couple with listlist representation, and weight matrix
    :complexity: linear
    """
    V = range(len(sparse))
    graph = [[] for _ in V]
    weight = [[None for v in V] for u in V]
    for u in V:
        for v in sparse[u]:
            graph[u].append(v)
            weight[u][v] = sparse[u][v]
    return graph, weight


def dictdict_to_listdict(dictgraph):
    """Transforms a dict-dict graph representation into a
    adjacency dictionary representation (list-dict)

    :param dictgraph: dictionary mapping vertices to dictionary
           such that dictgraph[u][v] is weight of arc (u,v)
    :complexity: linear
    :returns: tuple with graph (listdict), name_to_node (dict), node_to_name (list)
    """
    n = len(dictgraph)                            # vertices
    node_to_name = [name for name in dictgraph]   # bijection indices <-> names
    node_to_name.sort()                           # to make it more readable
    name_to_node = {}
    for i in range(n):
        name_to_node[node_to_name[i]] = i
    sparse = [{} for _ in range(n)]               # build sparse graph
    for u in dictgraph:
        for v in dictgraph[u]:
            sparse[name_to_node[u]][name_to_node[v]] = dictgraph[u][v]
    return sparse, name_to_node, node_to_name

# -----------------------------------------------------------------------------
# for shortest paths


def extract_path(prec, v):
    """extracts a path in form of vertex list from source to vertex v
       given a precedence table prec leading to the source

    :param prec: precedence table of a tree
    :param v: vertex on the tree
    :returns: path from root to v, in form of a list
    :complexity: linear
    """
    L = []
    while v is not None:
        L.append(v)
        v = prec[v]
        assert v not in L   # prevent infinite loops for a bad formed table prec
    return L[::-1]


# -----------------------------------------------------------------------------
# for exporting flows in dot format

def make_flow_labels(graph, flow, capac):
    """Generate arc labels for a flow in a graph with capacities.

    :param graph: adjacency list or adjacency dictionary
    :param flow:  flow matrix or adjacency dictionary
    :param capac: capacity matrix or adjacency dictionary
    :returns: listdic graph representation, with the arc label strings
    """
    V = range(len(graph))
    arc_label = [{v:"" for v in graph[u]} for u in V]
    for u in V:
        for v in graph[u]:
            if flow[u][v] >= 0:
                arc_label[u][v] = "%s/%s" % (flow[u][v], capac[u][v])
            else:
                arc_label[u][v] = None   # do not show negative flow arcs
    return arc_label

# -----------------------------------------------------------------------------
# for creating a graph using vertex names


#snip{ class_graph
class Graph:
    def __init__(self):
        self.neighbors = []
        self.name2node = {}
        self.node2name = []
        self.weight = []

    def __len__(self):
        return len(self.node2name)

    def __getitem__(self, v):
        return self.neighbors[v]

    def add_node(self, name):
        assert name not in self.name2node
        self.name2node[name] = len(self.name2node)
        self.node2name.append(name)
        self.neighbors.append([])
        self.weight.append({})
        return self.name2node[name]

    def add_edge(self, name_u, name_v, weight_uv=None):
        self.add_arc(name_u, name_v, weight_uv)
        self.add_arc(name_v, name_u, weight_uv)

    def add_arc(self, name_u, name_v, weight_uv=None):
        u = self.name2node[name_u]
        v = self.name2node[name_v]
        self.neighbors[u].append(v)
        self.weight[u][v] = weight_uv
#snip}
