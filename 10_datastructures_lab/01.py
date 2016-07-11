"""
excersize #1
Print IP address of hosts
"""

import sys

hosts = {}

with open("G:\People\Moshe\hosts.txt", "r") as fin:
    lines = [line.rstrip('\n') for line in fin]
    for line in lines:
        fields = line.split("=")
        hosts[fields[0]] = fields[1]

print hosts

if len(sys.argv) > 1:
    program_name = sys.argv[0]
    for arg in sys.argv:
        if arg == program_name: continue
        if arg in hosts:
            print "{}={}".format(arg,hosts[arg])
        else:
            print "{} not exist in hosts file".format(arg)

else:
    program_name = sys.argv[0]
    print "Usage: %s <hosts names>" % program_name


