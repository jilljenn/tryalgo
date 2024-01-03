"""  Rami Benelmir, Christoph Dürr, Erisa Kohansal - 2023

The PC-tree is a dynamic datastructure which encodes permutations on the integers modulo n 
satisfying constraints of the form: 
- for a given set S the permutations need to keep the elements of S in consecutive order. 
Here we consider a circular order, i.e. after n-1 comes 0, then 1 and so on.

TODO:
- annotations de type

"""

from tryalgo.Sequence import *  
from abc import ABC
from typing import Set, List, Dict, Optional, Union

class Node(ABC):
    """ This class is to group attributes and methods common to the subclasses. 
    But it is not intended to be instantiated. 
    Hence the heritage from ABC (Abstract Base Class).
    """

    def __init__(self, ID=None):
        self.parent = None
        self.full_counter = 0
        self.ID = ID
        self.is_terminal = False
        self.neighbors = None

    def is_full(self) -> bool:
        """
        Check if the element is full. Return True or False.
        """
        return self.full_counter >= len(self.neighbors) - 1

    def is_partial(self):
        """
        Check if the element is full. Return True or False.
        """
        return self.full_counter and not self.is_full()

    def signal_full(self):
        """
        Receive the signal and update the counter of full elements. 
        """
        self.full_counter += 1

    def clean(self):
        """
        Reset the attributes to their default values.
        """
        self.full_counter = 0

    def attach(self, new):
        """
        Adds the new element to the neighbors.
        """
        self.neighbors.add(new)

    def detach(self, old):
        """
        Removes a neighbor.
        """
        if self.parent is old:
            self.parent = None
        self.neighbors.remove(old)


    def detach_bilateral(self, to_detach):
        """
        Deletes the link between this node and all given neighbors
        """
        for x in to_detach:
            x.detach(self)
            self.detach(x)

    def attach_neighbors(self) -> None:
        """
        Used only during the initialization of 
        C_node and P_node. Manages the links 
        between neighbors and parent
        """
        for x in self.neighbors:
            x.attach(self)
            if x.parent is None:
                x.parent = self

            elif x.parent is not self:  # éviter le cas d'une feuille
                assert self.parent is None
                self.parent = x

    def represent_parent(self, show_parent: bool) -> List[Optional[int]]:
        """ Returns a list (empty or singleton) representing the parent of the node.
        """
        if show_parent:
            if self.parent is not None:
                return [self.parent.ID]
            else:
                return [None]
        else:
            return []


class Leaf(Node):
    def __init__(self, ID):
        super().__init__(ID)
        self.full = False

    def is_full(self):
        """
        Check if the element is full. Return True or False.
        """
        return self.full

    def clean(self):
        """
        Reset the attributes to their default values.
        """
        super().clean()
        self.full = False

    def to_signal(self):
        """
        Leaf signal to the parent that they are full.
        """
        return self.parent

    def detach(self, old):
        """
        Removes the link between an element and the parent.
        """
        assert self.parent is old
        self.parent = None

    def attach(self, new):
        """
        Defines a new parent for the element.
        """
        assert self.parent is None
        self.parent = new

    def frontier(self, trace: List[int], enter: Node):
        """Exploring the the tree and writing the leafs in the order they are discovered.
        enter is the neighbor of the current node from which the tree exploration was initiated
        """
        trace.append(self.ID)



