#!/usr/bin/env python

import random
import sys
import optparse

parser = optparse.OptionParser()
parser.add_option("--seed", "-s", metavar="SEED", dest="seed", type=int,
                  help="random seed value")
(options, args) = parser.parse_args()
if options.seed is not None:
    random.seed(options.seed)

numvars = random.randint(300, 1000)
numunits = random.randint(0, 25)
numlongs = random.randint(100, numvars)
numcls = numunits + numlongs

xorclsizes = []
for i in range(random.randint(100, numvars)):
    thissize = random.randint(3, 7)
    xorclsizes.append(thissize)
    numcls += 1 << (thissize - 1)

print "p cnf %d %d" % (numvars, numcls)

# longcls
for i in range(numlongs):
    for i2 in range(random.randint(2, 5)):
        lit = random.randint(1, numvars)
        if random.randint(0, 1) == 1:
            lit = -1 * lit
        sys.stdout.write("%d " % lit)

    print "0"

# units
for i in range(numunits):
    lit = random.randint(1, numvars)
    if random.randint(0, 1) == 1:
        lit = -1 * lit
    print "%d 0" % lit

# xors
for thisxorsize in xorclsizes:
    varlist = []

    # create varlist
    for a in range(thisxorsize):
        var = random.randint(1, numvars)
        while var in varlist:
            var = random.randint(1, numvars)

        # flip randomly
        if random.randint(0, 1) == 1:
            var = -1 * var

        varlist.append(var)

    # polarity of the XOR
    polarity = random.randint(0, 1)

    for i2 in range(1 << len(varlist)):
        # number of inversions is right, use it
        if bin(i2).count("1") % 2 == polarity:
            at = 0
            for var in varlist:
                lit = var

                # calculate inversion
                invert = (i2 >> at) & 1 == 1
                # if polarity :
                #    invert = not invert

                # create lit
                if invert:
                    lit = -1 * var

                # print lit
                sys.stdout.write("%d " % lit)
                at += 1

            # end of clause
            print "0"
