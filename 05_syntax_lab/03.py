"""
Syntax excersize #3
"""
sum_of_digits = 0
rand = 0

from random import randint

rand = randint(1, 10000)
print rand

divide_by_ten = rand

while divide_by_ten != 0:
    sum_of_digits += divide_by_ten % 10
    divide_by_ten = divide_by_ten / 10
    #print divide_by_ten
    #print sum_of_digits
    
print "The sum of digits of random number: {} is {}".format(rand, sum_of_digits)