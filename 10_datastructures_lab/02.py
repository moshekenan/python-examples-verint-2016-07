"""
excersize #1
Print list of all possible 3 lowercase English letters sequence
"""

letters = range(ord('a'),ord('z')+1)

c = [chr(x)+chr(y)+chr(z) for x in letters for y in letters for z in letters]

print c

