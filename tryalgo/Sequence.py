"""Sequence.py

Doubly-linked circular list for maintaining a sequence of items
subject to insertions and deletions.

Copyright D. Eppstein, November 2003. Under the MIT licence.

Modified by
Rami Benelmir, Christoph Dürr, Erisa Kohansal - 2023

we adapted the data structure to store only objects and to permit to replace objects easily.
we changed the name of the function "append" to "add" for simplifying our code.
"""

import math
import sys

class SequenceError(Exception): pass

class Sequence:
    """Maintain a sequence of items subject to insertions and removals.
    All sequence operations take constant time except indexing, which
    takes time proportional to the index.
    """

    def __init__(self, iterable=[], key=id):
        """We represent the sequence as a doubly-linked circular linked list,
        stored in two dictionaries, self._next and self._prev.  We also store
        a pointer self._first to the first item in the sequence.  If key is
        supplied, key(x) is used in place of x to look up item positions;
        e.g. using key=id allows sequences of lists or sets.
        """
        self._key = key
        self._items = {}
        self._next = {}
        self._prev = {}
        self._first = None
        for x in iterable:
            self.add(x)

    def __iter__(self):
        """Iterate through the objects in the sequence.
        May give unpredictable results if sequence changes mid-iteration.
        """
        item = self._first
        while self._next:
            yield self._items.get(item,item)
            item = self._next[item]
            if item == self._first:
                return

    def __getitem__(self,i):
        """Return the ith item in the sequence."""
        item = self._first
        while i:
            item = self._next[item]
            if item == self._first:
                raise IndexError("Index out of range")
            i -= 1
        return self._items.get(item,item)

    def __len__(self):
        """Number of items in the sequence."""
        return len(self._next)

    def __repr__(self):
        """Printable representation of the sequence."""
        output = []
        for x in self:
            output.append(repr(x))
        return 'Sequence([' + ','.join(output) + '])'

    def key(self,x):
        """Apply supplied key function."""
        if not self._key:
            return x
        key = self._key(x)
        self._items[key] = x
        return key

    def _insafter(self,x,y):
        """Unkeyed version of insertAfter."""
        if y in self._next:
            raise SequenceError("Item already in sequence: "+repr(y))
        self._next[y] = z = self._next[x]
        self._next[x] = self._prev[z] = y
        self._prev[y] = x

    def add(self,x):
        """Add x to the end of the sequence."""
        x = self.key(x)
        if not self._next:  # add to empty sequence
            self._next = {x:x}
            self._prev = {x:x}
            self._first = x
        else:
            self._insafter(self._prev[self._first],x)


    def remove(self,x):
        """Remove x from the sequence."""
        x = self.key(x)
        prev = self._prev[x]
        self._next[prev] = next = self._next[x]
        self._prev[next] = prev
        if x == self._first:
            self._first = next
        del self._next[x], self._prev[x]

    def insertAfter(self, x, y):
        """Add y after x in the sequence."""
        y = self.key(y)
        x = self.key(x)
        self._insafter(x,y)

    def insertBefore(self, x, y):
        """Add y before x in the sequence."""
        y = self.key(y)
        x = self.key(x)
        self._insafter(self._prev[x],y)
        if self._first == x:
            self._first = y

    def predecessor(self,x):
        """Find the previous element in the sequence."""
        x = self.key(x)
        prev = self._prev[x]
        return self._items.get(prev,prev)

    def successor(self,x):
        """Find the next element in the sequence."""
        x = self.key(x)
        next = self._next[x]
        return self._items.get(next,next)

    def replace(self, old, new):
        """ Replace an object by another one, preserving the position in the sequence
        """
        self.insertAfter(old, new)
        self.remove(old)

