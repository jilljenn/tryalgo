from collections import namedtuple
from random import random

"""
Inspired by https://kunigami.blog/2012/09/25/skip-lists-in-python/
"""


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
        update = [None] * len(self.next)
        x = self
        for i in reversed(range(len(self.next))):
            while x.next[i] is not None and x.next[i].key < key:
                x = x.next[i]
            update[i] = x
        return update

    def nextNode(self, key, update=None):
        if update is None:
            update = self._updateList(key)
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
        update = self._updateList(key)
        return (update[0].key
                if update
                else None)

    def find(self, key, update=None):
        ans = self.nextNode(key, update)
        return (ans
                if ans is not None and ans.key == key
                else None)

    def insert(self, node):
        while len(self.next) < len(node.next):
            self.next.append(None)
        update = self._updateList(node.key)
        if self.find(node.key, update) is None:
            self._len += 1
            for i in range(len(node.next)):
                node.next[i] = update[i].next[i]
                update[i].next[i] = node

    def remove(self, key):
        update = self._updateList(key)
        x = self.find(key, update)
        if x is None:
            raise KeyError
        self._len -= 1
        for i in range(len(x.next)):
            update[i].next[i] = x.next[i]

    @staticmethod
    def randomHeight():
        r = 2 * random()
        ans = 1
        while r > 1:
            r = (r - 1) * 2
            ans += 1
        return ans


class SortedSet(AbstractSkipList):

    Node = namedtuple('Node', 'key next')

    def __init__(self, iterable=()):
        self.head = self.Node(None, [])
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
            raise KeyError('pop from an empty set') from None

    def add(self, key):
        super().insert(self.Node(key, [None] * self.randomHeight()))

    def __repr__(self):
        return '{%s}' % (', '.join(map(str, iter(self))))


class SortedDict(AbstractSkipList):

    Node = namedtuple('Node', 'key val next')

    def __init__(self, iterable=()):
        self.head = self.Node(None, None, [])
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
        super().insert(self.Node(key, value, [None] * self.randomHeight()))

    def __delitem__(self, key):
        self.remove(key)

    def __repr__(self):
        return '{%s}' % (', '.join('%s: %s' % (k, self[k]) for k in self))
