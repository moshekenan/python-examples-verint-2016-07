"""
Files excersize #2
Create output file from 2 input files
"""
import sys
import itertools

(src1, src2, dst) = sys.argv[1:]

src1_lines = []
src2_lines = []

with open(src1, "r") as fin1:
    for line1 in fin1:
        src1_lines.append(line1)

with open(src2, "r") as fin2:
    for line2 in fin2:
        src2_lines.append(line2)

with open(dst, "a") as fout:
    for (lines1, lines2) in itertools.izip_longest(src1_lines, src2_lines, fillvalue=''): 
        fout.write(lines1)
        fout.write(lines2)