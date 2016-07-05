"""
Syntax excersize #1
"""
bigNum = 0
number = 0

while number < 10:
    print "Please enter any number"
    curNum = int(raw_input())
    if curNum > bigNum:
        bigNum = curNum

    number += 1

print "The highest number you entered is: ", bigNum        
