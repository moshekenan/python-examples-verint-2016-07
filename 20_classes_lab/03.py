"""
Classes and objects no 2
"""
import sys
import os

class Widget(object):

    all_objects = []

    def __init__(self, name):
        self.name = name
        self.dependencies = []

    def add_dependency(self, *objects):
        for obj in objects:
            self.dependencies.append(obj)

    def build(self):
        for obj in self.dependencies:
            if obj not in Widget.all_objects:
                Widget.all_objects.append(obj)
                obj.build()
                print obj.name

luke    = Widget("Luke")
hansolo = Widget("Han Solo")
leia    = Widget("Leia")
yoda    = Widget("Yoda")
padme   = Widget("Padme Amidala")
anakin  = Widget("Anakin Skywalker")
obi     = Widget("Obi-Wan")
darth   = Widget("Darth Vader")
_all    = Widget("All")


luke.add_dependency(hansolo, leia, yoda)
leia.add_dependency(padme, anakin)
obi.add_dependency(yoda)
darth.add_dependency(anakin)

_all.add_dependency(luke, hansolo, leia, yoda, padme, anakin, obi, darth)

_all.build()
# code should print: Han Solo, Padme Amidala, Anakin Skywalker, Leia, Yoda, Luke, Obi-Wan, Darth Vader
# (can print with newlines in between modules)
