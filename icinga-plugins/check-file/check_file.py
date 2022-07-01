#!/usr/bin/env python3

from os.path import exists
import sys

arguments = sys.argv[1:]

failCount = 0

for argument in arguments:

    if exists(argument):
        print("OK - File {} exists".format(argument))

    else:
        print("CRITICAL - File {} not exists".format(argument))
        failCount += 1

if failCount == 0:
    sys.exit(0)

else:
    sys.exit(2)
