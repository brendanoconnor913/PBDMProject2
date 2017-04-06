#!/usr/bin/python

import sys, ast, math

# function to categorize time according to time interval it falls into
def timeperiodcat(timelist,minint):
    hrs = int(timelist[0])
    mins = int(timelist[1])
    totalmins = (hrs*60)+mins
    interval = math.floor(totalmins / minint)
    intbot = (interval*minint)
    inttop = ((interval+1)*minint)
    timbot = divmod(intbot, 60)
    timtop = divmod(inttop, 60)
    return "%i:%.2i-%i:%.2i" % (int(timbot[0] % 24),int(timbot[1]),\
                                         int(timtop[0] % 24),int(timtop[1]))

for line in sys.stdin:
    if line == "":
        continue

    try:
        # Get time posting categorize it then output it with a count of 1
        newline = ast.literal_eval(line)["created_at"]
        newline = newline.strip()
        time = newline.split()[3]
        hrmin = time.split(":")
        print '%s\t%s' % (timeperiodcat(hrmin, 7), 1)
    except:
        continue
