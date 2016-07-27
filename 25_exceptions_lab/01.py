import math
def sqrt(n):
    if n < 0:
        raise ValueError("Expected parameter >= 0, Got: %d" % n)
    return math.sqrt(n)

while True:
    print "Please enter number to calculate square root:"
    number = int(raw_input())
    try:
        print sqrt(number)
    except ValueError as e:
        print "Failed to calculate sqrt of {}. Error was: {}".format(number, e.message)
    except Exception as e:
        print "Something went wrong. Sorry", e
    finally:
        print "Thanks for using Python Sqrt Calculator"
