import sys

(src, dst) = sys.argv[1:]

with open(src, "r") as fin:
    with open(dst, "a") as fout:
        for line in fin:
            fout.write(line)