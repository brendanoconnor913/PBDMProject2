#!/usr/bin/python

import sys
import operator

current_time = None
current_count = 0
word = None
timedict = {}

for line in sys.stdin:
    line = line.strip()
    # Get time and count
    time, count = line.split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        continue

    # If same time add count to counter
    if current_time == time:
        current_count += count
    else:
        # If all times counted add to dict
        if current_time:
            timedict[current_time] = current_count

        current_count = count
        current_word = word

# Sort the times by count and get the top 10
timesort = sorted(timedict.items(), key=operator.itemgetter(1), reverse=True)
topten = timesort[:10]

# Output each top ten
for time, count in topten:
    print '%s\t%s' % (time, count)