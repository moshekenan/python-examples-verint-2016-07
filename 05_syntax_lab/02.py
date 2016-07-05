"""
Syntax excersize #2
"""
sum = 0
number = 0
Boom = ""
rand = 0

from random import randint

while number < 7:
   rand = randint(1, 100)
   print rand
   sum  += rand
   print sum
   number += 1

if sum % 7 == 0:
    Boom = "Boom"

print "The sum of 7 random numbers between 1 and 100 is: {} {}".format(sum, Boom)

    