class P_node(Node):
    def __init__(self, neighbors: Set[Node] = set()):
        super().__init__()
        self.neighbors = neighbors
        self.full_neighbors: Set[Node] = set()
        self.attach_neighbors()

    def clean(self):
        """
        Reset the attributes to their default values.
        """
        super().clean()
        self.full_neighbors = set()

    def _splittable(self, left_terminal, right_terminal) -> None:
        """
        Verifies if we can split the node.
        Raises an exception if not.
        """
        pass            # P-nodes are always splittable

    def split(self):
        """
        Create a new full node that contains all the full neighbors 
        of this element, and it becomes an empty node.
        """
        self.detach_bilateral(self.full_neighbors)
        return P_node(neighbors=self.full_neighbors)

    def signal_full(self, full_neighbor):
        """
        Receive the signal and update the counter of full elements 
        and adds the fullNeighbor to its full set.
        """
        super().signal_full()
        self.full_neighbors.add(full_neighbor)

    def to_signal(self):
        """
        Determines and returns the only non full element for a full node.
        """
        difference = self.neighbors - self.full_neighbors
        assert len(difference) == 1
        return difference.pop()

    def represent(self, show_parent=False):
        """
        Prints the C node in the terminal.
        """
        par = self.represent_parent(show_parent)
        return ['P', self.ID, list(sorted([x.ID for x in self.neighbors]))] + par
    
    def frontier(self, trace: List[int], enter: Node):
        """Exploring the the tree and writing the leafs in the order they are discovered.
        enter is the neighbor of the current node from which the tree exploration was initiated
        """
        for x in self.neighbors:
            if x != enter:
                x.frontier(trace, enter=self)

    def _simplify(self):
        """Called after split and before attaching to new central C-node.
        contracts degree 2 P-nodes.
        """
        if len(self.neighbors) == 1:
            x = next(iter(self.neighbors)) # we have neighbors = {x}
            self.detach_bilateral([x])
            return [x]
        else:
            return [self]
        


