#!/usr/bin/python

# Simulation for Pig Streaming
# Robert Esteves
import sys
import string

for n in sys.stdin:
    res = int(n) * int(n)
    print "%d" % (res)
