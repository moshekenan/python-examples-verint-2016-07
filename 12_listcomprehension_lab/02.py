"""
excersize #1
Print list of all possible 3 lowercase English letters sequence
"""

#letters = range(ord('a'),ord('z')+1)
letters = [x for x in range(256) if x >= ord('a') and x <= ord('z')]

c = [chr(x)+chr(y)+chr(z) for x in letters for y in letters for z in letters]

print c

