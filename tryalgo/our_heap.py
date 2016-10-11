#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# A min heap
# christoph durr et jill-jenn vie - 2015


# snip{
class OurHeap:
    """ min heap

    * heap: is the actual heap, heap[1] = index of the smallest element
    * rank: inverse of heap with rank[x]=i iff heap[i]=x
    * n: size of the heap

    :complexity: init O(n log n), len O(1),
                other operations O(log n) in expectation
                and O(n) in worst case, due to the usage of a dictionary
    """
    def __init__(self, items):
        self.n = 0
        self.heap = [None]  # index 0 will be ignored
        self.rank = {}
        for x in items:
            self.push(x)

    def __len__(self):
        return len(self.heap) - 1

    def push(self, x):
        """Insert new element x in the heap.
           Assumption: x is not already in the heap"""
        assert x not in self.rank
        i = len(self.heap)
        self.heap.append(x)    # ajout d'une nouvelle feuille
        self.rank[x] = i
        self.up(i)             # maintenir l'ordre de tas

    def pop(self):
        """Remove and return smallest element"""
        root = self.heap[1]
        del self.rank[root]
        x = self.heap.pop()    # enlever la dernière feuille
        if self:               # le tas n'est pas vide
            self.heap[1] = x   # et la mettre à la racine
            self.rank[x] = 1
            self.down(1)       # maintenir l'ordre de tas
        return root
    # snip}

    # snip{ our_heap_up_down
    def up(self, i):
        """The value of heap[i] has decreased. Maintain heap invariant."""
        x = self.heap[i]
        while i > 1 and x < self.heap[i // 2]:
            self.heap[i] = self.heap[i // 2]
            self.rank[self.heap[i // 2]] = i
            i //= 2
        self.heap[i] = x       # point d'insertion trouvé
        self.rank[x] = i

    def down(self, i):
        """the value of heap[i] has increased. Maintain heap invariant."""
        x = self.heap[i]
        n = len(self.heap)
        while True:
            left = 2 * i       # descendre dans l'arbre
            right = left + 1
            if right < n and \
               self.heap[right] < x and self.heap[right] < self.heap[left]:
                self.heap[i] = self.heap[right]
                self.rank[self.heap[right]] = i   # remonter fils droite
                i = right
            elif left < n and self.heap[left] < x:
                self.heap[i] = self.heap[left]
                self.rank[self.heap[left]] = i    # remonter fils gauche
                i = left
            else:
                self.heap[i] = x   # point d'insertion trouvé
                self.rank[x] = i
                return

    def update(self, old, new):
        """Replace an element in the heap
        """
        i = self.rank[old]     # changer la valeur à l'indice i
        del self.rank[old]
        self.heap[i] = new
        self.rank[new] = i
        if old < new:          # maintenir l'ordre de tas
            self.down(i)
        else:
            self.up(i)
# snip}