class C_node(Node):
    def __init__(self, neighbors: List[Node] = []):
        super().__init__()
        self.neighbors = Sequence(neighbors)
        self.first_full = None  
        self.attach_neighbors()

    def clean(self):
        """
        Reset the attributes to their default values.
        """
        super().clean()
        self.first_full = None

    def flip(self):
        """ Invertes the order of the neighbors.
        """
        seq = Sequence()
        last = None
        for x in self.neighbors:
            if last is None:
                seq.add(x)
            else:
                seq.insertBefore(last, x)
            last = x 
        self.neighbors = seq

    def _splittable(self, left_terminal :Optional[Node], right_terminal :Optional[Node]) -> None:
        """ 
        Tests if the C code is is_splittable, i.e. if all full neighbors form an interval, 
        and the neighbors of this interval are exactly the given terminal_neighbors.

        Raises an exception if node is not splittable.

        Modifies first_full to be the left most full neighbor in that interval.
        Might flip the C node.
        """
        assert len(self.neighbors) > self.full_counter
        if self.first_full is None:
            # empty node, the terminal neighbors must be consecutive in the neighbor order.
            if left_terminal is not None and right_terminal is not None:
                if self.neighbors.successor(right_terminal) is left_terminal:
                    self.flip()
                elif not self.neighbors.successor(left_terminal) is right_terminal:
                    raise Infeasible("C node with non adjacent partial neighbors and no full neighbor")
            return
        
        # now this is a partial C-node
        # between left and right the interval has size interval_size.
        interval_size = 1
        right = self.first_full
        left = self.first_full

        # extend interval while possible to the right
        x = self.neighbors.successor(right)
        while x.is_full():
            right = x
            x = self.neighbors.successor(right)
            interval_size += 1

        # ... and to the left
        x = self.neighbors.predecessor(left)
        while x.is_full():
            left = x
            x = self.neighbors.predecessor(left)
            interval_size += 1

        # check if the interval captures all full neighbors
        if self.full_counter != interval_size:
            raise Infeasible("C node with non adjacent full neighbors")

        left_neighbor = self.neighbors.predecessor(left)
        right_neighbor = self.neighbors.successor(right)
        assert left_neighbor != right_neighbor          # because otherwise node is full

        # verify that the full interval is between the terminal neighbors
        if (left_terminal is None or left_terminal == right_neighbor) and \
            (right_terminal is None or right_terminal == left_neighbor) and \
            (left_terminal is not None or right_terminal is not None):
            self.flip()
            self.first_full = right
        elif ((left_terminal is None or left_terminal == left_neighbor) and \
              (right_terminal is None or right_terminal == right_neighbor)):
            self.first_full = left
        else:
            raise Infeasible("C node with terminal neighbors not adjacent to full neighbors")

    def split(self):
        """
        Splits a C node.
        Returns a new C-node with all full neighbors.
        """
        assert self.is_partial()        # will be called only for partial nodes

        L = [] # will contain the nodes of the full interval
        # we have the promize that first_full is 
        # the left most full node in the full interval
        x = self.first_full
        while x.is_full():
            L.append(x)
            x = self.neighbors.successor(x)

        # need to set a starting item in the empty neighbor list

        self.detach_bilateral(L)

        # first empty neighbor
        self.neighbors._first = id(x)

        split_off = C_node(L)
        split_off.neighbors._first = id(self.first_full)
        return split_off

    def signal_full(self, fullNeighbor):
        """
        Receive the signal and update the counter of full elements and
        adds the received element to the full nodes.
        """
        super().signal_full()
        if self.first_full is None:
            self.first_full = fullNeighbor

    def to_signal(self):
        """
        Determines which neighbor is the only non full neighbor.
        """
        assert self.full_counter == len(self.neighbors) - 1
        current = self.first_full
        while current.is_full():
            current = self.neighbors.successor(current)
        return current

    def represent(self, show_parent=False):
        """
        Returns a list representation of the node.
        Used for showing the C node correctly in the terminal
        and for unittests.
        """
        L = [x.ID for x in self.neighbors]
        # find the lexicographically smallest permutation of neighbors
        # start with minimum
        minimum = L.index(min(L))
        res = []
        # process in the direction which minimizes the second element in list
        if L[minimum - 1] < L[(minimum + 1) % len(L)]:
            res = L[minimum::-1] + L[-1:minimum:-1]
        else:
            res = L[minimum:] + L[:minimum]
        return ['C', self.ID, res] + self.represent_parent(show_parent)
    
    def frontier(self, trace: List[int], enter: Node):
        """Exploring the the tree and writing the leafs in the order they are discovered.
        enter is the neighbor of the current node from which the tree exploration was initiated
        """
        x = self.neighbors.successor(enter)
        while x is not enter:
            x.frontier(trace, enter=self)
            x = self.neighbors.successor(x)

    def _simplify(self):
        """Called after split and before attaching to new central C-node.
        replaces this C-node by its neighbors
        """
        retval = list(self.neighbors)
        self.detach_bilateral(retval)       # detach from current C-node (which will be deleted)
        return retval
    
    def detach(self, old):
        """
        Removes a neighbor.
        """
        self.neighbors._first = id(self.neighbors.successor(old))
        super().detach(old)



class Infeasible(Exception):
    """ Exception raised if the restriction is impossible for some reason.
    """
    def __init__(self, reason):
        super().__init__("Impossible restriction because : " + reason)


Inner_node = Union[P_node, C_node]

