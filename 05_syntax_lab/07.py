"""
Syntax excersize #7
"""
sum_of_digits = 0
rand = 0
count = 0

from random import randint

rand = randint(1, 100)
#print rand

print "please try to guess the random number between 1 and 100"

while True:
    count += 1
    guess = int(raw_input())
    #print guess

    if guess > rand:
        print "Sorry, too high, try again"
    elif guess < rand:
        print "Sorry, too low, try again"
    elif guess == rand: break
   
print "Congratulations: you have found my number in {} guesses".format(count)