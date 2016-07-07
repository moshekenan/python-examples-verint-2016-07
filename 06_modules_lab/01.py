import sys

if len(sys.argv) > 1:
    number_of_hellos = sys.argv[1]
    for n in range(int(number_of_hellos)):
        print "Hello Python"
else:
    program_name = sys.argv[0]
    print "Usage: %s <number of hellos>" % program_name