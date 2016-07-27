import sys
import os

src = sys.argv[1]

line_count = 0

if ( not os.path.isfile(src)):
    print("Sorry, file %s file not found" % src)
else:
    with open(src, "r") as fin:
        for line in fin:
            line_count += 1

    print line_count
