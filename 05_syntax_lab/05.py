"""
Syntax excersize #5
"""
sum_of_digits = 0
rand = 0

from random import randint

while True:
    rand = randint(1, 1000000)
    #print rand

    if rand % 7 == 0 and rand % 13 == 0 and rand % 15 == 0: break 
   
print "The random number: {} is divisable by 7 and by 13 and by 15".format(rand)