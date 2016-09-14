#!/usr/bin/env python3
# Partition refinement
# christoph durr - 2016


__all__ = ["PartitionRefinement"]


class DoubleLinkedListItem:
    """Item of a circular double linked list
    """

    def __init__(self, anchor=None):
        """Create a new item to be inserted before item anchor.
           if anchor is None: create a single item circular double linked list
        """
        if anchor:
            self.insert(anchor)
        else:
            self.prec = self
            self.succ = self

    def remove(self):
        self.prec.succ = self.succ
        self.succ.prec = self.prec

    def insert(self, anchor):
        # insert before anchor
        self.prec = anchor.prec        # point to the neighbors
        self.succ = anchor
        self.succ.prec = self          # make neighbors point to item
        self.prec.succ = self

    def __iter__(self):
        """iterate trough circular list.
        warning: might end stuck in an infinite loop if chaining is not valid
        """
        curr = self
        yield self
        while curr.succ != self:
            curr = curr.succ
            yield curr


class PartitionClass(DoubleLinkedListItem):
    """There is a single double linked list of all classes
    """

    def __init__(self, anchor, start, size=0):
        DoubleLinkedListItem.__init__(self, anchor)
        self.start = start        # first item in class
        self.size = size          # number of items in class
        self.split = None         # reference to split class


class PartitionItem(DoubleLinkedListItem):
    """There is a single double linked list of all items.
    Every class is consecutive in that list.
    """

    def __init__(self, val, anchor, theclass):
        DoubleLinkedListItem.__init__(self, anchor)
        self.val = val
        self.theclass = theclass


class PartitionRefinement:
    """This data structure implements an order preserving partition with refinements.
    """

    def __init__(self, n):
        """Start with the partition consisting of the unique class {0,1,..,n-1}
        complexity: O(n) both in time and space
        """
        self.n = n
        c = PartitionClass(None, None, n)   # initially there is a single class of size n
        self.classes = c
        self.items = [PartitionItem(0, None, c)]   # first item needs special treatment
        c.start = self.items[0]
        for x in range(1, n):               # insert before first item equals appending after last item
            self.items.append(PartitionItem(x, c.start, c))

    def refine(self, pivot):
        """Split every class C in the partition into C intersection pivot and C setminus pivot
        complexity: linear in size of pivot
        """
        has_split = []                      # remember which classes split
        for i in pivot:
            if 0 <= i < self.n:             # ignore if outside of domain
                x = self.items[i]
                c = x.theclass              # c = class of x
                c.size -= 1                 # remove item from c
                if c.start is x:
                    c.start = x.succ
                x.remove()
                if not c.split:             # possibly create new split class
                    c.split = PartitionClass(c, x, 0)
                    if self.classes is c:
                        self.classes = c.split   # always make self.classes point to the first class
                    has_split.append(c)
                x.insert(c.start)           # append item to split class, which ends right before class c
                x.theclass = c.split
                c.split.size += 1
        for c in has_split:                 # clean information about split classes
            c.split = None
            if c.size == 0:                 # delete class if it became empty
                c.remove()


    def tolist(self):
        """produce a list representation of the partition
        """
        retval = []
        for c in self.classes:
            retval.append([])
            curr = c.start
            for _ in range(c.size):
                retval[-1].append(curr.val)
                curr = curr.succ
        return retval

    def order(self):
        """Produce a flatten list of the partition, ordered by classes
        """
        return [x.val for x in self.classes.start]

