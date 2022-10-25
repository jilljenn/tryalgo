#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""\
A FIFO queue

christoph dürr - jill-jênn vie - 2015-2019
"""


# snip{ OurQueue
# pylint: disable=missing-docstring
class OurQueue:
    """A FIFO queue

    Complexity:
        all operators in amortized constant time,
        except __str__ which is linear
    """
    def __init__(self):
        self.in_stack = []        # tail
        self.out_stack = []       # head

    def __len__(self):
        return len(self.in_stack) + len(self.out_stack)

    def push(self, obj):
        self.in_stack.append(obj)

    def pop(self):
        if not self.out_stack:    # head is empty
            # Note that the in_stack is assigned to the out_stack
            #  in reverse order. This is because the in_stack stores
            #  elements from oldest to newest whereas the out_stack
            #  needs to pop elements from newest to oldest
            self.out_stack = self.in_stack[::-1]
            self.in_stack = []
        return self.out_stack.pop()
# snip}

    def __str__(self):
        return str(self.out_stack[::-1] + self.in_stack)
