"""
excersize #1
Print list of all English lowercase letters
"""

#x = range(ord('a'),ord('z')+1)
lowercase_letters = [x for x in range(256) if x >= ord('a') and x <= ord('z')]
for i in lowercase_letters: print chr(i)

