"""
Syntax excersize #2
"""
sum_of_randoms = 0
rand = 0

from random import randint

for n in range(7):
   rand = randint(1, 100)
   print rand
   sum_of_randoms  += rand
   print sum_of_randoms
   n += 1

if sum_of_randoms % 7 == 0:
  print "The sum of 7 random numbers between 1 and 100 is: {} {}".format(sum_of_randoms, "Boom")
else:
  print "The sum of 7 random numbers between 1 and 100 is: {}".format(sum_of_randoms)

    
