"""
Syntax excersize #6
"""
sum_of_digits = 0
rand1 = 0
rand2 = 0
common = 0

from random import randint

rand1 = randint(1, 10)
rand2 = randint(1, 10)
print rand1
print rand2

bigger = rand1

if rand2 > rand1:
    bigger = rand2

for n in range(bigger,100):
    if n % rand1 == 0 and n % rand2 == 0:
        common = n
        break 
   
print "The lowest common multiplication of {} and {} is {}".format(rand1, rand2, common)