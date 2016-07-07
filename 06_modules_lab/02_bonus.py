import sys

if len(sys.argv) > 2:
    try:
        first_number = int(sys.argv[1])
        seconfd_number = int(sys.argv[2])
        print "The sum of %d and %d is %d" % (first_number,seconfd_number, first_number + seconfd_number )
    except ValueError:
        print "Pleased pass 2 numeric arguments only"
else:
    program_name = sys.argv[0]
    print "Please pass 2 arguments, Usage: %s <first_number> <seconfd_number>" % program_name