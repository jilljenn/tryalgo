#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Partition refinement
# christoph durr - 2016-2018

#log: 10/11/2016 modified to preserve class order after refinement
#     15/11/2016 this was non sense, moved back


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
        """insert list item before anchor
        """
        self.prec = anchor.prec        # point to neighbors
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
    """A partition is a list of classes
    """

    def __init__(self, anchor=None):
        DoubleLinkedListItem.__init__(self, anchor)
        self.items = None         # empty list
        self.split = None         # reference to split class

    def append(self, item):
        """add item to the end of the item list
        """
        if not self.items:        # was list empty ?
            self.items = item     # then this is the new head
        item.insert(self.items)


class PartitionItem(DoubleLinkedListItem):
    """A class is a list of items
    """

    def __init__(self, val, theclass):
        DoubleLinkedListItem.__init__(self)
        self.val = val
        self.theclass = theclass
        theclass.append(self)

    def remove(self):
        """remove item from its class
        """
        DoubleLinkedListItem.remove(self)     # remove from double linked list
        if self.succ is self:                 # list was a singleton
            self.theclass.items = None        # class is empty
        elif self.theclass.items is self:     # oups we removed the head
            self.theclass.items = self.succ   # head is now successor


class PartitionRefinement:
    """This data structure implements an order preserving partition with refinements.
    """

    def __init__(self, n):
        """Start with the partition consisting of the unique class {0,1,..,n-1}
        complexity: O(n) both in time and space
        """
        c = PartitionClass()                  # initially there is a single class of size n
        self.classes = c                      # reference to first class in class list
        self.items = [PartitionItem(i, c) for i in range(n)]   # value ordered list of items

    def refine(self, pivot):
        """Split every class C in the partition into C intersection pivot and C setminus pivot
        complexity: linear in size of pivot
        """
        has_split = []                        # remember which classes split
        for i in pivot:
            if 0 <= i < len(self.items):      # ignore if outside of domain
                x = self.items[i]
                c = x.theclass                # c = class of x
                if not c.split:               # possibly create new split class
                    c.split = PartitionClass(c)
                    if self.classes is c:
                        self.classes = c.split   # always make self.classes point to the first class
                    has_split.append(c)
                x.remove()                    # remove from its class
                x.theclass = c.split
                c.split.append(x)             # append to the split class
        for c in has_split:                   # clean information about split classes
            c.split = None
            if not c.items:                   # delete class if it became empty
                c.remove()
                del c

    def tolist(self):
        """produce a list representation of the partition
        """
        return [[x.val for x in theclass.items] for theclass in self.classes]

    def order(self):
        """Produce a flatten list of the partition, ordered by classes
        """
        return [x.val for theclass in self.classes for x in theclass.items]
