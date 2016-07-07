import sys

if len(sys.argv) > 1:
    first_number = int(sys.argv[1])
    seconfd_number = int(sys.argv[2])
    print "The sum of %d and %d is %d" % (first_number,seconfd_number, first_number + seconfd_number )
else:
    program_name = sys.argv[0]
    print "Usage: %s <first_number> <seconfd_number>" % program_name