class PC_tree:
    def __init__(self, nb_leaves: int):
        assert nb_leaves >= 3
        self.leaves = [Leaf(i) for i in range(nb_leaves)]
        P_node(set(self.leaves))    # initially the tree is a star

    def restrict(self, restriction):
        """
        Refines the PC tree with the restrictions passed in the arguments.
        """
        try:
            # step 0: check for trivial cardinalty
            size = len(restriction)
            nb_leaves = len(self.leaves)
            if size in [0, 1, nb_leaves-1, nb_leaves]:
                return True     # nothing to do

            # step 1: label nodes
            partial_nodes, fullNodes = self._label(restriction)

            # step 2: identify terminal path
            path = self._terminal_path(partial_nodes)

            # steps 3,4,...: 
            forest = self._split(path)
            forest = self._simplify(forest)
            self._remodel(forest)

            valide_res = True

        except Infeasible as e:
            valide_res = False

        # clean up even if exception was raised
        for d in [partial_nodes, fullNodes]:
            for x in d:
                d[x].clean()

        return valide_res

    def _label(self, restriction):
        """
        Marks the full and partial nodes and return a dictionnary 
        of each of them.
        """
        fullNodes = {}
        partial_nodes = {}

        # on marque les noeuds pleins
        becameFull = []
        for i in restriction:
            x_leaf = self.leaves[i]
            x_leaf.full = True
            becameFull.append(x_leaf)
            fullNodes[id(x_leaf)] = x_leaf

        # propagation de l'information par rapport aux noeuds full et partiels
        while becameFull:
            current = becameFull.pop()
            to_signal = current.to_signal()
            if id(to_signal) not in partial_nodes:
                partial_nodes[id(to_signal)] = to_signal
            to_signal.signal_full(current)
            if to_signal.is_full():
                becameFull.append(to_signal)
                del partial_nodes[id(to_signal)]
                fullNodes[id(to_signal)] = to_signal

        return partial_nodes, fullNodes

    def _terminal_path(self, partial_nodes: Dict[int, Node]):
        """
        :param partial_nodes: is a dictionary from node identifiers to nodes
        Tries to identify the terminal path.
        In the positive case it returns a list of its nodes,
        otherwise it raises an exception.
        """
        # Case: single partial node
        if len(partial_nodes) == 1:
            return list(partial_nodes.values())
        
        apex = None         # the apex node
        leader = None       # the leader node
        
        # by definition, all partial nodes are terminal
        for x in partial_nodes:
            partial_nodes[x].is_terminal = True 

        # maps the identifier of an active seed 
        # to the current node of the walk from the seed
        active = {x: partial_nodes[x] for x in partial_nodes} 
        # for every marked node we store which node marked it
        marked = {x: x for x in partial_nodes} 

        # extend walks from active nodes
        while len(active) >= 2 or ( len(active) == 1 and leader != None ):
            # we cannot disable seeds while looping, so disabling is delayed
            disable = []    
            # the path is expended in Robin-Round manner
            for act in active: 
                p = active[act] # extend by arc (p, q) the walk which started by seed act
                q = p.parent
                if q is None:               # we walked into root
                    disable.append(act)
                    leader = partial_nodes[act]
                elif id(q) in marked:       # walked into already visited node
                    disable.append(act)
                    if q.is_partial() and q.is_terminal:
                        q.is_terminal = False
                    if not q.is_terminal:
                        if apex is None:
                            apex = q        # we found the apex
                        else:
                            raise Infeasible("terminal (partial) edges form a degree 3 node")
                else:
                    marked[id(q)] = act     # mark as visited
                active[act] = q             # make one step
                
            for act in disable:             # disable nodes
                del active[act]

        if leader is None:
            leader = partial_nodes[list(active.keys())[0]]

        # I don't manage to find tests sets that would cover
        # the following lines (1) and (2). 
        # Maybe I missed something in the algorithm,
        # and these cases never happen.
        if apex is not None : 
            # A shaped path
            if marked[id(apex)] != id(leader):
                raise Infeasible("terminal edges form a degree 3 node") # (1)
        else:
            # I shaped path
            apex = leader                                               # (2)

        tail = [partial_nodes[x] for x in partial_nodes if partial_nodes[x].is_terminal]
        assert 1 <= len(tail) <= 2
        # construct the list of the nodes in the terminal path
        part1 = []      # from 1st tail to apex (included)
        a = tail[0]
        while True:
            part1.append(a)
            if a is apex:
                break
            a = a.parent
        part2 = []      # from 2nd tail to apex (excluded)
        if len(tail) == 2:
            a = tail[1]
            while a is not apex:
                part2.append(a)
                a = a.parent
        return part1 + part2[::-1]
                            
    def _splittable(self, path :List[Inner_node]) -> None:
        """  
        Checks to see if the nodes on the terminal path
        can be splitted. Raises an exception if not.
        """
        # singleton path ?
        if len(path) == 1:  
            path[0]._splittable(None, None)
        else:
        # first and last node
            path[0]._splittable(None, path[1])
            path[-1]._splittable(path[-2], None)
        # remaining inner nodes
        for i in range(1, len(path)-1):
            path[i]._splittable(path[i - 1], path[i + 1])

    def _split(self, path):
        """
        Splits the nodes on the terminal path into
        full nodes and empty ones. 
        returns list of those nodes.
        """
        # check first if path is splittable
        self._splittable(path)

        # no exception? good!

        # actual splitting
        term_full = []
        term_empty = []
        # detach all nodes in path from each other
        for i, x in enumerate(path[:-1]):
            # detach from next node in path
            x.detach_bilateral([path[i + 1]])
        # split nodes individually
        for x in path:
            term_empty.append(x)
            if x.full_counter:
                term_full.append(x.split())

        # reconnect both lists
        return term_empty[::-1]  + term_full    # recompose in circular order

    def _simplify(self, path):
        """
        Deletes nodes which would have degree 2 if attached to central C-node.
        Returns modified path.
        """
        result = []
        for x in path:
            result.extend(x._simplify())  
        return result

    def _remodel(self, path):
        """
        Used for creating the C node or in the case of a 
        single node on the terminal path, defining correct 
        parent link.
        """
        if len(path) == 2:
            path[0].attach(path[1])
            path[1].attach(path[0])

            assert not (path[0].parent and path[1].parent)

            if path[0].parent:
                path[1].parent = path[0]
            else:
                path[0].parent = path[1]

        else:
            # create a central C-node
            C_node(path)

    def represent(self, show_parent=False):
        """
        Printing the PC tree in the terminal.
        """
        # first we assign identifiers to parents of leafs
        L = []  # list of nodes with assigned id, in order of id
        ID = len(self.leaves)   # start numbering after largest leaf number
        for i, x_i in enumerate(self.leaves):
            p_i = x_i.parent
            if p_i.ID is None:  # if it does not already have an id
                p_i.ID = ID
                L.append(p_i)
                ID += 1

        # now we process L, and assign ids to unassigned neighbors
        k = 0   # position in L
        # the part in L between k and the end plays the role of a queue
        while k < len(L):  
            for neighbor in L[k].neighbors:
                if neighbor.ID is None:
                    neighbor.ID = ID
                    L.append(neighbor)  # to be processed later
                    ID += 1
            k += 1
        result = [x.represent(show_parent) for x in L]
        # clean up as my mother teached me to do
        for x in L:
            x.ID = None
        return result
    
    def frontier(self) -> List[int]:
        """ 
        Returns a permutation on {0, 1, ..., n-1} satisfying all given restrictions.
        """
        trace = [0]
        x = self.leaves[0] 
        x.parent.frontier(trace, x)
        return trace

        
    def print_dot(self):
        """ Prints the PC-tree in dot format.
            Redirect the output in a file t.dot, 
            which can be rendered for example with 
            dot t.dot -T pdf -o t.pdf
        """
        rep = self.represent(True)        
        arcs = []
        print("digraph G{")
        print("layout=neato")
        n = rep[0][1]
        for node in rep:
            if node[0] == "P":
                shape = "circle"
            else:
                shape = "doublecircle"
            print(node[1], f"[shape={shape}, label={node[1]}]")
            for v in node[2]:
                if v < n:
                    arcs.append((v, node[1]))
            if node[3] is not None:
                arcs.append(([node[1], node[3]]))
        for v in range(n):
            print(v, "[shape=none]")
        for u,v in arcs:
            print(u, "->", v)
        order = self.frontier()
        print(order[-1], end=' ')
        # single cycle over all leafs in order should force correct drawing
        for v in order:
            print("->", v, end=' ')
        print("[color=white]")
        print("}")

