"""
excersize #2
check above average grades in list
"""
from random import randint

sum_of_grades = 0

grades = range(20)

for n in grades:
   grades[n] = randint(40, 100)
   sum_of_grades += grades[n]

average = sum_of_grades/20
print grades
print "average: {}".format(average)

print "baove average grades are:"
for grade in grades:
    if grade > average:
        print "{}".format(grade)
