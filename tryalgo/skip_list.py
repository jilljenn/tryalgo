# -*- coding: utf-8 -*-
# skip-list
# louis abraham - 2017-2018

# Inspired by https://kunigami.blog/2012/09/25/skip-lists-in-python/
# count contains the gap between the positions (https://www.cs.bgu.ac.il/~ds112/wiki.files/ds112_ps7.pdf)

from __future__ import print_function
from collections import namedtuple
from random import random


# TODO: add order_of_key

class AbstractSkipList():

    def __init__(self):
        raise NotImplemented

    def __getattr__(self, k):
        return getattr(self.head, k)

    def __iter__(self):
        """Iterable in ascending order"""
        if not self.next:
            return
        self = self.next[0]
        while self is not None:
            yield self.key
            self = self.next[0]

    def __len__(self):
        return self._len

    def __bool__(self):
        return bool(len(self))

    def __contains__(self, key):
        return self.find(key) is not None

    def _updateList(self, key):
        heigh = len(self.next)
        update = [None] * heigh
        count = [0] * heigh
        c = -1
        x = self
        for i in reversed(range(heigh)):
            while x.next[i] is not None and x.next[i].key < key:
                c += x.count[i]
                x = x.next[i]
            update[i] = x
            count[i] = c
        return update, count

    def getkth(self, k):
        "starts from 0"
        if k >= len(self):
            raise IndexError
        k += 1  # self has index -1
        h = len(self.next) - 1
        x = self
        while k:
            while x.next[h] is None or x.count[h] > k:
                h -= 1
            k -= x.count[h]
            x = x.next[h]
        return x.key

    def nextNode(self, key, update=None):
        if update is None:
            update = self._updateList(key)[0]
        if update:
            ans = update[0].next[0]
            if ans is not None:
                return ans
        return None

    def nextKey(self, key):
        """nextKey(key) >= key"""
        ans = self.nextNode(key)
        return (ans.key
                if ans is not None
                else None)

    def lastKey(self, key):
        """lastKey(key) < key"""
        update = self._updateList(key)[0]
        return (update[0].key
                if update
                else None)

    def find(self, key, update=None):
        ans = self.nextNode(key, update)
        return (ans
                if ans is not None and ans.key == key
                else None)

    def insert(self, node):
        # nup = len(self.next)
        while len(self.next) < len(node.next):
            self.next.append(None)
            self.count.append(self._len)
        update, index = self._updateList(node.key)
        # print(index)
        # for i in range(nup, len(self.count)):
        #     self.count[i] += 1
        nindex = index[0] + 1
        if self.find(node.key, update) is None:
            self._len += 1
            for i in range(len(node.next)):
                node.next[i] = update[i].next[i]
                update[i].next[i] = node
                node.count[i] = index[i] + update[i].count[i] + 1 - nindex
                update[i].count[i] = nindex - index[i]
            for i in range(len(node.next), len(update)):
                update[i].count[i] += 1

    def remove(self, key):
        update = self._updateList(key)[0]
        node = self.find(key, update)
        if node is None:
            raise KeyError
        self._len -= 1
        for i in range(len(node.next)):
            update[i].next[i] = node.next[i]
            update[i].count[i] += node.count[i] - 1
        for i in range(len(node.next), len(update)):
            update[i].count[i] -= 1

    @staticmethod
    def randomHeight():

        p = 2

        r = p * random()
        ans = 1
        while r < 1:
            r = r * p
            ans += 1
        return ans


class SortedSet(AbstractSkipList):

    Node = namedtuple('Node', 'key next count')

    def __init__(self, iterable=()):
        self.head = self.Node(None, [], [])
        self._len = 0
        for i in iterable:
            self.add(i)

    def pop(self):
        """Pops the first element"""
        try:
            x = next(iter(self))
            self.remove(x)
            return x
        except StopIteration:
            raise KeyError('pop from an empty set')
            # raise KeyError('pop from an empty set') from None

    def add(self, key):
        height = self.randomHeight()
        self.insert(self.Node(key, [None] * height, [0] * height))

    def __repr__(self):
        return '{%s}' % (', '.join(map(str, iter(self))))


class SortedDict(AbstractSkipList):

    Node = namedtuple('Node', 'key val next count')

    def __init__(self, iterable=()):
        self.head = self.Node(None, None, [], [])
        self._len = 0
        if hasattr(iterable, 'keys') and hasattr(iterable, '__getitem__'):
            for i in iterable.keys():
                self[i] = iterable[i]
        else:
            for i, j in iterable:
                self[i] = j

    def keys(self):
        return list(self)

    def __getitem__(self, key):
        x = self.find(key)
        if x is None:
            raise KeyError
        else:
            return x.val

    def __setitem__(self, key, value):
        try:
            self.remove(key)
        except KeyError:
            pass
        height = self.randomHeight()
        self.insert(self.Node(key, value, [None] * height, [0] * height))

    def __delitem__(self, key):
        self.remove(key)

    def __repr__(self):
        return '{%s}' % (', '.join('%s: %s' % (k, self[k]) for k in self))


if __name__ == '__main__':
    from random import sample

    def display(a):
        while a is not None:
            # if sys.version_info.major < 3:
            #     print (a.key if a.key is not None else 'N') + ' | ',
            # else:
            print(a.key if a.key is not None else 'N', end=' | ')
            print(*('(%s, %s)' % (i.key if i is not None else 'N', c)
                    for i, c in zip(a.next, a.count)))
            a = a.next[0]
    n = SortedSet()
    for i in sample(range(5), 5):
        n.add(i)
        display(n)
        print(n.getkth(0))
        print("----------")
    for i in sample(range(5), 0):
        n.remove(i)
        display(n)
        print("----------")
