"""
Syntax excersize #4
"""
sum_of_lines = ""

while True:
    print "please type a row"
    line = raw_input()

    if line == "": break

    sum_of_lines += line
    sum_of_lines += "#"

lines_count = len(sum_of_lines.split("#"))

line_index = lines_count

while line_index > 0:
    print sum_of_lines.split("#")[line_index-1]
    line_index -= 1

