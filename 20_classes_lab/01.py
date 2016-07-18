"""
Classes and objects no 1
"""
import sys
import os
import re

class Summer(object):

    def __init__(self):
        self._total = 0

    def add(self, *nums):
        self._total += sum([n for n in nums])

    def total(self):
        return self._total

s = Summer()
t = Summer()

s.add(10, 20)
t.add(50)
s.add(30)

# should print 60
print s.total()

# should print 50
print t.total()

